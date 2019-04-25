# Standard Properties

Special meanings:
`$(value)` is replaced by the selected value or the default value.

## None
### Active Build Action - `ACTION` (string)
A string identifying the build system action being performed.

Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Active Build Components - `BUILD_COMPONENTS` (stringlist)
A list of components being built during this action.

Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Project Name - `PROJECT_NAME` (string)
The name of the current project.

Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Target Name - `TARGET_NAME` (string)
The name of the current target.

Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Base SDK - `SDKROOT` (string)
The name or path of the base SDK being used during the build. The product will be built against the headers and libraries located inside the indicated SDK. This path will be prepended to all search paths, and will be passed through the environment to the compiler and linker. Additional SDKs can be specified in the `ADDITIONAL_SDKS` setting.
Default value: **""**
Condition Flavors: `arch`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Additional SDKs - `ADDITIONAL_SDKS` (stringlist)
The locations of any sparse SDKs that should be layered on top of the one specified by `SDKROOT`. If more than one SDK is listed, the first one has highest precedence. Every SDK specified in this setting should be a "sparse" SDK, for example, not an SDK for an entire macOS release.
Default value: **""**
Condition Flavors: `arch`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Supported Platforms - `SUPPORTED_PLATFORMS` (stringlist)
The list of supported platforms from which a base SDK can be used. This setting is used if the product can be built for multiple platforms using different SDKs.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Precompiled Headers Cache Path - `SHARED_PRECOMPS_DIR` (string)
The path where precompiled prefix header files are placed during a build. Defaults to `$(OBJROOT)/SharedPrecompiledHeaders`. Using a common location allows precompiled headers to be shared between multiple projects.
Default value: **`$(OBJROOT)/SharedPrecompiledHeaders`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Header Search Paths - `HEADER_SEARCH_PATHS` (pathlist)
This is a list of paths to folders to be searched by the compiler for included or imported header files when compiling C, Objective-C, C++, or Objective-C++. Paths are delimited by whitespace, so any paths with spaces in them need to be properly quoted.
Default value: **""**
Condition Flavors: `arch`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### User Header Search Paths - `USER_HEADER_SEARCH_PATHS` (pathlist)
This is a list of paths to folders to be searched by the compiler for included or imported user header files (those headers listed in quotes) when compiling C, Objective-C, C++, or Objective-C++. Paths are delimited by whitespace, so any paths with spaces in them need to be properly quoted. See `ALWAYS_SEARCH_USER_PATHS` for more details on how this setting is used. If the compiler doesn't support the concept of user headers, then the search paths are prepended to the any existing header search paths defined in `HEADER_SEARCH_PATHS`.
Default value: **""**
Condition Flavors: `arch`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Library Search Paths - `LIBRARY_SEARCH_PATHS` (pathlist)
This is a list of paths to folders to be searched by the linker for libraries used by the product. Paths are delimited by whitespace, so any paths with spaces in them need to be properly quoted.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Framework Search Paths - `FRAMEWORK_SEARCH_PATHS` (pathlist)
This is a list of paths to folders containing frameworks to be searched by the compiler for both included or imported header files when compiling C, Objective-C, C++, or Objective-C++, and by the linker for frameworks used by the product. Paths are delimited by whitespace, so any paths with spaces in them must be properly quoted.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Rez Search Paths - `REZ_SEARCH_PATHS` (pathlist)
This is a list of paths to search for files with resource manager resources. Paths are delimited by whitespace, so any paths with spaces in them need to be properly quoted.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Always Search User Paths (Deprecated) - `ALWAYS_SEARCH_USER_PATHS` (bool)
This setting is deprecated as of Xcode 8.3 and may not be supported in future versions. It is recommended that you disable the setting.

If enabled, both `#include <header.h>`-style and `#include "header.h"`-style directives search the paths in `USER_HEADER_SEARCH_PATHS` before `HEADER_SEARCH_PATHS`. As a consequence, user headers, such as your own `String.h` header, have precedence over system headers when using `#include <header.h>`. This is done using the `-iquote` flag for the paths provided in `USER_HEADER_SEARCH_PATHS`. If disabled and your compiler fully supports separate user paths, user headers are only accessible with `#include "header.h"`-style preprocessor directives.

For backwards compatibility reasons, this setting is enabled by default. Disabling it is strongly recommended.
Default value: **`YES`**
Condition Flavors: `arch`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `ENABLE_DEFAULT_HEADER_SEARCH_PATHS` (bool)
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Sub-Directories to Include in Recursive Searches - `INCLUDED_RECURSIVE_SEARCH_PATH_SUBDIRECTORIES` (stringlist)
This is a list of `fnmatch()`-style patterns of file or directory names to include when performing a recursive search. By default, this is empty and is only customized when you want to provide exceptions to the list of filename patterns provided in `EXCLUDED_RECURSIVE_SEARCH_PATH_SUBDIRECTORIES`.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Sub-Directories to Exclude in Recursive Searches - `EXCLUDED_RECURSIVE_SEARCH_PATH_SUBDIRECTORIES` (stringlist)
This is a list of `fnmatch()`-style patterns of file or directory names to exclude when performing a recursive search. By default, this is set to `\*.nib \*.lproj \*.framework \*.gch \*.xcode (\*) .DS_Store CVS .svn .git .hg`. Normally, if you override this value you should include the default values via the `$(inherited)` macro.
Default value: **`*.nib *.lproj *.framework *.gch *.xcode* *.xcassets (*) .DS_Store CVS .svn .git .hg *.pbproj *.pbxproj`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `PRECOMP_DESTINATION_DIR` (string)
Default value: **`$(TEMP_DIR)/PrefixHeaders`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Versioning System - `VERSIONING_SYSTEM` (enum)
Selects the process used for version-stamping generated files.

* *None:* Use no versioning system.
* *Apple Generic:* Use the current project version setting. [apple-generic]

| enum value |
| -------- |
| **``** |
| `apple-generic` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Current Project Version - `CURRENT_PROJECT_VERSION` (string)
This setting defines the current version of the project. The value must be a integer or floating point number, such as `57` or `365.8`.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Versioning Name Prefix - `VERSION_INFO_PREFIX` (string)
Used as a prefix for the name of the version info symbol in the generated versioning source file. If you prefix your exported symbols you will probably want to set this to the same prefix.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Versioning Name Suffix - `VERSION_INFO_SUFFIX` (string)
Used as a suffix for the name of the version info symbol in the generated versioning source file. This is rarely used.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Versioning Username - `VERSION_INFO_BUILDER` (string)
This defines a reference to the user performing a build to be included in the generated Apple Generic Versioning stub. Defaults to the value of the `USER` environment variable.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Generated Versioning Variables - `VERSION_INFO_EXPORT_DECL` (string)
This defines a prefix string for the version info symbol declaration in the generated Apple Generic Versioning stub. This can be used, for example, to add an optional `export` keyword to the version symbol declaration. This should rarely be changed.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Generated Versioning Source Filename - `VERSION_INFO_FILE` (string)
Used to specify a name for the source file that will be generated by Apple Generic Versioning and compiled into your product. By default, this is set to `$(PRODUCT_NAME)_vers.c`.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Debug Information Format - `DEBUG_INFORMATION_FORMAT` (enum)
The type of debug information to produce.

* *DWARF:* Object files and linked products will use DWARF as the debug information format. [dwarf]
* *DWARF with dSYM File:* Object files and linked products will use DWARF as the debug information format, and Xcode will also produce a dSYM file containing the debug information from the individual object files (except that a dSYM file is not needed and will not be created for static library or object file products). [dwarf-with-dsym]

