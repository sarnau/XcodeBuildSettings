#!/usr/bin/env python
# -*- coding: utf-8 -*-

import plistlib
import subprocess
import tempfile
import os

# Xcode searches all plugins for xcspecs plists, which contain custom configurations
# The Clang plugin has a selection of warnings defined, they are converted into
# clang commandline parameter via this xcspec file.
# All clang warnings are documented at https://clang.llvm.org/docs/DiagnosticsReference.html

appPath = '/Applications/Xcode.app'
xcodePluginsResourcesPath = appPath + "/Contents/PlugIns/Xcode3Core.ideplugin/Contents/SharedSupport/Developer/Library/Xcode/Plug-ins/Clang LLVM 1.0.xcplugin/Contents/Resources/"

# This file contains the user readable name and descriptions of the visible options
Apple_Clang_strings = plistlib.load(open(xcodePluginsResourcesPath + "English.lproj/Apple Clang.strings","rb"), fmt=plistlib.FMT_BINARY)

# load the xcspec file (after converting it from the ASCII plist format to XML) and generate categories, just like Xcode
tempSpecFile = tempfile.gettempdir() + "/Clang_LLVM_xcspec.xml"
subprocess.run(["plutil", "-convert","xml1","-o",tempSpecFile,xcodePluginsResourcesPath + "Clang LLVM 1.0.xcspec"])
with open('Apple Clang Options.md', 'w') as f:
    for plistComponent in plistlib.load(open(tempSpecFile,"rb")):
        if 'FileTypes' not in plistComponent: # no assigned filetypes => we can ignore that
            continue
        print("# %s" % (plistComponent['Name']), file=f)
        if 'Description' in plistComponent:
            print("%s" % plistComponent['Description'], file=f)
        if 'FileTypes' in plistComponent:
            fileTypeStr = []
            for filetype in plistComponent['FileTypes']:
                if '[GCC_INPUT_FILETYPE]-value-[%s]' % filetype in Apple_Clang_strings:
                    filetype = Apple_Clang_strings['[GCC_INPUT_FILETYPE]-value-[%s]' % filetype]
                fileTypeStr.append(filetype)
            print('File types: %s' % ', '.join(fileTypeStr), file=f)
        if 'SourceFileOption' in plistComponent:
            print("Source File Option: `%s`" % plistComponent['SourceFileOption'], file=f)
        if 'OverridingProperties' in plistComponent:
            print('', file=f)
            print('| Overriding Properties | Value |', file=f)
            print('| -------- | --------  |', file=f)
            for property in plistComponent['OverridingProperties']:
                print('| `%s` | `%s` |' % (property,plistComponent['OverridingProperties'][property]), file=f)
        print("", file=f)
        if 'Options' in plistComponent:
            print("Special meanings:", file=f)
            print("`$(value)` is replaced by the selected value or the default value.", file=f)
            print("", file=f)

            categories = {}
            for option in plistComponent['Options']:
                categoryKey = 'None'
                if 'Category' in option:
                    categoryKey = option['Category']
                if categoryKey not in categories:
                    categories[categoryKey] = []
                categories[categoryKey].append(option)

            for category in sorted(categories):
                categoryName = category
                if '[%s]-category' % categoryName in Apple_Clang_strings:
                    categoryName = Apple_Clang_strings['[%s]-category' % categoryName]
                print('## %s' % categoryName, file=f)
                for option in categories[category]:
                    name = None
                    if '[%s]-name' % option['Name'] in Apple_Clang_strings:
                        name = Apple_Clang_strings['[%s]-name' % option['Name']]
                        hasHeader = True
                    else: # some are not in the localized file, but might be in the xcspec file itself.
                        if 'DisplayName' in option:
                            name = option['DisplayName']
                            hasHeader = True
                    if name:
                        print('### %s - `%s` (%s)' % (name,option['Name'],option['Type']), file=f)
                    else:
                        print('### `%s` (%s)' % (option['Name'],option['Type']), file=f)
                    if '[%s]-description' % option['Name'] in Apple_Clang_strings:
                        print("%s" % Apple_Clang_strings['[%s]-description' % option['Name']], file=f)
                    elif 'Description' in option:
                        print(option['Description'], file=f)
                        print('', file=f)

                    if 'DefaultValue' in option:
                        defaultValue = option['DefaultValue']
                        defaultInTable = False
                        if 'CommandLineArgs' in option:
                            for arg in option['CommandLineArgs']:
                                if arg==defaultValue:
                                    defaultInTable = True
                                    break
                        if 'Values' in option:
                            if defaultValue in option['Values']:
                                defaultInTable = True
                        if len(defaultValue)==0:
                            defaultValue = '""'
                        else:
                            defaultValue = '`%s`' % defaultValue
                        if not defaultInTable:
                            print("Default value: **%s**" % defaultValue, file=f)
                    else:
                        defaultValue = ''

                    usedDefault = False
                    valList = []
                    if 'Values' in option:
                        valuesInTable = 0
                        for val in option['Values']:
                            if 'CommandLineArgs' in option:
                                for arg in option['CommandLineArgs']:
                                    if arg==val:
                                        valuesInTable += 1
                            if val == option['DefaultValue']:
                                val = '**`%s`**' % val # Default value in bold
                            else:
                                val = '`%s`' % val
                            valList.append(val)

                    if 'Condition' in option:
                        print('Condition: `%s`' % option['Condition'], file=f)
                    if 'ConditionFlavors' in option and len(option['ConditionFlavors']):
                        print('Condition Flavors: `%s`' % ', '.join(option['ConditionFlavors']), file=f)
                    if 'Architectures' in option:
                        print('Architectures: `%s`' % ', '.join(option['Architectures']), file=f)
                
                    if 'FileTypes' in option:
                        fileTypeStr = []
                        for filetype in option['FileTypes']:
                            if '[GCC_INPUT_FILETYPE]-value-[%s]' % filetype in Apple_Clang_strings:
                                filetype = Apple_Clang_strings['[GCC_INPUT_FILETYPE]-value-[%s]' % filetype]
                            fileTypeStr.append(filetype)
                        print('File types: %s' % ', '.join(fileTypeStr), file=f)

                    hasTable = False
                    if 'CommandLineArgs' in option:
                        hasTable = True
                        if type(option['CommandLineArgs']) == type({}):
                            print('', file=f)
                            print('| %s value | Command Line Argument |' % option['Type'], file=f)
                            print('| ----- | -------- |', file=f)
                            otherwiseVal = ''
                            remainingValues = valList[:]
                            for arg in option['CommandLineArgs']:
                                val = ' '.join(option['CommandLineArgs'][arg])
                                if len(val)==0:
                                    val = ''
                                else:
                                    val = '`%s`' % val
                                argVal = '`%s`' % arg
                                if argVal==defaultValue:
                                    argVal = '**%s**' % argVal # Default value in bold
                                elif argVal == '``':
                                    argVal = '`<<empty>>`'
                                if argVal in remainingValues:
                                    remainingValues.remove(argVal)
                                if len(remainingValues) and arg == '<<otherwise>>':
                                    otherwiseVal = val
                                    continue
                                print('| %s | %s |' % (argVal,val), file=f)
                            for arg in remainingValues:
                                val = otherwiseVal.replace("$(value)", arg.replace('`','').replace('*',''))
                                if len(val) != 0:
                                    val = '`%s`' % val
                                print('| %s | %s |' % (arg,val), file=f)
                            print('', file=f)
                        else:
                            print('', file=f)
                            if len(option['CommandLineArgs']) == 1 and '$(value)' in option['CommandLineArgs'][0] and len(valList):
                                print('| %s value | Command Line Argument |' % option['Type'], file=f)
                                print('| ----- | -------- |', file=f)
                                for arg in valList:
                                    print('| %s | `%s` |' % (arg,option['CommandLineArgs'][0].replace("$(value)", arg.replace('`','').replace('*',''))), file=f)
                            else:
                                print('| Command Line Argument |', file=f)
                                print('| -------- |', file=f)
                                print('| `%s` |' % (' '.join(option['CommandLineArgs'])), file=f)

                    if 'CommandLinePrefixFlag' in option:
                        hasTable = True
                        print('', file=f)
                        print('| Command Line Argument |', file=f)
                        print('| -------- |', file=f)
                        print('| `%s$(value)` |' % (option['CommandLinePrefixFlag']), file=f)
                    if 'CommandLineFlag' in option:
                        hasTable = True
                        print('', file=f)
                        print('| Command Line Argument |', file=f)
                        print('| -------- |', file=f)
                        if option['Type'] == 'Boolean':
                            print('| `%s` |' % (option['CommandLineFlag']), file=f)
                        else:
                            print('| `%s $(%s)` |' % (option['CommandLineFlag'],option['Type'].lower()), file=f)

                    if 'AdditionalLinkerArgs' in option:
                        hasTable = True
                        if type(option['AdditionalLinkerArgs']) == type({}):
                            print('', file=f)
                            print('| %s value | Linker Argument |' % option['Type'], file=f)
                            print('| ----- | -------- |', file=f)
                            otherwiseVal = ''
                            remainingValues = valList[:]
                            for arg in option['AdditionalLinkerArgs']:
                                val = ','.join(option['AdditionalLinkerArgs'][arg])
                                if len(val)==0:
                                    val = ''
                                else:
                                    val = '`%s`' % val
                                argVal = '`%s`' % arg
                                if argVal==defaultValue:
                                    argVal = '**%s**' % argVal # Default value in bold
                                elif argVal == '``':
                                    argVal = '`<<empty>>`'
                                if argVal in remainingValues:
                                    remainingValues.remove(argVal)
                                if len(remainingValues) and arg == '<<otherwise>>':
                                    otherwiseVal = val
                                    continue
                                print('| %s | %s |' % (argVal,val), file=f)
                            for arg in remainingValues:
                                val = otherwiseVal.replace("$(value)", arg.replace('`','').replace('*',''))
                                if len(val) != 0:
                                    val = '`%s`' % val
                                print('| %s | %s |' % (arg,val), file=f)
                            print('', file=f)
                        else:
                            print('', file=f)
                            print('| Linker Argument |', file=f)
                            print('| -------- |', file=f)
                            print('| `%s` |' % (' '.join(option['AdditionalLinkerArgs'])), file=f)

                    if not hasTable:
                        print('', file=f)
                        if len(valList) != 0:
                            print('| %s value |' % option['Type'], file=f)
                            print('| -------- |', file=f)
                            for arg in valList:
                                print('| %s |' % (arg), file=f)
                            print('', file=f)
                        print('The option only sets an internal value, which is used by other options as a condition or as an internal parameter.', file=f)

                    print('\n', file=f)
                print('\n', file=f)