| enum value |
| -------- |
| **`dwarf`** |
| `dwarf-with-dsym` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `DWARF_DSYM_FILE_NAME` (string)
Default value: **`$(FULL_PRODUCT_NAME).dSYM`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `DWARF_DSYM_FOLDER_PATH` (string)
Default value: **`$(CONFIGURATION_BUILD_DIR)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `DWARF_DSYM_FILE_SHOULD_ACCOMPANY_PRODUCT` (bool)
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `COLOR_DIAGNOSTICS` (bool)
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Scan All Source Files for Includes - `SCAN_ALL_SOURCE_FILES_FOR_INCLUDES` (bool)
Activating this setting will cause all source files to be scanned for includes (for example, of header files) when computing the dependency graph, in which case if an included file is changed then the including file will be rebuilt next time a target containing it is built. Normally only certain types of files, such as C-language source files, are scanned.

This setting is useful if your project contains files of unusual types, which are compiled using a custom build rule.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Generate Profiling Code - `GENERATE_PROFILING_CODE` (bool)
Activating this setting will cause the compiler and linker to generate profiling code. For example, GCC will generate code suitable for use with `gprof(1)`.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `ENABLE_BITCODE` (bool)
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `HIDE_BITCODE_SYMBOLS` (bool)
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `BITCODE_GENERATION_MODE` (enum)

| enum value |
| -------- |
| **`marker`** |
| `bitcode` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `STRIP_BITCODE_FROM_COPIED_FILES` (bool)
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Precompiled Header Uses Files From Build Directory - `PRECOMPS_INCLUDE_HEADERS_FROM_BUILT_PRODUCTS_DIR` (bool)
This setting allows for better control of sharing precompiled prefix header files between projects. By default, Xcode assumes that the prefix header file may include header files from the build directory if the build directory is outside of the project directory. Xcode cannot determine this ahead of time since other projects may not have been built into the shared build directory at the time the information is needed.

If your prefix file never includes files from the build directory you may set this to `NO` to improve sharing of precompiled headers. If the prefix does use files from a build directory that is inside your project directory, you may set this to `YES` to avoid unintended sharing that may result in build failures.
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `EXCLUDED_INSTALLSRC_SUBDIRECTORY_PATTERNS` (stringlist)
Default value: **`.DS_Store .svn .git .hg CVS`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Mach-O Type - `MACH_O_TYPE` (enum)
This setting determines the format of the produced binary and how it can be linked when building other binaries. For information on binary types, see [Building Mach-O Files](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/MachOTopics/1-Articles/building_files.html#//apple_ref/doc/uid/TP40001828-SW1) in [Mach-O Programming Topics](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/MachOTopics/0-Introduction/introduction.html).

* *Executable:* Executables and standalone binaries and cannot be linked. [mh_execute]
* *Dynamic Library:* Dynamic libraries are linked at build time and loaded automatically when needed. [mh_dylib]
* *Bundle:* Bundle libraries are loaded explicitly at run time. [mh_bundle]
* *Static Library:* Static libraries are linked at build time and loaded at execution time. [staticlib]
* *Relocatable Object File:* Object files are single-module files that are linked at build time. [mh_object]
Default value: **""**

| enum value |
| -------- |
| `mh_execute` |
| `mh_dylib` |
| `mh_bundle` |
| `staticlib` |
| `mh_object` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Initialization Routine - `INIT_ROUTINE` (string)
This is the name of the routine to use for initialization.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Link With Standard Libraries - `LINK_WITH_STANDARD_LIBRARIES` (bool)
When this setting is enabled, the compiler driver will automatically pass its standard libraries to the linker to use during linking. If desired, this flag can be used to disable linking with the standard libraries, and then individual libraries can be passed as `OTHER_LDFLAGS`.
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Preserve Private External Symbols - `KEEP_PRIVATE_EXTERNS` (bool)
Activating this setting will preserve private external symbols, rather than turning them into static symbols. This setting is also respected when performing a single-object prelink.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Exported Symbols File - `EXPORTED_SYMBOLS_FILE` (string)
This is a project-relative path to a file that lists the symbols to export. See `ld -exported_symbols_list` for details on exporting symbols.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Unexported Symbols File - `UNEXPORTED_SYMBOLS_FILE` (string)
A project-relative path to a file that lists the symbols not to export. See `ld -exported_symbols_list` for details on exporting symbols.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Separately Edit Symbols - `SEPARATE_SYMBOL_EDIT` (bool)
Activating this setting when the linked product's symbols are to be edited will cause editing to occur via a separate invocation of `nmedit(1)`. Otherwise editing will occur during linking, if possible.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Current Library Version - `DYLIB_CURRENT_VERSION` (string)
This setting defines the current version of any framework built by the project. As with `CURRENT_PROJECT_VERSION`, the value must be an integer or floating point number, such as `57` or `365.8`. By default, it is set to `$(CURRENT_PROJECT_VERSION)`. See [Dynamic Library Design Guidelines](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/DynamicLibraryDesignGuidelines.html#//apple_ref/doc/uid/TP40002013-SW19) in [Dynamic Library Programming Topics](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/DynamicLibraries/000-Introduction/Introduction.html) for details on assigning version numbers of dynamic libraries.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Compatibility Version - `DYLIB_COMPATIBILITY_VERSION` (string)
Determines the compatibility version of the resulting library, bundle, or framework binary. See [Dynamic Library Design Guidelines](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/DynamicLibraryDesignGuidelines.html#//apple_ref/doc/uid/TP40002013-SW19) in [Dynamic Library Programming Topics](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/DynamicLibraries/000-Introduction/Introduction.html) for details on assigning version numbers of dynamic libraries.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Dynamic Library Install Name - `LD_DYLIB_INSTALL_NAME` (path)
Sets an internal `install path` (`LC_ID_DYLIB`) in a dynamic library. Any clients linked against the library will record that path as the way `dyld` should locate this library. If this option is not specified, then the `-o` path will be used. This setting is ignored when building any product other than a dynamic library. See [Dynamic Library Programming Topics](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/DynamicLibraries/000-Introduction/Introduction.html).
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Dynamic Library Install Name Base - `DYLIB_INSTALL_NAME_BASE` (String)
Sets the base value for the internal `install path` (`LC_ID_DYLIB`) in a dynamic library. This will be combined with the `EXECUTABLE_PATH` to form the full install path. Setting `LD_DYLIB_INSTALL_NAME` directly will override this setting. This setting defaults to the target's `INSTALL_PATH`. It is ignored when building any product other than a dynamic library.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Symbol Ordering Flags - `SECTORDER_FLAGS` (stringlist)
These flags are typically used to specify options for ordering symbols within segments, for example the `-sectorder` option to `ld`.

Generally you should not specify symbol ordering options in Debug or Development configurations, as this will make the linked binary less readable to the debugger. Use them only in Release or Deployment configurations.
Default value: **""**
Condition Flavors: `arch`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Order File - `ORDER_FILE` (string)
The path to a file that alters the order in which functions and data are laid out.

For each section in the output file, any symbol in that section that are specified in the order file is moved to the start of its section and laid out in the same order as in the order file. Order files are text files with one symbol name per line. Lines starting with a `#` are comments. A symbol name may be optionally preceded with its object file leafname and a colon (for example, `foo.o:_foo`). This is useful for static functions/data that occur in multiple files. A symbol name may also be optionally preceded with the architecture (for example, `ppc:_foo` or `ppc:foo.o:_foo`). This enables you to have one order file that works for multiple architectures. Literal C-strings may be ordered by quoting the string in the order file (for example, `"Hello, world\n"`).

Generally you should not specify an order file in Debug or Development configurations, as this will make the linked binary less readable to the debugger. Use them only in Release or Deployment configurations.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Runpath Search Paths - `LD_RUNPATH_SEARCH_PATHS` (stringlist)
This is a list of paths to be added to the `runpath` search path list for the image being created. At runtime, `dyld` uses the `runpath` when searching for dylibs whose load path begins with `@rpath/`. See [Dynamic Library Programming Topics](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/DynamicLibraries/000-Introduction/Introduction.html).
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Write Link Map File - `LD_GENERATE_MAP_FILE` (bool)
Activating this setting will cause the linker to write a map file to disk, which details all symbols and their addresses in the output image. The path to the map file is defined by the `LD_MAP_FILE_PATH` setting.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Path to Link Map File - `LD_MAP_FILE_PATH` (path)
This setting defines the path to the map file written by the linker when the `LD_GENERATE_MAP_FILE` setting is activated. By default, a separate file will be written for each architecture and build variant, and these will be generated in the Intermediates directory for the target whose product is being linked.
Default value: **`$(TARGET_TEMP_DIR)/$(PRODUCT_NAME)-LinkMap-$(CURRENT_VARIANT)-$(CURRENT_ARCH).txt`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Warning Linker Flags - `WARNING_LDFLAGS` (stringlist)
These flags are passed with linker invocations, and by default give the `-no_arch_warnings` flag to the linker to avoid many warnings being generated during multi-architecture builds.
Default value: **""**
Condition Flavors: `arch`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Other Linker Flags - `OTHER_LDFLAGS` (stringlist)
Options defined in this setting are passed to invocations of the linker.
Default value: **""**
Condition Flavors: `arch`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Other Librarian Flags - `OTHER_LIBTOOLFLAGS` (stringlist)
Options defined in this setting are passed to all invocations of the archive librarian, which is used to generate static libraries.
Default value: **""**
Condition Flavors: `arch`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Dead Code Stripping - `DEAD_CODE_STRIPPING` (bool)
Activating this setting causes the `-dead_strip` flag to be passed to `ld(1)` via `cc(1)` to turn on dead code stripping.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Don't Dead-Strip Inits and Terms - `PRESERVE_DEAD_CODE_INITS_AND_TERMS` (bool)
Activating this setting, in combination with the `DEAD_CODE_STRIPPING` (`-dead_strip`) option, causes the `-no_dead_strip_inits_and_terms` flag to be passed to `ld(1)` via `cc(1)` to disable dead code stripping for initialization and termination routines. This option should not be used without the aforementioned `DEAD_CODE_STRIPPING` option.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Bundle Loader - `BUNDLE_LOADER` (string)
Specifies the executable that will load the bundle output file being linked. Undefined symbols from the bundle are checked against the specified executable as if it is one of the dynamic libraries the bundle was linked with.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Display Mangled Names - `LINKER_DISPLAYS_MANGLED_NAMES` (bool)
Activating this setting causes the linker to display mangled names for C++ symbols. Normally, this is not recommended, but turning it on can help to diagnose and solve C++ link errors.

| bool value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Xlinker --no-demangle` |



### Perform Single-Object Prelink - `GENERATE_MASTER_OBJECT_FILE` (bool)
Activating this setting will cause the object files built by a target to be prelinked using `ld -r` into a single object file, and that object file will then be linked into the final product. This is useful to force the linker to resolve symbols and link the object files into a single module before building a static library. Also, a separate set of link flags can be applied to the prelink allowing additional control over, for instance, exported symbols.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Prelink libraries - `PRELINK_LIBS` (stringlist)
Additional libraries to pass when performing a single-object prelink.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Single-Object Prelink Flags - `PRELINK_FLAGS` (stringlist)
Additional flags to pass when performing a single-object prelink.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Generate Position-Dependent Executable - `LD_NO_PIE` (bool)
Activating this setting will prevent Xcode from building a main executable that is position independent (PIE). When targeting macOS 10.7 or later, PIE is the default for main executables, so activating this setting will change that behavior. When targeting OS X 10.6 or earlier, or when building for i386, PIE is not the default, so activating this setting does nothing.

You cannot create a PIE from `.o` files compiled with `-mdynamic-no-pic`. Using PIE means the codegen is less optimal, but the address randomization adds some security.
Condition Flavors: `arch, sdk`

| bool value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Xlinker -no_pie` |



### Quote Linker Arguments - `LD_QUOTE_LINKER_ARGUMENTS_FOR_COMPILER_DRIVER` (Boolean)
This setting controls whether arguments to the linker should be quoted using `-Xlinker`. By default, Xcode invokes the linker by invoking the driver of the compiler used to build the source files in the target, and passing `-Xlinker` to quote arguments will cause the compiler driver to pass them through to the linker (rather than trying to evaluate them within the driver). By default, this setting is enabled. Disabling it will cause Xcode to not use `-Xlinker` to pass arguments to the linker. Disabling this setting is useful if the target has instructed Xcode to use an alternate linker (for example, by setting the `LD` setting to the path to another linker) and that alternate linker does not recognize `-Xlinker`.
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Path to Linker Dependency Info File - `LD_DEPENDENCY_INFO_FILE` (Path)
This setting defines the path to which the linker should emit information about what files it used as inputs and generated. Xcode uses this information for its dependency tracking. Setting the value of this setting to empty will disable passing this option to the linker.
Default value: **`$(OBJECT_FILE_DIR_$(CURRENT_VARIANT))/$(CURRENT_ARCH)/$(PRODUCT_NAME)_dependency_info.dat`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Dynamic Library Allowable Clients - `LD_DYLIB_ALLOWABLE_CLIENTS` (StringList)
This setting restricts the clients allowed to link a dylib by passing `-allowable_client` to the linker for each supplied value.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Product Name - `PRODUCT_NAME` (string)
This is the basename of the product generated by the target.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Executable Prefix - `EXECUTABLE_PREFIX` (string)
The prefix used for the executable product generated by the target, which has a default value based on the product type.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Executable Extension - `EXECUTABLE_EXTENSION` (string)
This is the extension used for the executable product generated by the target, which has a default value based on the product type.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Wrapper Extension - `WRAPPER_EXTENSION` (string)
The extension used for product wrappers, which has a default value based on the product type.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CURRENT_VERSION` (string)
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `VERSIONS_FOLDER_PATH` (string)
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Private Headers Folder Path - `PRIVATE_HEADERS_FOLDER_PATH` (string)
The location to copy the private headers to during building, relative to the built products folder.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Public Headers Folder Path - `PUBLIC_HEADERS_FOLDER_PATH` (string)
The location to copy the public headers to during building, relative to the built products folder.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Force Package Info Generation - `GENERATE_PKGINFO_FILE` (bool)
Forces the `PkgInfo` file to be written to wrapped products even if this file is not expected.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Info.plist File - `INFOPLIST_FILE` (string)
The project-relative path to the property list file that contains the `Info.plist` information used by bundles. For details on information property list files, see [Information Property List Files](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPRuntimeConfig/Articles/ConfigFiles.html#//apple_ref/doc/uid/20002091-CJBJIEDH) in [Runtime Configuration Guidelines](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPRuntimeConfig/000-Introduction/introduction.html).
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Preprocess Info.plist File - `INFOPLIST_PREPROCESS` (bool)
Preprocess the `Info.plist` file using the C Preprocessor.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Expand Build Settings in Info.plist File - `INFOPLIST_EXPAND_BUILD_SETTINGS` (bool)
Expand build settings in the `Info.plist` file.
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Info.plist Output Encoding - `INFOPLIST_OUTPUT_FORMAT` (Enumeration)
Specifies the output encoding for the output `Info.plist`. The output encodings can be `binary` or `XML`. By default, the output encoding will be unchanged from the input.

| Enumeration value |
| -------- |
| **`same-as-input`** |
| `XML` |
| `binary` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Create Info.plist Section in Binary - `CREATE_INFOPLIST_SECTION_IN_BINARY` (bool)
Enabling this setting will create a section in the product's linked binary containing the processed `Info.plist` file for the target. This setting only applies to command-line tool targets.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Property List Output Encoding - `PLIST_FILE_OUTPUT_FORMAT` (Enumeration)
Specifies the output encoding for property list files (`.plist`). The output encodings can be `binary` or `XML`. By default, the output encoding will be unchanged from the input.

| Enumeration value |
| -------- |
| **`same-as-input`** |
| `XML` |
| `binary` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Strings File Output Encoding - `STRINGS_FILE_OUTPUT_ENCODING` (Enumeration)
Specify the encoding to be used for Strings files (by default, the output encoding will be 16-bit Unicode). The value can be either an `NSStringEncoding`, such as one of the numeric values recognized by `NSString`, or it can be an IANA character set name as understood by `CFString`. The operation will fail if the file cannot be converted to the specified encoding.

| Enumeration value |
| -------- |
| **`UTF-16`** |
| `UTF-8` |
| `binary` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Convert Copied Files - `APPLY_RULES_IN_COPY_FILES` (bool)
Files copied with a Copy Files build phase are unchanged by default. Setting this to `TRUE` causes property list files (`.plist`) and strings files to be converted as specified by `PLIST_FILE_OUTPUT_FORMAT` and `STRINGS_FILE_OUTPUT_ENCODING`.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `REMOVE_HEADERS_FROM_EMBEDDED_BUNDLES` (bool)
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Info.plist Preprocessor Prefix File - `INFOPLIST_PREFIX_HEADER` (string)
Implicitly include the given file when preprocessing the `Info.plist` file. The path given should either be a project relative path or an absolute path.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Info.plist Other Preprocessor Flags - `INFOPLIST_OTHER_PREPROCESSOR_FLAGS` (StringList)
Other flags to pass to the C preprocessor when preprocessing the `Info.plist` file.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Info.plist Preprocessor Definitions - `INFOPLIST_PREPROCESSOR_DEFINITIONS` (stringlist)
Space-separated list of preprocessor macros of the form `foo` or `foo=bar`. These macros are used when preprocessing the `Info.plist` file.
Default value: **""**

| Command Line Argument |
| -------- |
| `-D$(value)` |


### Preserve HFS Data - `COPYING_PRESERVES_HFS_DATA` (bool)
Causes the copying of resources to preserve resource forks and Finder info.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Deployment Location - `DEPLOYMENT_LOCATION` (bool)
If enabled, built products are placed in their installed locations in addition to the built products folder.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Deployment Postprocessing - `DEPLOYMENT_POSTPROCESSING` (bool)
If enabled, indicates that binaries should be stripped and file mode, owner, and group information should be set to standard values.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Installation Directory - `INSTALL_PATH` (string)
The directory in which to install the build products. This path is prepended by the `DSTROOT`.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `SYSTEM_KEXT_INSTALL_PATH` (string)
Default value: **`$(SYSTEM_LIBRARY_DIR)/Extensions`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `LIBRARY_KEXT_INSTALL_PATH` (string)
Default value: **`$(LOCAL_LIBRARY_DIR)/Extensions`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `DEFAULT_KEXT_INSTALL_PATH` (string)
Default value: **`$(SYSTEM_KEXT_INSTALL_PATH)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Skip Install - `SKIP_INSTALL` (bool)
If enabled, don't install built products even if deployment locations are active.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `SEPARATE_STRIP` (bool)
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Strip Style - `STRIP_STYLE` (enum)
The level of symbol stripping to be performed on the linked product of the build. The default value is defined by the target's product type.

* *All Symbols:* Completely strips the binary, removing the symbol table and relocation information. [all, -s]
* *Non-Global Symbols:* Strips non-global symbols, but saves external symbols. [non-global, -x]
* *Debugging Symbols:* Strips debugging symbols, but saves local and global symbols. [debugging, -S]

| enum value | Command Line Argument |
| ----- | -------- |
| **`all`** |  |
| `debugging` | `-S` |
| `non-global` | `-x` |



### Additional Strip Flags - `STRIPFLAGS` (stringlist)
Additional flags to be passed when stripping the linked product of the build.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Alternate Permissions Files - `ALTERNATE_PERMISSIONS_FILES` (stringlist)
List of files to which the alternate owner, group and permissions are applied.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Alternate Install Owner - `ALTERNATE_OWNER` (string)
The owner name or uid for the files listed under the `ALTERNATE_PERMISSIONS_FILES` setting.
Default value: **`$(INSTALL_OWNER)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Alternate Install Group - `ALTERNATE_GROUP` (string)
The group name or gid for the files listed under the `ALTERNATE_PERMISSIONS_FILES` setting.
Default value: **`$(INSTALL_GROUP)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Alternate Install Permissions - `ALTERNATE_MODE` (string)
Permissions used for the files listed under the `ALTERNATE_PERMISSIONS_FILES` setting.
Default value: **`$(INSTALL_MODE_FLAG)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Test Host - `TEST_HOST` (string)
Path to the executable into which a bundle of tests is injected. Only specify this setting if testing an application or other executable.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Treat missing baselines as test failures - `TREAT_MISSING_BASELINES_AS_TEST_FAILURES` (Boolean)
When running tests that measure performance via `XCTestCase`, report missing baselines as test failures.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `EXCLUDED_SOURCE_FILE_NAMES` (stringlist)
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `INCLUDED_SOURCE_FILE_NAMES` (stringlist)
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Module Identifier - `MODULE_NAME` (string)
This is the identifier of the kernel module listed in the generated stub. This is only used when building kernel extensions.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Module Version - `MODULE_VERSION` (string)
This is the version of the kernel module listed in the generated stub. This is only used when building kernel extensions.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Module Start Routine - `MODULE_START` (string)
This defines the name of the kernel module start routine. This is only used when building kernel extensions.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Module Stop Routine - `MODULE_STOP` (string)
This defines the name of the kernel module stop routine. This is only used when building kernel extensions.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `HOME` (path)

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `LOGNAME` (string)

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `PWD` (path)

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `SHELL` (path)

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `USER` (string)

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `XCODE_DEVELOPER_DIR_PATH` (path)

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `METAL_LIBRARY_FILE_BASE` (string)
Default value: **`default`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `METAL_LIBRARY_OUTPUT_DIR` (string)
Default value: **`$(TARGET_BUILD_DIR)/$(UNLOCALIZED_RESOURCES_FOLDER_PATH)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




## Packaging
### Product Bundle Identifier - `PRODUCT_BUNDLE_IDENTIFIER` (String)
A string that uniquely identifies the bundle. The string should be in reverse DNS format using only alphanumeric characters (`A-Z`, `a-z`, `0-9`), the dot (`.`), and the hyphen (`-`). This value is used as the `CFBundleIdentifier` in the `Info.plist` of the built bundle.

Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




# CoreBuildSystem

Special meanings:
`$(value)` is replaced by the selected value or the default value.

## Architectures
### Architectures - `ARCHS` (StringList)
A list of the architectures for which the product will be built. This is usually set to a predefined build setting provided by the platform. If more than one architecture is specified, a universal binary will be produced.
Default value: **`$(ARCHS_STANDARD)`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Build Active Architecture Only - `ONLY_ACTIVE_ARCH` (Boolean)
If enabled, only the active architecture is built. This setting will be ignored when building with a run destination which does not define a specific architecture, such as a 'Generic Device' run destination.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Valid Architectures - `VALID_ARCHS` (StringList)
A space-separated list of architectures for which the target should actually be built. For each target, this is intersected with the list specified in `ARCHS`, and the resulting set is built. This allows individual targets to opt out of building for particular architectures. If the resulting set of architectures is empty, no executable will be produced.
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Base SDK - `SDKROOT` (Path)
The name or path of the base SDK being used during the build. The product will be built against the headers and libraries located inside the indicated SDK. This path will be prepended to all search paths, and will be passed through the environment to the compiler and linker. Additional SDKs can be specified in the `ADDITIONAL_SDKS` setting.
Default value: **""**
Condition Flavors: `arch`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Additional SDKs - `ADDITIONAL_SDKS` (StringList)
The locations of any sparse SDKs that should be layered on top of the one specified by `SDKROOT`. If more than one SDK is listed, the first one has highest precedence. Every SDK specified in this setting should be a "sparse" SDK, for example, not an SDK for an entire macOS release.
Default value: **""**
Condition Flavors: `arch`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




## Assets
### Enable On Demand Resources - `ENABLE_ON_DEMAND_RESOURCES` (Boolean)
If enabled, tagged assets—files and asset catalog entries—are built into asset packs based on their combination of tags. Untagged resources are treated normally.

Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Embed Asset Packs In Product Bundle - `EMBED_ASSET_PACKS_IN_PRODUCT_BUNDLE` (Boolean)
Embed all the built asset packs inside the product bundle. Since this negates the performance benefits of the On Demand Resources feature, it is only useful for testing purposes when it isn't practical to use an asset pack server.

Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### On Demand Resources Initial Install Tags - `ON_DEMAND_RESOURCES_INITIAL_INSTALL_TAGS` (StringList)
Defined a set of initial On Demand Resources tags to be downloaded and installed with your application.


The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### On Demand Resources Prefetch Order - `ON_DEMAND_RESOURCES_PREFETCH_ORDER` (StringList)
Once your app is installed, this defined a set of On Demand Resources tags that should be downloaded. These tags are downloaded after the initial installation of your application, and will be downloaded in the order the tags provided in the list from first to last.


The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Asset Pack Manifest URL Prefix - `ASSET_PACK_MANIFEST_URL_PREFIX` (String)
If set to anything other than the empty string, every URL in the `AssetPackManifest.plist` file will consist of this string with the name of the asset pack appended. If not set, the URLs in the `AssetPackManifest.plist` will be formed as appropriate for the build location of the asset packs. The prefix string is not escaped or quoted in any way, so any necessary escaping must be part of the URL string. This setting affects only URLs in the `AssetPackManifest.plist` file — it does not affect where asset packs are built in the local file system.

Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




## Build Locations
### Build Products Path - `SYMROOT` (Path)
The path at which all products will be placed when performing a build. Typically this path is not set per target, but is set per-project or per-user. By default, this is set to `$(PROJECT_DIR)/build`.
Default value: **`build`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Intermediate Build Files Path - `OBJROOT` (Path)
The path where intermediate files will be placed during a build. Intermediate files include generated sources, object files, etc. Shell script build phases can place and access files here, as well. Typically this path is not set per target, but is set per project or per user. By default, this is set to `$(PROJECT_DIR)/build`.
Default value: **`$(SYMROOT)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Per-configuration Build Products Path - `CONFIGURATION_BUILD_DIR` (Path)
The base path where build products will be placed during a build for a given configuration. By default, this is set to `$(BUILD_DIR)/$(CONFIGURATION)`.
Default value: **`$(BUILD_DIR)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Per-configuration Intermediate Build Files Path - `CONFIGURATION_TEMP_DIR` (Path)
The base path where intermediates will be placed during a build for a given configuration. By default, this is set to `$(PROJECT_TEMP_DIR)/$(CONFIGURATION)`.
Default value: **`$(PROJECT_TEMP_DIR)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Precompiled Headers Cache Path - `SHARED_PRECOMPS_DIR` (String)
The path where precompiled prefix header files are placed during a build. Defaults to `$(OBJROOT)/SharedPrecompiledHeaders`. Using a common location allows precompiled headers to be shared between multiple projects.
Default value: **`$(OBJROOT)/SharedPrecompiledHeaders`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




## Build Options
### Build Variants - `BUILD_VARIANTS` (StringList)
A list of the build variants of the linked binary that will be produced. By default, only the `normal` variant is produced. Other common values include `debug` and `profile`.
Default value: **`normal`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Debug Information Format - `DEBUG_INFORMATION_FORMAT` (Enumeration)
The type of debug information to produce.

* *DWARF:* Object files and linked products will use DWARF as the debug information format. [dwarf]
* *DWARF with dSYM File:* Object files and linked products will use DWARF as the debug information format, and Xcode will also produce a dSYM file containing the debug information from the individual object files (except that a dSYM file is not needed and will not be created for static library or object file products). [dwarf-with-dsym]
Default value: **""**
Condition Flavors: `sdk`

| Enumeration value |
| -------- |
| `{'Value': 'dwarf'}` |
| `{'Value': 'dwarf-with-dsym'}` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Scan All Source Files for Includes - `SCAN_ALL_SOURCE_FILES_FOR_INCLUDES` (Boolean)
Activating this setting will cause all source files to be scanned for includes (for example, of header files) when computing the dependency graph, in which case if an included file is changed then the including file will be rebuilt next time a target containing it is built. Normally only certain types of files, such as C-language source files, are scanned.

This setting is useful if your project contains files of unusual types, which are compiled using a custom build rule.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Generate Profiling Code - `GENERATE_PROFILING_CODE` (Boolean)
Activating this setting will cause the compiler and linker to generate profiling code. For example, GCC will generate code suitable for use with `gprof(1)`.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Precompiled Header Uses Files From Build Directory - `PRECOMPS_INCLUDE_HEADERS_FROM_BUILT_PRODUCTS_DIR` (Boolean)
This setting allows for better control of sharing precompiled prefix header files between projects. By default, Xcode assumes that the prefix header file may include header files from the build directory if the build directory is outside of the project directory. Xcode cannot determine this ahead of time since other projects may not have been built into the shared build directory at the time the information is needed.

If your prefix file never includes files from the build directory you may set this to `NO` to improve sharing of precompiled headers. If the prefix does use files from a build directory that is inside your project directory, you may set this to `YES` to avoid unintended sharing that may result in build failures.
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Compiler for C/C++/Objective-C - `GCC_VERSION` (CompilerVersion)
The compiler to use for C, C++, and Objective-C.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Excluded Source File Names - `EXCLUDED_SOURCE_FILE_NAMES` (StringList)
A list of patterns (as defined by `fnmatch(3)`) specifying the names of source files to explicitly *exclude* when processing the sources build phase (see also `INCLUDED_SOURCE_FILE_NAMES`). This setting can be used to define complex filters for which files from the phase should be built in response to other build settings; for example, a value of `*.$(CURRENT_ARCH).c` could serve to exclude particular files based on the architecture being built.

Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Included Source File Names - `INCLUDED_SOURCE_FILE_NAMES` (StringList)
A list of patterns (as defined by `fnmatch(3)`) specifying the names of source files to explicitly *include* when processing the sources build phase. This setting is only useful when combined with `EXCLUDED_SOURCE_FILE_NAMES`, and can be used to define complex filters for which files from the phase should be built in response to other build settings.

Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Enable Index-While-Building Functionality - `COMPILER_INDEX_STORE_ENABLE` (Enumeration)
Control whether the compiler should emit index data while building.


| Enumeration value |
| -------- |
| **`Default`** |
| `YES` |
| `NO` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Require Only App-Extension-Safe API - `APPLICATION_EXTENSION_API_ONLY` (bool)
When enabled, this causes the compiler and linker to disallow use of APIs that are not available to app extensions and to disallow linking to frameworks that have not been built with this setting enabled.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Enable Testability - `ENABLE_TESTABILITY` (Boolean)
When this setting is activated, the product will be built with options appropriate for running automated tests, such as making private interfaces accessible to the tests. This may result in tests running slower than they would without testability enabled.

Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




## Signing
### Code Signing Identity - `CODE_SIGN_IDENTITY` (CodeSignIdentity)
The name, also known as the *common name*, of a valid code-signing certificate in a keychain within your keychain path. A missing or invalid certificate will cause a build error.
Default value: **""**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Code Signing Style - `CODE_SIGN_STYLE` (CodeSignStyle)
This setting specifies the method used to acquire and locate signing assets. Choose `Automatic` to let Xcode automatically create and update profiles, app IDs, and certificates. Choose `Manual` to create and update these yourself on the developer website.
Condition Flavors: `sdk`

| CodeSignStyle value |
| -------- |
| **``** |
| `Automatic` |
| `Manual` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Development Team - `DEVELOPMENT_TEAM` (DevelopmentTeam)
The team ID of a development team to use for signing certificates and provisioning profiles.
Default value: **""**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Provisioning Profile - `PROVISIONING_PROFILE_SPECIFIER` (ProvisioningProfileSpecifier)
Must contain a profile name (or UUID). A missing or invalid profile will cause a build error. Use in conjunction with [DEVELOPMENT_TEAM] to fully specify provisioning profile.
Default value: **""**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Other Code Signing Flags - `OTHER_CODE_SIGN_FLAGS` (StringList)
A list of additional options to pass to `codesign(1)`.
Default value: **""**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Code Signing Entitlements - `CODE_SIGN_ENTITLEMENTS` (String)
The path to a file specifying code-signing entitlements.
Default value: **""**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Code Signing Inject Base Entitlements - `CODE_SIGN_INJECT_BASE_ENTITLEMENTS` (Boolean)
Automatically inject entitlements from the platform's BaseEntitlements.plist into the code signatures of executables.
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




## Deployment
### Deployment Location - `DEPLOYMENT_LOCATION` (Boolean)
If enabled, built products are placed in their installed locations in addition to the built products folder.
Default value: **`NO`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Deployment Postprocessing - `DEPLOYMENT_POSTPROCESSING` (Boolean)
If enabled, indicates that binaries should be stripped and file mode, owner, and group information should be set to standard values.
Default value: **`NO`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Installation Build Products Location - `DSTROOT` (Path)
The path at which all products will be rooted when performing an install build. For instance, to install your products on the system proper, set this path to `/`. Defaults to `/tmp/$(PROJECT_NAME).dst` to prevent a *test* install build from accidentally overwriting valid and needed data in the ultimate install path.

Typically this path is not set per target, but is provided as an option on the command line when performing an `xcodebuild install`. It may also be set in a build configuration in special circumstances.
Default value: **`/tmp/$(PROJECT_NAME).dst`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Installation Directory - `INSTALL_PATH` (String)
The directory in which to install the build products. This path is prepended by the `DSTROOT`.
Default value: **""**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Skip Install - `SKIP_INSTALL` (Boolean)
If enabled, don't install built products even if deployment locations are active.
Default value: **`NO`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Strip Linked Product - `STRIP_INSTALLED_PRODUCT` (Boolean)
If enabled,  the linked product of the build will be stripped of symbols when performing deployment postprocessing.
Default value: **`YES`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Strip Style - `STRIP_STYLE` (Enumeration)
The level of symbol stripping to be performed on the linked product of the build. The default value is defined by the target's product type.

* *All Symbols:* Completely strips the binary, removing the symbol table and relocation information. [all, -s]
* *Non-Global Symbols:* Strips non-global symbols, but saves external symbols. [non-global, -x]
* *Debugging Symbols:* Strips debugging symbols, but saves local and global symbols. [debugging, -S]
Default value: **`all`**
Condition Flavors: `sdk`

| Enumeration value |
| -------- |
| `{'Value': 'all'}` |
| `{'Value': 'non-global'}` |
| `{'Value': 'debugging'}` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Additional Strip Flags - `STRIPFLAGS` (StringList)
Additional flags to be passed when stripping the linked product of the build.
Default value: **""**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Strip Swift Symbols - `STRIP_SWIFT_SYMBOLS` (Boolean)
Adjust the level of symbol stripping specified by the STRIP_STYLE setting so that when the linked product of the build is stripped, all Swift symbols will be removed.
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Strip Debug Symbols During Copy - `COPY_PHASE_STRIP` (Boolean)
Specifies whether binary files that are copied during the build, such as in a Copy Bundle Resources or Copy Files build phase, should be stripped of debugging symbols. It does not cause the linked product of a target to be stripped—use `STRIP_INSTALLED_PRODUCT` for that.
Default value: **`YES`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Install Owner - `INSTALL_OWNER` (String)
The owner name or `uid` for installed products.
Default value: **`$(USER)`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Install Group - `INSTALL_GROUP` (String)
The group name or `gid` for installed products.
Default value: **`$(GROUP)`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Install Permissions - `INSTALL_MODE_FLAG` (String)
Permissions used for installed product files.
Default value: **`u+w,go-w,a+rX`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Alternate Permissions Files - `ALTERNATE_PERMISSIONS_FILES` (StringList)
List of files to which the alternate owner, group and permissions are applied.
Default value: **""**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Alternate Install Owner - `ALTERNATE_OWNER` (String)
The owner name or uid for the files listed under the `ALTERNATE_PERMISSIONS_FILES` setting.
Default value: **`$(INSTALL_OWNER)`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Alternate Install Group - `ALTERNATE_GROUP` (String)
The group name or gid for the files listed under the `ALTERNATE_PERMISSIONS_FILES` setting.
Default value: **`$(INSTALL_GROUP)`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Alternate Install Permissions - `ALTERNATE_MODE` (String)
Permissions used for the files listed under the `ALTERNATE_PERMISSIONS_FILES` setting.
Default value: **`$(INSTALL_MODE_FLAG)`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Resources Targeted Device Family - `RESOURCES_TARGETED_DEVICE_FAMILY` (StringList)
Overrides `TARGETED_DEVICE_FAMILY` when the resource copying needs to differ from the default targeted device.

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




## Headers
### Run unifdef on Product Headers - `COPY_HEADERS_RUN_UNIFDEF` (Boolean)
If enabled, headers are run through the `unifdef(1)` tool when copied to the product.

Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Unifdef Flags for Product Headers - `COPY_HEADERS_UNIFDEF_FLAGS` (StringList)
Specifies the flags to pass to `unifdef(1)` when invoking that tool to copy headers. This setting has no effect unless `COPY_HEADERS_RUN_UNIFDEF` is enabled.

Default value: **""**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




## Kernel Module
### Module Identifier - `MODULE_NAME` (String)
This is the identifier of the kernel module listed in the generated stub. This is only used when building kernel extensions.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Module Version - `MODULE_VERSION` (String)
This is the version of the kernel module listed in the generated stub. This is only used when building kernel extensions.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Module Start Routine - `MODULE_START` (String)
This defines the name of the kernel module start routine. This is only used when building kernel extensions.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Module Stop Routine - `MODULE_STOP` (String)
This defines the name of the kernel module stop routine. This is only used when building kernel extensions.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




## Linking
### Mach-O Type - `MACH_O_TYPE` (Enumeration)
This setting determines the format of the produced binary and how it can be linked when building other binaries. For information on binary types, see [Building Mach-O Files](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/MachOTopics/1-Articles/building_files.html#//apple_ref/doc/uid/TP40001828-SW1) in [Mach-O Programming Topics](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/MachOTopics/0-Introduction/introduction.html).

* *Executable:* Executables and standalone binaries and cannot be linked. [mh_execute]
* *Dynamic Library:* Dynamic libraries are linked at build time and loaded automatically when needed. [mh_dylib]
* *Bundle:* Bundle libraries are loaded explicitly at run time. [mh_bundle]
* *Static Library:* Static libraries are linked at build time and loaded at execution time. [staticlib]
* *Relocatable Object File:* Object files are single-module files that are linked at build time. [mh_object]
Default value: **""**
Condition Flavors: `arch, sdk`

| Enumeration value |
| -------- |
| `{'Value': 'mh_execute'}` |
| `{'Value': 'mh_dylib'}` |
| `{'Value': 'mh_bundle'}` |
| `{'Value': 'staticlib'}` |
| `{'Value': 'mh_object'}` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Initialization Routine - `INIT_ROUTINE` (String)
This is the name of the routine to use for initialization.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Link With Standard Libraries - `LINK_WITH_STANDARD_LIBRARIES` (Boolean)
When this setting is enabled, the compiler driver will automatically pass its standard libraries to the linker to use during linking. If desired, this flag can be used to disable linking with the standard libraries, and then individual libraries can be passed as `OTHER_LDFLAGS`.
Default value: **`YES`**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Preserve Private External Symbols - `KEEP_PRIVATE_EXTERNS` (Boolean)
Activating this setting will preserve private external symbols, rather than turning them into static symbols. This setting is also respected when performing a single-object prelink.
Default value: **`NO`**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Exported Symbols File - `EXPORTED_SYMBOLS_FILE` (String)
This is a project-relative path to a file that lists the symbols to export. See `ld -exported_symbols_list` for details on exporting symbols.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Unexported Symbols File - `UNEXPORTED_SYMBOLS_FILE` (String)
A project-relative path to a file that lists the symbols not to export. See `ld -exported_symbols_list` for details on exporting symbols.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Separately Edit Symbols - `SEPARATE_SYMBOL_EDIT` (Boolean)
Activating this setting when the linked product's symbols are to be edited will cause editing to occur via a separate invocation of `nmedit(1)`. Otherwise editing will occur during linking, if possible.
Default value: **`NO`**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Re-Exported Library Names - `REEXPORTED_LIBRARY_NAMES` (StringList)
List of library names that should have their symbols be reexported from the built library.

Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Re-Exported Library Paths - `REEXPORTED_LIBRARY_PATHS` (PathList)
List of library paths that should have their symbols be reexported from the built library.

Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Re-Exported Framework Names - `REEXPORTED_FRAMEWORK_NAMES` (StringList)
List of framework names that should have their symbols be reexported from the built library.

Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Bundle Loader - `BUNDLE_LOADER` (String)
Specifies the executable that will load the bundle output file being linked. Undefined symbols from the bundle are checked against the specified executable as if it is one of the dynamic libraries the bundle was linked with.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Current Library Version - `DYLIB_CURRENT_VERSION` (String)
This setting defines the current version of any framework built by the project. As with `CURRENT_PROJECT_VERSION`, the value must be an integer or floating point number, such as `57` or `365.8`. By default, it is set to `$(CURRENT_PROJECT_VERSION)`. See [Dynamic Library Design Guidelines](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/DynamicLibraryDesignGuidelines.html#//apple_ref/doc/uid/TP40002013-SW19) in [Dynamic Library Programming Topics](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/DynamicLibraries/000-Introduction/Introduction.html) for details on assigning version numbers of dynamic libraries.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Compatibility Version - `DYLIB_COMPATIBILITY_VERSION` (String)
Determines the compatibility version of the resulting library, bundle, or framework binary. See [Dynamic Library Design Guidelines](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/DynamicLibraryDesignGuidelines.html#//apple_ref/doc/uid/TP40002013-SW19) in [Dynamic Library Programming Topics](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/DynamicLibraries/000-Introduction/Introduction.html) for details on assigning version numbers of dynamic libraries.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Dynamic Library Install Name - `LD_DYLIB_INSTALL_NAME` (Path)
Sets an internal `install path` (`LC_ID_DYLIB`) in a dynamic library. Any clients linked against the library will record that path as the way `dyld` should locate this library. If this option is not specified, then the `-o` path will be used. This setting is ignored when building any product other than a dynamic library. See [Dynamic Library Programming Topics](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/DynamicLibraries/000-Introduction/Introduction.html).
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Dynamic Library Install Name Base - `DYLIB_INSTALL_NAME_BASE` (String)
Sets the base value for the internal `install path` (`LC_ID_DYLIB`) in a dynamic library. This will be combined with the `EXECUTABLE_PATH` to form the full install path. Setting `LD_DYLIB_INSTALL_NAME` directly will override this setting. This setting defaults to the target's `INSTALL_PATH`. It is ignored when building any product other than a dynamic library.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Symbol Ordering Flags - `SECTORDER_FLAGS` (StringList)
These flags are typically used to specify options for ordering symbols within segments, for example the `-sectorder` option to `ld`.

Generally you should not specify symbol ordering options in Debug or Development configurations, as this will make the linked binary less readable to the debugger. Use them only in Release or Deployment configurations.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Order File - `ORDER_FILE` (String)
The path to a file that alters the order in which functions and data are laid out.

For each section in the output file, any symbol in that section that are specified in the order file is moved to the start of its section and laid out in the same order as in the order file. Order files are text files with one symbol name per line. Lines starting with a `#` are comments. A symbol name may be optionally preceded with its object file leafname and a colon (for example, `foo.o:_foo`). This is useful for static functions/data that occur in multiple files. A symbol name may also be optionally preceded with the architecture (for example, `ppc:_foo` or `ppc:foo.o:_foo`). This enables you to have one order file that works for multiple architectures. Literal C-strings may be ordered by quoting the string in the order file (for example, `"Hello, world\n"`).

Generally you should not specify an order file in Debug or Development configurations, as this will make the linked binary less readable to the debugger. Use them only in Release or Deployment configurations.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Runpath Search Paths - `LD_RUNPATH_SEARCH_PATHS` (StringList)
This is a list of paths to be added to the `runpath` search path list for the image being created. At runtime, `dyld` uses the `runpath` when searching for dylibs whose load path begins with `@rpath/`. See [Dynamic Library Programming Topics](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/DynamicLibraries/000-Introduction/Introduction.html).
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Write Link Map File - `LD_GENERATE_MAP_FILE` (Boolean)
Activating this setting will cause the linker to write a map file to disk, which details all symbols and their addresses in the output image. The path to the map file is defined by the `LD_MAP_FILE_PATH` setting.
Default value: **`NO`**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Path to Link Map File - `LD_MAP_FILE_PATH` (Path)
This setting defines the path to the map file written by the linker when the `LD_GENERATE_MAP_FILE` setting is activated. By default, a separate file will be written for each architecture and build variant, and these will be generated in the Intermediates directory for the target whose product is being linked.
Default value: **`$(TARGET_TEMP_DIR)/$(PRODUCT_NAME)-LinkMap-$(CURRENT_VARIANT)-$(CURRENT_ARCH).txt`**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Dead Code Stripping - `DEAD_CODE_STRIPPING` (Boolean)
Activating this setting causes the `-dead_strip` flag to be passed to `ld(1)` via `cc(1)` to turn on dead code stripping.
Default value: **`NO`**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Don't Dead-Strip Inits and Terms - `PRESERVE_DEAD_CODE_INITS_AND_TERMS` (Boolean)
Activating this setting, in combination with the `DEAD_CODE_STRIPPING` (`-dead_strip`) option, causes the `-no_dead_strip_inits_and_terms` flag to be passed to `ld(1)` via `cc(1)` to disable dead code stripping for initialization and termination routines. This option should not be used without the aforementioned `DEAD_CODE_STRIPPING` option.
Default value: **`NO`**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Display Mangled Names - `LINKER_DISPLAYS_MANGLED_NAMES` (Boolean)
Activating this setting causes the linker to display mangled names for C++ symbols. Normally, this is not recommended, but turning it on can help to diagnose and solve C++ link errors.
Default value: **`NO`**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Warning Linker Flags - `WARNING_LDFLAGS` (StringList)
These flags are passed with linker invocations, and by default give the `-no_arch_warnings` flag to the linker to avoid many warnings being generated during multi-architecture builds.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Other Linker Flags - `OTHER_LDFLAGS` (StringList)
Options defined in this setting are passed to invocations of the linker.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Perform Single-Object Prelink - `GENERATE_MASTER_OBJECT_FILE` (Boolean)
Activating this setting will cause the object files built by a target to be prelinked using `ld -r` into a single object file, and that object file will then be linked into the final product. This is useful to force the linker to resolve symbols and link the object files into a single module before building a static library. Also, a separate set of link flags can be applied to the prelink allowing additional control over, for instance, exported symbols.
Default value: **`NO`**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Prelink libraries - `PRELINK_LIBS` (StringList)
Additional libraries to pass when performing a single-object prelink.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Single-Object Prelink Flags - `PRELINK_FLAGS` (StringList)
Additional flags to pass when performing a single-object prelink.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Generate Position-Dependent Executable - `LD_NO_PIE` (bool)
Activating this setting will prevent Xcode from building a main executable that is position independent (PIE). When targeting macOS 10.7 or later, PIE is the default for main executables, so activating this setting will change that behavior. When targeting OS X 10.6 or earlier, or when building for i386, PIE is not the default, so activating this setting does nothing.

You cannot create a PIE from `.o` files compiled with `-mdynamic-no-pic`. Using PIE means the codegen is less optimal, but the address randomization adds some security.
Condition Flavors: `arch, sdk`

| bool value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Xlinker -no_pie` |



### Quote Linker Arguments - `LD_QUOTE_LINKER_ARGUMENTS_FOR_COMPILER_DRIVER` (Boolean)
This setting controls whether arguments to the linker should be quoted using `-Xlinker`. By default, Xcode invokes the linker by invoking the driver of the compiler used to build the source files in the target, and passing `-Xlinker` to quote arguments will cause the compiler driver to pass them through to the linker (rather than trying to evaluate them within the driver). By default, this setting is enabled. Disabling it will cause Xcode to not use `-Xlinker` to pass arguments to the linker. Disabling this setting is useful if the target has instructed Xcode to use an alternate linker (for example, by setting the `LD` setting to the path to another linker) and that alternate linker does not recognize `-Xlinker`.
Default value: **`YES`**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Dynamic Library Allowable Clients - `LD_DYLIB_ALLOWABLE_CLIENTS` (StringList)
This setting restricts the clients allowed to link a dylib by passing `-allowable_client` to the linker for each supplied value.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




## Localization
### Localized String Macro Names - `LOCALIZED_STRING_MACRO_NAMES` (StringList)
The base names for NSLocalizedString-like macros or functions used to produce localized strings in source code. The default base names of NSLocalizedString and CFLocalizedString are always considered, even if this setting is empty.

Default value: **`NSLocalizedString CFLocalizedString`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




## None
### `ARCHS_STANDARD_32_64_BIT` (StringList)

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `ARCHS_STANDARD_32_BIT` (StringList)

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `ARCHS_STANDARD_64_BIT` (StringList)

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `LOCROOT` (Path)
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `LOCSYMROOT` (Path)
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `MODULE_CACHE_DIR` (Path)
Absolute path of folder in which compiler stores its cached modules—this cache is a performance improvement.

Default value: **`$(DERIVED_DATA_DIR)/ModuleCache.noindex`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `ENABLE_BITCODE` (Boolean)
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `BITCODE_GENERATION_MODE` (Enumeration)
Default value: **`marker`**

| Enumeration value |
| -------- |
| `{'Value': 'marker'}` |
| `{'Value': 'bitcode'}` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `HIDE_BITCODE_SYMBOLS` (Boolean)
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `STRIP_BITCODE_FROM_COPIED_FILES` (Boolean)
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `REEXPORTED_LIBRARY_INSTALL_NAMES` (PathList)

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `REEXPORTED_FRAMEWORK_INSTALL_NAMES` (StringList)

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Path to Linker Dependency Info File - `LD_DEPENDENCY_INFO_FILE` (Path)
This setting defines the path to which the linker should emit information about what files it used as inputs and generated. Xcode uses this information for its dependency tracking. Setting the value of this setting to empty will disable passing this option to the linker.
Default value: **`$(OBJECT_FILE_DIR_$(CURRENT_VARIANT))/$(CURRENT_ARCH)/$(PRODUCT_NAME)_dependency_info.dat`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `LIBRARY_FLAG_NOSPACE` (bool)
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `LIBRARY_FLAG_PREFIX` (String)
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CODE_SIGNING_ALLOWED` (bool)
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `ENTITLEMENTS_DESTINATION` (Enumeration)

| Enumeration value |
| -------- |
| **``** |
| `Signature` |
| `__entitlements` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `EMBEDDED_PROFILE_NAME` (String)
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `FULL_PRODUCT_NAME` (String)
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `REMOVE_HEADERS_FROM_EMBEDDED_BUNDLES` (Boolean)
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `SEPARATE_STRIP` (Boolean)
Default value: **`NO`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `BUILD_STYLE` (String)
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CONFIGURATION` (String)
Identifies the build configuration, such as `Debug` or `Release`, that the target uses to generate the product.

Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `SRCROOT` (Path)
Identifies the directory containing the target’s source files.

Default value: **`.`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `SOURCE_ROOT` (Path)
Default value: **`$(SRCROOT)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `TEMP_ROOT` (Path)
Default value: **`$(OBJROOT)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `BUILD_ROOT` (Path)
Default value: **`$(SYMROOT)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `INSTALL_ROOT` (Path)
Default value: **`$(DSTROOT)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `PROJECT_DIR` (Path)
Default value: **`$(SRCROOT)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `BUILD_DIR` (Path)
Default value: **`$(SYMROOT)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `PROJECT_TEMP_ROOT` (Path)
Default value: **`$(OBJROOT)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `PROJECT_TEMP_DIR` (Path)
Identifies the directory in which the project’s intermediate build files are placed. This directory is shared between all the targets defined by the project. Run Script build phases should generate intermediate build files in the directory identified by `DERIVED_FILE_DIR`, not the location this build setting specifies.

Default value: **`$(PROJECT_TEMP_ROOT)/$(PROJECT_NAME).build`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `TARGET_TEMP_DIR` (Path)
Identifies the directory containing the target’s intermediate build files. Run Script build phases should place intermediate files at the location indicated by `DERIVED_FILE_DIR`, not the directory identified by this build setting.

Default value: **`$(CONFIGURATION_TEMP_DIR)/$(TARGET_NAME).build`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `TEMP_DIR` (Path)
Default value: **`$(TARGET_TEMP_DIR)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `OBJECT_FILE_DIR` (Path)
Partially identifies the directory into which variant object files are placed. The complete specification is computed using the variants of this build setting.

Default value: **`$(TEMP_DIR)/Objects`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CLASS_FILE_DIR` (Path)
Default value: **`$(TEMP_DIR)/JavaClasses`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `FILE_LIST` (Path)
Default value: **`$(OBJECT_FILE_DIR)/LinkFileList`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `DERIVED_FILE_DIR` (Path)
Identifies the directory into which derived source files, such as those generated by `lex` and `yacc`, are placed.

Default value: **`$(TEMP_DIR)/DerivedSources`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `LOCALIZABLE_CONTENT_DIR` (Path)
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `INSTALL_DIR` (Path)
Identifies the directory in the developer’s filesystem into which the *installed* product is placed.

Default value: **`$(DSTROOT)$(INSTALL_PATH)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `PROJECT_DERIVED_FILE_DIR` (Path)
Default value: **`$(OBJROOT)/$(PROJECT_NAME).build/DerivedSources`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `SHARED_DERIVED_FILE_DIR` (Path)
Default value: **`$(BUILT_PRODUCTS_DIR)/DerivedSources`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `TARGET_BUILD_DIR` (Path)
Identifies the root of the directory hierarchy that contains the product’s files (no intermediate build files). Run Script build phases that operate on product files of the target that defines them should use the value of this build setting, but Run Script build phases that operate on product files of other targets should use `BUILT_PRODUCTS_DIR` instead.

Default value: **`$(CONFIGURATION_BUILD_DIR)$(TARGET_BUILD_SUBPATH)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `TARGET_BUILD_SUBPATH` (Path)
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `BUILT_PRODUCTS_DIR` (Path)
Identifies the directory under which all the product’s files can be found. This directory contains either product files or symbolic links to them. Run Script build phases can use the value of this build setting as a convenient way to refer to the product files built by one or more targets even when these files are scattered throughout a directory hierarchy (for example, when `DEPLOYMENT_LOCATION` is set to `YES`.

Default value: **`$(CONFIGURATION_BUILD_DIR)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `ENABLE_HEADER_DEPENDENCIES` (Boolean)
Specifies whether to automatically track dependencies on included header files.

Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `PATH_PREFIXES_EXCLUDED_FROM_HEADER_DEPENDENCIES` (PathList)
Default value: **`/usr/include /usr/local/include /System/Library/Frameworks /System/Library/PrivateFrameworks $(SYSTEM_DEVELOPER_DIR)/Headers $(SYSTEM_DEVELOPER_DIR)/SDKs $(SYSTEM_DEVELOPER_DIR)/Platforms`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `DO_HEADER_SCANNING_IN_JAM` (Boolean)
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `TEMP_FILE_DIR` (Path)
Default value: **`$(TEMP_DIR)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `TEMP_FILES_DIR` (Path)
Default value: **`$(TEMP_FILE_DIR)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `DERIVED_SOURCES_DIR` (Path)
Default value: **`$(DERIVED_FILE_DIR)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `NATIVE_ARCH` (String)
Identifies the architecture on which the build is being performed.


The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `NATIVE_ARCH_32_BIT` (String)

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `NATIVE_ARCH_64_BIT` (String)

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `NATIVE_ARCH_ACTUAL` (String)

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `REMOVE_CVS_FROM_RESOURCES` (Boolean)
Specifies whether to remove `CVS` directories from bundle resources when they are copied.

Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `REMOVE_SVN_FROM_RESOURCES` (Boolean)
Specifies whether to remove `SVN` directories from bundle resources when they are copied.

Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `REMOVE_GIT_FROM_RESOURCES` (Boolean)
Specifies whether to remove `.git` directories from bundle resources when they are copied.

Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `REMOVE_HG_FROM_RESOURCES` (Boolean)
Specifies whether to remove `.hg` directories from bundle resources when they are copied.

Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `DEBUGGING_SYMBOLS` (Boolean)
Default value: **`YES`**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `PROFILING_CODE` (Boolean)
Default value: **`NO`**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `OTHER_CFLAGS` (StringList)
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `OTHER_CPLUSPLUSFLAGS` (StringList)
Default value: **`$(OTHER_CFLAGS)`**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `KEXT_CFLAGS` (StringList)
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `KEXT_CPLUSPLUSFLAGS` (StringList)
Default value: **`$(KEXT_CFLAGS)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CC` (Path)
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `JAVA_COMPILER` (Path)
Default value: **`/usr/bin/javac`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `JAVA_ARCHIVE_CLASSES` (Boolean)
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `JAVA_ARCHIVE_TYPE` (String)
Default value: **`JAR`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `JAVA_APP_STUB` (Path)
Default value: **`$(SYSTEM_LIBRARY_DIR)/Frameworks/JavaVM.framework/Resources/MacOS/JavaApplicationStub`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `JAVA_JAR_FLAGS` (StringList)
Default value: **`cv`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `JAVA_SOURCE_SUBDIR` (Path)
Default value: **`.`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `JAVA_FRAMEWORK_RESOURCES_DIRS` (PathList)
Default value: **`Resources`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `JAVA_FRAMEWORK_JARS` (PathList)
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `JAVA_USE_DEPENDENCIES` (Boolean)
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `JAVA_ZIP_FLAGS` (StringList)
Default value: **`-urg`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CLONE_HEADERS` (Boolean)
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `GCC3_VERSION` (String)
Default value: **`3.3`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `DEFAULT_COMPILER` (String)
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `MAC_OS_X_VERSION_MAX_ALLOWED` (String)
Condition Flavors: `arch`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `MAC_OS_X_VERSION_MIN_REQUIRED` (String)
Condition Flavors: `arch`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `USE_HEADER_SYMLINKS` (Boolean)
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `HEADERMAP_INCLUDES_NONPUBLIC_NONPRIVATE_HEADERS` (Boolean)
Default value: **`$(HEADERMAP_INCLUDES_PROJECT_HEADERS)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `HEADERMAP_INCLUDES_FRAMEWORK_ENTRIES_FOR_ALL_PRODUCT_TYPES` (Boolean)
Specifies whether the header map contains a framework-name/path entry for every header in the target being built, including targets that do not build frameworks.

Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `HEADERMAP_INCLUDES_FLAT_ENTRIES_FOR_TARGET_BEING_BUILT` (Boolean)
Specifies whether the header map contains a name/path entry for every header in the target being built.

Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `HEADERMAP_INCLUDES_PROJECT_HEADERS` (Boolean)
Specifies whether the header map contains a name/path entry for every header in the project, regardless of the headers’ target membership.

Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `HEADERMAP_USES_FRAMEWORK_PREFIX_ENTRIES` (Boolean)
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `HEADERMAP_USES_VFS` (Boolean)
Default value: **`$(DEFINES_MODULE)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `DWARF_DSYM_FOLDER_PATH` (String)
Default value: **`$(CONFIGURATION_BUILD_DIR)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `DWARF_DSYM_FILE_NAME` (String)
Default value: **`$(FULL_PRODUCT_NAME).dSYM`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `DWARF_DSYM_FILE_SHOULD_ACCOMPANY_PRODUCT` (bool)
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `PRECOMP_DESTINATION_DIR` (String)
Default value: **`$(TEMP_DIR)/PrefixHeaders`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `TOOLCHAINS` (StringList)
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `REZ_EXECUTABLE` (String)
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Perform Copy Files Phases During `installhdrs` - `INSTALLHDRS_COPY_PHASE` (Boolean)
Specifies whether the target’s Copy Files build phases are executed in `installhdr` builds.

Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Perform Shell Script Phases During `installhdrs` - `INSTALLHDRS_SCRIPT_PHASE` (Boolean)
Specifies whether the target’s Run Script build phases are executed in `installhdr` builds. See `ACTION` for details on `installhdr` builds.

Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `BUILD_ACTIVE_RESOURCES_ONLY` (Boolean)
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `WRAP_ASSET_PACKS_IN_SEPARATE_DIRECTORIES` (Boolean)
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




## Packaging
### Product Name - `PRODUCT_NAME` (String)
This is the basename of the product generated by the target.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Product Module Name - `PRODUCT_MODULE_NAME` (String)
The name to use for the source code module constructed for this target, and which will be used to import the module in implementation source files. Must be a valid identifier.
Default value: **`$(PRODUCT_NAME:c99extidentifier)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Executable Prefix - `EXECUTABLE_PREFIX` (String)
The prefix used for the executable product generated by the target, which has a default value based on the product type.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Executable Extension - `EXECUTABLE_EXTENSION` (String)
This is the extension used for the executable product generated by the target, which has a default value based on the product type.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Wrapper Extension - `WRAPPER_EXTENSION` (String)
The extension used for product wrappers, which has a default value based on the product type.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Private Headers Folder Path - `PRIVATE_HEADERS_FOLDER_PATH` (String)
The location to copy the private headers to during building, relative to the built products folder.
Default value: **""**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Public Headers Folder Path - `PUBLIC_HEADERS_FOLDER_PATH` (String)
The location to copy the public headers to during building, relative to the built products folder.
Default value: **""**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Force Package Info Generation - `GENERATE_PKGINFO_FILE` (Boolean)
Forces the `PkgInfo` file to be written to wrapped products even if this file is not expected.
Default value: **`NO`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Info.plist File - `INFOPLIST_FILE` (String)
The project-relative path to the property list file that contains the `Info.plist` information used by bundles. For details on information property list files, see [Information Property List Files](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPRuntimeConfig/Articles/ConfigFiles.html#//apple_ref/doc/uid/20002091-CJBJIEDH) in [Runtime Configuration Guidelines](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPRuntimeConfig/000-Introduction/introduction.html).
Default value: **""**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Preprocess Info.plist File - `INFOPLIST_PREPROCESS` (Boolean)
Preprocess the `Info.plist` file using the C Preprocessor.
Default value: **`NO`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Expand Build Settings in Info.plist File - `INFOPLIST_EXPAND_BUILD_SETTINGS` (Boolean)
Expand build settings in the `Info.plist` file.
Default value: **`YES`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Info.plist Output Encoding - `INFOPLIST_OUTPUT_FORMAT` (Enumeration)
Specifies the output encoding for the output `Info.plist`. The output encodings can be `binary` or `XML`. By default, the output encoding will be unchanged from the input.
Condition Flavors: `sdk`

| Enumeration value |
| -------- |
| **`same-as-input`** |
| `XML` |
| `binary` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Create Info.plist Section in Binary - `CREATE_INFOPLIST_SECTION_IN_BINARY` (Boolean)
Enabling this setting will create a section in the product's linked binary containing the processed `Info.plist` file for the target. This setting only applies to command-line tool targets.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Property List Output Encoding - `PLIST_FILE_OUTPUT_FORMAT` (Enumeration)
Specifies the output encoding for property list files (`.plist`). The output encodings can be `binary` or `XML`. By default, the output encoding will be unchanged from the input.
Condition Flavors: `sdk`

| Enumeration value |
| -------- |
| **`same-as-input`** |
| `XML` |
| `binary` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Strings File Output Encoding - `STRINGS_FILE_OUTPUT_ENCODING` (Enumeration)
Specify the encoding to be used for Strings files (by default, the output encoding will be 16-bit Unicode). The value can be either an `NSStringEncoding`, such as one of the numeric values recognized by `NSString`, or it can be an IANA character set name as understood by `CFString`. The operation will fail if the file cannot be converted to the specified encoding.
Condition Flavors: `sdk`

| Enumeration value |
| -------- |
| **`UTF-16`** |
| `UTF-8` |
| `binary` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Convert Copied Files - `APPLY_RULES_IN_COPY_FILES` (Boolean)
Files copied with a Copy Files build phase are unchanged by default. Setting this to `TRUE` causes property list files (`.plist`) and strings files to be converted as specified by `PLIST_FILE_OUTPUT_FORMAT` and `STRINGS_FILE_OUTPUT_ENCODING`.
Default value: **`NO`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Info.plist Preprocessor Prefix File - `INFOPLIST_PREFIX_HEADER` (String)
Implicitly include the given file when preprocessing the `Info.plist` file. The path given should either be a project relative path or an absolute path.
Default value: **""**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Info.plist Preprocessor Definitions - `INFOPLIST_PREPROCESSOR_DEFINITIONS` (StringList)
Space-separated list of preprocessor macros of the form `foo` or `foo=bar`. These macros are used when preprocessing the `Info.plist` file.
Default value: **""**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Info.plist Other Preprocessor Flags - `INFOPLIST_OTHER_PREPROCESSOR_FLAGS` (StringList)
Other flags to pass to the C preprocessor when preprocessing the `Info.plist` file.
Default value: **""**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Preserve HFS Data - `COPYING_PRESERVES_HFS_DATA` (Boolean)
Causes the copying of resources to preserve resource forks and Finder info.
Default value: **`NO`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Defines Module - `DEFINES_MODULE` (Boolean)
If enabled, the product will be treated as defining its own module. This enables automatic production of LLVM module map files when appropriate, and allows the product to be imported as a module.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Module Map File - `MODULEMAP_FILE` (String)
This is the project-relative path to the LLVM module map file that defines the module structure for the compiler. If empty, it will be automatically generated for appropriate products when `DEFINES_MODULE` is enabled.
Default value: **""**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Private Module Map File - `MODULEMAP_PRIVATE_FILE` (String)
This is the project-relative path to the LLVM module map file that defines the module structure for private headers.
Default value: **""**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Framework Version - `FRAMEWORK_VERSION` (String)
Framework bundles are versioned by having contents in subfolders of a version folder that has links to the current version and its contents.
Default value: **`A`**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




## Search Paths
### Header Search Paths - `HEADER_SEARCH_PATHS` (PathList)
This is a list of paths to folders to be searched by the compiler for included or imported header files when compiling C, Objective-C, C++, or Objective-C++. Paths are delimited by whitespace, so any paths with spaces in them need to be properly quoted.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### User Header Search Paths - `USER_HEADER_SEARCH_PATHS` (PathList)
This is a list of paths to folders to be searched by the compiler for included or imported user header files (those headers listed in quotes) when compiling C, Objective-C, C++, or Objective-C++. Paths are delimited by whitespace, so any paths with spaces in them need to be properly quoted. See `ALWAYS_SEARCH_USER_PATHS` for more details on how this setting is used. If the compiler doesn't support the concept of user headers, then the search paths are prepended to the any existing header search paths defined in `HEADER_SEARCH_PATHS`.
Default value: **""**
Condition Flavors: `arch`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### System Header Search Paths - `SYSTEM_HEADER_SEARCH_PATHS` (PathList)
This is a list of paths to folders to be searched by the compiler for included or imported system header files when compiling C, Objective-C, C++, or Objective-C++. The order is from highest to lowest precedence. Paths are delimited by whitespace, so any paths with spaces in them need to be properly quoted. This setting is very similar to "Header Search Paths", except that headers are passed to the compiler in a way that suppresses most warnings for headers found in system search paths. If the compiler doesn't support the concept of system header search paths, then the search paths are appended to any existing header search paths defined in "Header Search Paths".

Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Library Search Paths - `LIBRARY_SEARCH_PATHS` (PathList)
This is a list of paths to folders to be searched by the linker for libraries used by the product. Paths are delimited by whitespace, so any paths with spaces in them need to be properly quoted.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Framework Search Paths - `FRAMEWORK_SEARCH_PATHS` (PathList)
This is a list of paths to folders containing frameworks to be searched by the compiler for both included or imported header files when compiling C, Objective-C, C++, or Objective-C++, and by the linker for frameworks used by the product. Paths are delimited by whitespace, so any paths with spaces in them must be properly quoted.
Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### System Framework Search Paths - `SYSTEM_FRAMEWORK_SEARCH_PATHS` (PathList)
This is a list of paths to folders containing system frameworks to be searched by the compiler for both included or imported header files when compiling C, Objective-C, C++, or Objective-C++, and by the linker for frameworks used by the product. The order is from highest to lowest precedence. Paths are delimited by whitespace, so any paths with spaces in them need to be properly quoted. This setting is very similar to "Framework Search Paths", except that the search paths are passed to the compiler in a way that suppresses most warnings for headers found in system search paths. If the compiler doesn't support the concept of system framework search paths, then the search paths are appended to any existing framework search paths defined in "Framework Search Paths".

Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Rez Search Paths - `REZ_SEARCH_PATHS` (PathList)
This is a list of paths to search for files with resource manager resources. Paths are delimited by whitespace, so any paths with spaces in them need to be properly quoted.
Default value: **""**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Always Search User Paths (Deprecated) - `ALWAYS_SEARCH_USER_PATHS` (Boolean)
This setting is deprecated as of Xcode 8.3 and may not be supported in future versions. It is recommended that you disable the setting.

If enabled, both `#include <header.h>`-style and `#include "header.h"`-style directives search the paths in `USER_HEADER_SEARCH_PATHS` before `HEADER_SEARCH_PATHS`. As a consequence, user headers, such as your own `String.h` header, have precedence over system headers when using `#include <header.h>`. This is done using the `-iquote` flag for the paths provided in `USER_HEADER_SEARCH_PATHS`. If disabled and your compiler fully supports separate user paths, user headers are only accessible with `#include "header.h"`-style preprocessor directives.

For backwards compatibility reasons, this setting is enabled by default. Disabling it is strongly recommended.
Default value: **`YES`**
Condition Flavors: `arch`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Sub-Directories to Include in Recursive Searches - `INCLUDED_RECURSIVE_SEARCH_PATH_SUBDIRECTORIES` (StringList)
This is a list of `fnmatch()`-style patterns of file or directory names to include when performing a recursive search. By default, this is empty and is only customized when you want to provide exceptions to the list of filename patterns provided in `EXCLUDED_RECURSIVE_SEARCH_PATH_SUBDIRECTORIES`.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Sub-Directories to Exclude in Recursive Searches - `EXCLUDED_RECURSIVE_SEARCH_PATH_SUBDIRECTORIES` (StringList)
This is a list of `fnmatch()`-style patterns of file or directory names to exclude when performing a recursive search. By default, this is set to `\*.nib \*.lproj \*.framework \*.gch \*.xcode (\*) .DS_Store CVS .svn .git .hg`. Normally, if you override this value you should include the default values via the `$(inherited)` macro.
Default value: **`*.nib *.lproj *.framework *.gch *.xcode* *.xcassets (*) .DS_Store CVS .svn .git .hg *.pbproj *.pbxproj`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Use Header Maps - `USE_HEADERMAP` (Boolean)
Enable the use of *Header Maps*, which provide the compiler with a mapping from textual header names to their locations, bypassing the normal compiler header search path mechanisms. This allows source code to include headers from various locations in the file system without needing to update the header search path build settings.
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




## Text-Based API
### Supports Text-Based InstallAPI - `SUPPORTS_TEXT_BASED_API` (Boolean)
Enable to indicate that the target supports `Text-Based InstallAPI`, which will enable its generation during `install` builds.

Default value: **`NO`**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Text-Based InstallAPI Verification Mode - `TAPI_VERIFY_MODE` (Enumeration)
Selects the level of warnings and errors to report when building `Text-Based InstallAPI`.

Default value: **`ErrorsOnly`**

| Enumeration value |
| -------- |
| `{'DisplayName': 'Errors Only', 'Value': 'ErrorsOnly'}` |
| `{'DisplayName': 'Errors and Warnings', 'Value': 'ErrorsAndWarnings'}` |
| `{'DisplayName': 'Pedantic', 'Value': 'Pedantic'}` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Other Text-Based InstallAPI Flags - `OTHER_TAPI_FLAGS` (StringList)
Options defined in this setting are passed to invocations of the `Text-Based InstallAPI` tool.

Default value: **""**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Enable Text-Based Stubs Generation - `GENERATE_TEXT_BASED_STUBS` (bool)
Enables the generation of Text-Based stubs for dynamic libraries and frameworks.

Default value: **`NO`**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Enable Text-Based Stubs Inlining - `INLINE_PRIVATE_FRAMEWORKS` (bool)
Enables private framework inlining for Text-Based Stubs.

Default value: **`NO`**
Condition Flavors: `arch, sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




## Testing
### Test Host - `TEST_HOST` (String)
Path to the executable into which a bundle of tests is injected. Only specify this setting if testing an application or other executable.
Default value: **""**
Condition Flavors: `sdk`

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Treat missing baselines as test failures - `TREAT_MISSING_BASELINES_AS_TEST_FAILURES` (Boolean)
When running tests that measure performance via `XCTestCase`, report missing baselines as test failures.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




## Versioning
### Versioning System - `VERSIONING_SYSTEM` (Enumeration)
Selects the process used for version-stamping generated files.

* *None:* Use no versioning system.
* *Apple Generic:* Use the current project version setting. [apple-generic]
Default value: **""**

| Enumeration value |
| -------- |
| `{'Value': ''}` |
| `{'Value': 'apple-generic'}` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Current Project Version - `CURRENT_PROJECT_VERSION` (String)
This setting defines the current version of the project. The value must be a integer or floating point number, such as `57` or `365.8`.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Versioning Name Prefix - `VERSION_INFO_PREFIX` (String)
Used as a prefix for the name of the version info symbol in the generated versioning source file. If you prefix your exported symbols you will probably want to set this to the same prefix.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Versioning Name Suffix - `VERSION_INFO_SUFFIX` (String)
Used as a suffix for the name of the version info symbol in the generated versioning source file. This is rarely used.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Versioning Username - `VERSION_INFO_BUILDER` (String)
This defines a reference to the user performing a build to be included in the generated Apple Generic Versioning stub. Defaults to the value of the `USER` environment variable.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Generated Versioning Variables - `VERSION_INFO_EXPORT_DECL` (String)
This defines a prefix string for the version info symbol declaration in the generated Apple Generic Versioning stub. This can be used, for example, to add an optional `export` keyword to the version symbol declaration. This should rarely be changed.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Generated Versioning Source Filename - `VERSION_INFO_FILE` (String)
Used to specify a name for the source file that will be generated by Apple Generic Versioning and compiled into your product. By default, this is set to `$(PRODUCT_NAME)_vers.c`.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




