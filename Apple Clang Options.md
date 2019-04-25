# Apple Clang
Apple Clang compiler
File types: C, Objective-C, C++, Objective-C++, sourcecode.asm

Special meanings:
`$(value)` is replaced by the selected value or the default value.

## Address Sanitizer
### Enable C++ Container Overflow Checks - `CLANG_ADDRESS_SANITIZER_CONTAINER_OVERFLOW` (Boolean)
Check for C++ container overflow when Address Sanitizer is enabled. This check requires the entire application to be built with Address Sanitizer. If not, it may report false positives.
Condition: `$(CLANG_ADDRESS_SANITIZER) == YES`

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-D_LIBCPP_HAS_NO_ASAN` |
| `YES` |  |





## Code Generation
### Generate Debug Symbols - `GCC_GENERATE_DEBUGGING_SYMBOLS` (Boolean)
Enables or disables generation of debug symbols. When debug symbols are enabled, the level of detail can be controlled by the `DEBUG_INFORMATION_FORMAT` setting.
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Optimization Level - `GCC_OPTIMIZATION_LEVEL` (Enumeration)
Specifies the degree to which the generated code is optimized for speed and binary size.

* *None:* Do not optimize. [-O0]
  With this setting, the compiler's goal is to reduce the cost of compilation and to make debugging produce the expected results. Statements are independent—if you stop the program with a breakpoint between statements, you can then assign a new value to any variable or change the program counter to any other statement in the function and get exactly the results you would expect from the source code.
* *Fast:* Optimizing compilation takes somewhat more time, and a lot more memory for a large function. [-O1]
  With this setting, the compiler tries to reduce code size and execution time, without performing any optimizations that take a great deal of compilation time. In Apple's compiler, strict aliasing, block reordering, and inter-block scheduling are disabled by default when optimizing.
* *Faster:* The compiler performs nearly all supported optimizations that do not involve a space-speed tradeoff. [-O2]
  With this setting, the compiler does not perform loop unrolling or function inlining, or register renaming. As compared to the `Fast` setting, this setting increases both compilation time and the performance of the generated code.
* *Fastest:* Turns on all optimizations specified by the `Faster` setting and also turns on function inlining and register renaming options. This setting may result in a larger binary. [-O3]
* *Fastest, Smallest:* Optimize for size. This setting enables all `Faster` optimizations that do not typically increase code size. It also performs further optimizations designed to reduce code size. [-Os]
* *Fastest, Aggressive Optimizations:* This setting enables `Fastest` but also enables aggressive optimizations that may break strict standards compliance but should work well on well-behaved code. [-Ofast]

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `0` | `-O0` |
| `1` | `-O1` |
| `2` | `-O2` |
| `3` | `-O3` |
| **`s`** | `-Os` |
| `fast` | `-Ofast` |


### Link-Time Optimization - `LLVM_LTO` (Enumeration)
Enabling this setting allows optimization across file boundaries during linking.

* *No:* Disabled. Do not use link-time optimization.
* *Monolithic Link-Time Optimization:* This mode performs monolithic link-time optimization of binaries, combining all executable code into a single unit and running aggressive compiler optimizations.
* *Incremental Link-Time Optimization:* This mode performs partitioned link-time optimization of binaries, inlining between compilation units and running aggressive compiler optimizations on each unit in parallel. This enables fast incremental builds and uses less memory than Monolithic LTO.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-flto` |
| `YES_THIN` | `-flto=thin` |


| Enumeration value | Linker Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES_THIN` | `-flto=thin,-Xlinker,-cache_path_lto,-Xlinker,$(OBJROOT)/LTOCache` |
| `YES` |  |



### No Common Blocks - `GCC_NO_COMMON_BLOCKS` (Boolean)
In C, allocate even uninitialized global variables in the data section of the object file, rather than generating them as common blocks. This has the effect that if the same variable is declared (without `extern`) in two different compilations, you will get an error when you link them.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fno-common` |



### Make Strings Read-Only - `GCC_REUSE_STRINGS` (Boolean)
Reuse string literals.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-fwritable-strings` |
| **`YES`** |  |



### Generate Position-Dependent Code - `GCC_DYNAMIC_NO_PIC` (Boolean)
Faster function calls for applications. Not appropriate for shared libraries, which need to be position-independent.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-mdynamic-no-pic` |



### Kernel Development Mode - `GCC_ENABLE_KERNEL_DEVELOPMENT` (Boolean)
Activating this setting enables kernel development mode.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-mkernel` |



### Unroll Loops - `GCC_UNROLL_LOOPS` (Boolean)
Unrolls loops. Unrolling makes the code larger, but may make it faster by reducing the number of branches executed.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-funroll-loops` |



### Relax IEEE Compliance - `GCC_FAST_MATH` (Boolean)
Enables some floating point optimizations that are not IEEE754-compliant, but which usually work. Programs that require strict IEEE compliance may not work with this option.
Condition: `$(LLVM_IMPLICIT_AGGRESSIVE_OPTIMIZATIONS) == NO`

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-ffast-math` |



### Enforce Strict Aliasing - `GCC_STRICT_ALIASING` (Boolean)
Optimize code by making more aggressive assumptions about whether pointers can point to the same objects as other pointers. Programs that use pointers a lot may benefit from this, but programs that don't strictly follow the ISO C rules about the type with which an object may be accessed may behave unexpectedly.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-fno-strict-aliasing` |
| **`YES`** | `-fstrict-aliasing` |



### Instrument Program Flow - `GCC_INSTRUMENT_PROGRAM_FLOW_ARCS` (Boolean)
Activating this setting indicates that code should be added so program flow arcs are instrumented.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fprofile-arcs` |


| Boolean value | Linker Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fprofile-arcs` |



### Generate Legacy Test Coverage Files - `GCC_GENERATE_TEST_COVERAGE_FILES` (Boolean)
Activating this setting causes a `notes` file to be produced that the `gcov` code-coverage utility can use to show program coverage.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-ftest-coverage` |


| Boolean value | Linker Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-ftest-coverage` |



### Debug Information Level - `CLANG_DEBUG_INFORMATION_LEVEL` (Enumeration)
Toggles the amount of debug information emitted when debug symbols are enabled. This can impact the size of the generated debug information, which may matter in some cases for large projects, such as when using LTO.
Condition: `$(GCC_GENERATE_DEBUGGING_SYMBOLS)`

| Enumeration value | Command Line Argument |
| ----- | -------- |
| **`default`** |  |
| `line-tables-only` | `-gline-tables-only` |



### Enable Additional Vector Extensions - `CLANG_X86_VECTOR_INSTRUCTIONS` (Enumeration)
Enables the use of extended vector instructions. Only used when targeting Intel architectures.

Default value: **`$(DEFAULT_SSE_LEVEL_4_2_$(GCC_ENABLE_SSE42_EXTENSIONS))`**
Architectures: `i386, x86_64`

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `avx512` | `-march=skylake-avx512` |
| `default` |  |
| `sse3` | ``-msse3`` |
| `ssse3` | ``-mssse3`` |
| `sse4.1` | ``-msse4.1`` |
| `sse4.2` | ``-msse4.2`` |
| `avx` | ``-mavx`` |
| `avx2` | ``-mavx2`` |



### Symbols Hidden by Default - `GCC_SYMBOLS_PRIVATE_EXTERN` (Boolean)
When enabled, all symbols are declared `private extern` unless explicitly marked to be exported using `\_\_attribute\_\_((visibility("default")))` in code. If not enabled, all symbols are exported unless explicitly marked as `private extern`. See [Controlling Symbol Visibility](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/CppRuntimeEnv/Articles/SymbolVisibility.html#//apple_ref/doc/uid/TP40001670-CJBGBHEJ) in [C++ Runtime Environment Programming Guide](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/CppRuntimeEnv/CPPRuntimeEnv.html).

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fvisibility=hidden` |



### Inline Methods Hidden - `GCC_INLINES_ARE_PRIVATE_EXTERN` (Boolean)
When enabled, out-of-line copies of inline methods are declared `private extern`.
File types: C++, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fvisibility-inlines-hidden` |



### Statics are Thread-Safe - `GCC_THREADSAFE_STATICS` (Boolean)
Emits extra code to use the routines specified in the C++ ABI for thread-safe initialization of local statics. You can disable this option to reduce code size slightly in code that doesn't need to be thread-safe.

File types: C++, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-fno-threadsafe-statics` |
| **`YES`** |  |



### Optimization Profile File - `CLANG_OPTIMIZATION_PROFILE_FILE` (Path)
The path to the file of the profile data to use when `CLANG_USE_OPTIMIZATION_PROFILE` is enabled.
Default value: **`$(SRCROOT)/OptimizationProfiles/$(PROJECT_NAME).profdata`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Use Optimization Profile - `CLANG_USE_OPTIMIZATION_PROFILE` (Boolean)
When this setting is enabled, `clang` will use the optimization profile collected for a target when building it.
Condition: `! $(CLANG_INSTRUMENT_FOR_OPTIMIZATION_PROFILING) && ! $(CLANG_COVERAGE_MAPPING)`

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fprofile-instr-use=$(CLANG_OPTIMIZATION_PROFILE_FILE)` |



### Enable Code Coverage Support - `CLANG_ENABLE_CODE_COVERAGE` (Boolean)
Enables building with code coverage instrumentation. This is only used when the build has code coverage enabled, which is typically done via the Xcode scheme settings.

Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




## Custom Compiler Flags
### Other C Flags - `OTHER_CFLAGS` (StringList)
Space-separated list of additional flags to pass to the compiler for C and Objective-C files. Be sure to backslash-escape any arguments that contain spaces or special characters, such as path names that may contain spaces. Use this setting if Xcode does not already provide UI for a particular C or Objective-C compiler flag.
File types: C, Objective-C

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Other C++ Flags - `OTHER_CPLUSPLUSFLAGS` (StringList)
Space-separated list of additional flags to pass to the compiler for C++ and Objective-C++ files. Be sure to backslash-escape any arguments that contain spaces or special characters, such as path names that may contain spaces. Use this setting if Xcode does not already provide UI for a C++ or Objective-C++ compiler flag.
File types: C++, Objective-C++

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Other Warning Flags - `WARNING_CFLAGS` (StringList)
Space-separated list of additional warning flags to pass to the compiler. Use this setting if Xcode does not already provide UI for a particular compiler warning flag.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




## Language
### Compile Sources As - `GCC_INPUT_FILETYPE` (Enumeration)
Specifies whether to compile each source file according to its file type, or whether to treat all source files in the target as if they are of a specific language.

| Enumeration value |
| -------- |
| **`automatic`** |
| `sourcecode.c.c` |
| `sourcecode.c.objc` |
| `sourcecode.cpp.cpp` |
| `sourcecode.cpp.objcpp` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Use Standard System Header Directory Searching - `GCC_USE_STANDARD_INCLUDE_SEARCHING` (Boolean)
Controls whether the standard system directories are searched for header files. When disabled, only the directories you have specified with `-I` options (and the directory of the current file, if appropriate) are searched.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-nostdinc` |
| **`YES`** |  |



### C Language Dialect - `GCC_C_LANGUAGE_STANDARD` (Enumeration)
Choose a standard or non-standard C language dialect.

* *ANSI C:* Accept ISO C90 and ISO C++, turning off GNU extensions that are incompatible. [-ansi]
  Incompatible GNU extensions include the `asm`, `inline`, and `typeof` keywords (but not the equivalent `\_\_asm\_\_`, `\_\_inline\_\_`, and `\_\_typeof\_\_` forms), and the `//` syntax for comments.
  This setting also enables trigraphs.
* *C89:* Accept ISO C90 (1990), but not GNU extensions. [-std=c89]
* *GNU89:* Accept ISO C90 and GNU extensions. [-std=gnu89]
* *C99:* Accept ISO C99 (1999), but not GNU extensions. [-std=c99]
* *GNU99:* Accept ISO C99 and GNU extensions. [-std=gnu99]
* *C11:* Accept ISO C11 (2011), but not GNU extensions. [-std=c11]
* *GNU11:* Accept ISO C11 and GNU extensions. [-std=gnu11]
* *Compiler Default:* Tells the compiler to use its default C language dialect. This is normally the best choice unless you have specific needs. (Currently equivalent to GNU99.)
File types: C, Objective-C

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `ansi` | `-ansi` |
| **`compiler-default`** |  |
| `c89` | ``-std=c89`` |
| `gnu89` | ``-std=gnu89`` |
| `c99` | ``-std=c99`` |
| `gnu99` | ``-std=gnu99`` |
| `c11` | ``-std=c11`` |
| `gnu11` | ``-std=gnu11`` |



### 'char' Type Is Unsigned - `GCC_CHAR_IS_UNSIGNED_CHAR` (Boolean)
Enabling this setting causes `char` to be unsigned by default, disabling it causes `char` to be signed by default.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-funsigned-char` |



### Allow 'asm', 'inline', 'typeof' - `GCC_ENABLE_ASM_KEYWORD` (Boolean)
Controls whether `asm`, `inline`, and `typeof` are treated as keywords or whether they can be used as identifiers.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-fno-asm` |
| **`YES`** |  |



### Recognize Builtin Functions - `GCC_ENABLE_BUILTIN_FUNCTIONS` (Boolean)
Controls whether builtin functions that do not begin with `\_\_builtin\_` as prefix are recognized.

GCC normally generates special code to handle certain builtin functions more efficiently; for instance, calls to `alloca` may become single instructions that adjust the stack directly, and calls to `memcpy` may become inline copy loops. The resulting code is often both smaller and faster, but since the function calls no longer appear as such, you cannot set a breakpoint on those calls, nor can you change the behavior of the functions by linking with a different library. In addition, when a function is recognized as a builtin function, GCC may use information about that function to warn about problems with calls to that function, or to generate more efficient code, even if the resulting code still contains calls to that function. For example, warnings are given with `-Wformat` for bad calls to `printf`, when `printf` is built in, and `strlen` is known not to modify global memory.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-fno-builtin` |
| **`YES`** |  |



### Enable Trigraphs - `GCC_ENABLE_TRIGRAPHS` (Boolean)
Controls whether or not trigraphs are permitted in the source code.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-trigraphs` |
| `YES` | `-trigraphs` |



### Recognize Pascal Strings - `GCC_ENABLE_PASCAL_STRINGS` (Boolean)
Recognize and construct Pascal-style string literals. Its use in new code is discouraged.

Pascal string literals take the form `"\pstring"` . The special escape sequence `\p` denotes the Pascal length byte for the string, and will be replaced at compile time with the number of characters that follow. The `\p` may only appear at the beginning of a string literal, and may not appear in wide string literals or as an integral constant.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| **`YES`** | `-fpascal-strings` |



### Short Enumeration Constants - `GCC_SHORT_ENUMS` (Boolean)
Make enums only as large as needed for the range of possible values.

This setting generates code that may not binary compatible with code generated without this setting or with macOS frameworks.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fshort-enums` |



### Enable Linking With Shared Libraries - `GCC_LINK_WITH_DYNAMIC_LIBRARIES` (Boolean)
Enabling this option allows linking with the shared libraries. This is the default for most product types.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-static` |
| **`YES`** |  |



### Generate Floating Point Library Calls - `GCC_ENABLE_FLOATING_POINT_LIBRARY_CALLS` (Boolean)
Generate output containing library calls for floating point.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-msoft-float` |



### Prefix Header - `GCC_PREFIX_HEADER` (String)
Implicitly include the named header. The path given should either be a project relative path or an absolute path.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Precompile Prefix Header - `GCC_PRECOMPILE_PREFIX_HEADER` (Boolean)
Generates a precompiled header for the prefix header, which should reduce overall build times.

Precompiling the prefix header will be most effective if the contents of the prefix header or any file it includes change rarely. If the contents of the prefix header or any file it includes change frequently, there may be a negative impact to overall build time.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Increase Sharing of Precompiled Headers - `GCC_INCREASE_PRECOMPILED_HEADER_SHARING` (Boolean)
Enabling this option will enable increased sharing of precompiled headers among targets that share the same prefix header and precompiled header directory.

Xcode distinguishes between precompiled header (PCH) files by generating a hash value based on the command-line options to the compiler used to create the PCH. Enabling this option will exclude certain compiler options from that hash. Presently this option will exclude search path options (`-I`, `-iquote`, `-isystem`, `-F`, `-L`) from the hash.

Enabling increased sharing of PCH files carries some risk—if two targets use the same prefix header but have different include paths that cause the prefix header to include different files when they are precompiled, then subtle problems may result because one target will use a PCH that was built using files included by the other target. In this case, this option must be turned off in order to enforce correctness.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### CodeWarrior/MS-Style Inline Assembly - `GCC_CW_ASM_SYNTAX` (Boolean)
Enable the CodeWarrior/Microsoft syntax for inline assembly code in addition to the standard GCC syntax.
Architectures: `i386, x86_64`

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| **`YES`** | `-fasm-blocks` |





## Language - C++
### C++ Language Dialect - `CLANG_CXX_LANGUAGE_STANDARD` (Enumeration)
Choose a standard or non-standard C++ language dialect. Options include:

* *C++98:* Accept ISO C++ 1998 with amendments, but not GNU extensions. [-std=c++98]
* *GNU++98:* Accept ISO C++ 1998 with amendments and GNU extensions. [-std=gnu++98]
* *C++11:* Accept the ISO C++ 2011 standard with amendments, but not GNU extensions. [-std=c++11]
* *GNU++11:* Accept the ISO C++ 2011 standard with amendments and GNU extensions. [-std=gnu++11]
* *C++14:* Accept the ISO C++ 2014 standard with amendments, but not GNU extensions. [-std=c++14]
* *GNU++14:* Accept the ISO C++ 2014 standard with amendments and GNU extensions. [-std=gnu++14]
* *C++17:* Accept the ISO C++ 2017 standard with amendments, but not GNU extensions. [-std=c++17]
* *GNU++17:* Accept the ISO C++ 2017 standard with amendments and GNU extensions. [-std=gnu++17]
* *Compiler Default:* Tells the compiler to use its default C++ language dialect. This is normally the best choice unless you have specific needs. (Currently equivalent to GNU++98.)
File types: C++, Objective-C++

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `c++0x` | `-std=c++11` |
| `c++17` | `-std=c++1z` |
| **`compiler-default`** |  |
| `gnu++0x` | `-std=gnu++11` |
| `gnu++17` | `-std=gnu++1z` |
| `c++98` | ``-std=c++98`` |
| `gnu++98` | ``-std=gnu++98`` |
| `c++14` | ``-std=c++14`` |
| `gnu++14` | ``-std=gnu++14`` |



### C++ Standard Library - `CLANG_CXX_LIBRARY` (Enumeration)
Choose a version of the C++ standard library to use.

* *libstdc++:* A traditional C++ standard library that works with GCC and Clang (default).
* *libc++:* A highly optimized C++ standard library that works only with Clang, and is designed to support new C++11 features.
File types: C++, Objective-C++

| Enumeration value | Command Line Argument |
| ----- | -------- |
| **`compiler-default`** |  |
| `libstdc++` | ``-stdlib=libstdc++`` |
| `libc++` | ``-stdlib=libc++`` |


| Enumeration value | Linker Argument |
| ----- | -------- |
| **`compiler-default`** |  |
| `libstdc++` | ``-stdlib=libstdc++`` |
| `libc++` | ``-stdlib=libc++`` |



### Enable C++ Exceptions - `GCC_ENABLE_CPP_EXCEPTIONS` (Boolean)
Enable C++ exception handling. Generates extra code needed to propagate exceptions. For some targets, this implies GCC will generate frame unwind information for all functions, which can produce significant data size overhead, although it does not affect execution. If you do not specify this option, GCC will enable it by default for languages like C++ that normally require exception handling, and disable it for languages like C that do not normally require it. However, you may need to enable this option when compiling C code that needs to interoperate properly with exception handlers written in C++.
File types: C++, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-fno-exceptions` |
| **`YES`** |  |



### Enable C++ Runtime Types - `GCC_ENABLE_CPP_RTTI` (Boolean)
Enable generation of information about every class with virtual functions for use by the C++ runtime type identification features (`dynamic_cast` and `typeid`). If you don't use those parts of the language, you can save some space by using this flag. Note that exception handling uses the same information, but it will generate it as needed.
File types: C++, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-fno-rtti -fno-sanitize=vptr` |
| **`YES`** |  |





## Language - Modules
### Enable Modules (C and Objective-C) - `CLANG_ENABLE_MODULES` (Boolean)
Enables the use of modules for system APIs. System headers are imported as semantic modules instead of raw headers. This can result in faster builds and project indexing.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fmodules` |



### Enable Clang Module Debugging - `CLANG_ENABLE_MODULE_DEBUGGING` (Boolean)
When this setting is enabled, `clang` will use the shared debug info available in `clang` modules and precompiled headers. This results in smaller build artifacts, faster compile times, and more complete debug info. This setting should only be disabled when building static libraries with debug info for distribution.

Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Link Frameworks Automatically - `CLANG_MODULES_AUTOLINK` (Boolean)
Automatically link SDK frameworks that are referenced using `#import` or `#include`. This feature requires also enabling support for modules. This build setting only applies to C-family languages.
Condition: `$(CLANG_ENABLE_MODULES) == YES`

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-fno-autolink` |
| **`YES`** |  |



### Disable Private Modules Warnings - `CLANG_MODULES_DISABLE_PRIVATE_WARNING` (Boolean)
Disable warnings related to the recommended use of private module naming. This only makes sense when support for modules is enabled.
Condition: `$(CLANG_ENABLE_MODULES) == YES`

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Wno-private-module` |



### Allow Non-modular Includes In Framework Modules - `CLANG_ALLOW_NON_MODULAR_INCLUDES_IN_FRAMEWORK_MODULES` (Boolean)
Enabling this setting allows non-modular includes to be used from within framework modules. This is inherently unsafe, as such headers might cause duplicate definitions when used by any client that imports both the framework and the non-modular includes.

Condition: `$(CLANG_ENABLE_MODULES) == YES`

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wnon-modular-include-in-framework-module -Werror=non-modular-include-in-framework-module` |
| `YES` |  |





## Language - Objective-C
### Objective-C Automatic Reference Counting - `CLANG_ENABLE_OBJC_ARC` (Boolean)
Compiles reference-counted Objective-C code (when garbage collection is not enabled) to use Automatic Reference Counting. Code compiled using automated reference counting is compatible with other code (such as frameworks) compiled using either manual reference counting (for example, traditional `retain` and `release` messages) or automated reference counting. Using this mode is currently incompatible with compiling code to use Objective-C Garbage Collection.
File types: Objective-C, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fobjc-arc` |


| Boolean value | Linker Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fobjc-arc` |



### Weak References in Manual Retain Release - `CLANG_ENABLE_OBJC_WEAK` (Boolean)
Compiles Objective-C code to enable weak references for code compiled with manual retain release (MRR) semantics.
File types: Objective-C, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fobjc-weak` |



### Implicitly Link Objective-C Runtime Support - `CLANG_LINK_OBJC_RUNTIME` (Boolean)
When linking a target using Objective-C code, implicitly link in Foundation (and if deploying back to an older OS) a backwards compatibility library to allow newer language features to run on an OS where the runtime support is not natively available. Most targets that use Objective-C should use this, although there are rare cases where a target should opt out of this behavior.
File types: Objective-C, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| **`YES`** |  |


| Boolean value | Linker Argument |
| ----- | -------- |
| `NO` |  |
| **`YES`** | `-fobjc-link-runtime` |



### Enable Objective-C Exceptions - `GCC_ENABLE_OBJC_EXCEPTIONS` (Boolean)
This setting enables `@try`/`@catch`/`@throw` syntax for handling exceptions in Objective-C code. Only applies to Objective-C.
File types: Objective-C, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-fno-objc-exceptions` |
| **`YES`** |  |





## None
### `CLANG_TARGET_TRIPLE_ARCHS` (StringList)
Default value: **`$(CURRENT_ARCH)`**
Condition: `$(USE_LLVM_TARGET_TRIPLES_FOR_CLANG) == YES`

| Command Line Argument |
| -------- |
| `-target $(value)-$(LLVM_TARGET_TRIPLE_VENDOR)-$(LLVM_TARGET_TRIPLE_OS_VERSION)$(LLVM_TARGET_TRIPLE_SUFFIX)` |


### `CLANG_TARGET_TRIPLE_VARIANTS` (StringList)
Condition: `$(USE_LLVM_TARGET_TRIPLES_FOR_CLANG) == YES`
Condition Flavors: `arch`

| Command Line Argument |
| -------- |
| `-target-variant $(stringlist)` |


### `arch` (String)
Condition: `$(USE_LLVM_TARGET_TRIPLES_FOR_CLANG) != YES`

| Command Line Argument |
| -------- |
| `-arch $(string)` |


### `diagnostic_message_length` (String)
Default value: **`0`**

| Command Line Argument |
| -------- |
| `-fmessage-length=$(value)` |


### `print_note_include_stack` (Boolean)

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| **`YES`** | `-fdiagnostics-show-note-include-stack` |



### `CLANG_MACRO_BACKTRACE_LIMIT` (String)
Default value: **`0`**

| Command Line Argument |
| -------- |
| `-fmacro-backtrace-limit=$(value)` |


### `CLANG_RETAIN_COMMENTS_FROM_SYSTEM_HEADERS` (Boolean)

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fretain-comments-from-system-headers` |



### `CLANG_COLOR_DIAGNOSTICS` (Boolean)
Default value: **`$(COLOR_DIAGNOSTICS)`**

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| `YES` | `-fcolor-diagnostics` |



### `GCC_OPERATION` (Enumeration)

| Enumeration value |
| -------- |
| **`compile`** |
| `generate-preprocessed` |
| `generate-assembler` |
| `precompile` |
| `separate-symbols` |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CLANG_DEBUG_MODULES` (Boolean)
Default value: **`$(CLANG_ENABLE_MODULE_DEBUGGING)`**
Condition: `$(GCC_GENERATE_DEBUGGING_SYMBOLS) == YES  &&  ( $(CLANG_ENABLE_MODULES) == YES  ||  ( $(GCC_PREFIX_HEADER) != ''  &&  $(GCC_PRECOMPILE_PREFIX_HEADER) == YES ) )`

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| `YES` | `-gmodules` |



### `CLANG_MODULE_CACHE_PATH` (String)
Default value: **`$(MODULE_CACHE_DIR)`**
Condition: `$(CLANG_ENABLE_MODULES) == YES`

| String value | Command Line Argument |
| ----- | -------- |
| `<<empty>>` |  |
| `<<otherwise>>` | `-fmodules-cache-path=$(CLANG_MODULE_CACHE_PATH)` |



### `CLANG_MODULE_LSV` (Boolean)
Condition: `$(CLANG_ENABLE_MODULES) == YES`

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Xclang -fmodules-local-submodule-visibility` |



### `CLANG_MODULES_PRUNE_INTERVAL` (String)
Default value: **`86400`**
Condition: `$(CLANG_ENABLE_MODULES) == YES`

| String value | Command Line Argument |
| ----- | -------- |
| `<<empty>>` |  |
| `<<otherwise>>` | `-fmodules-prune-interval=$(value)` |



### `CLANG_MODULES_PRUNE_AFTER` (String)
Default value: **`345600`**
Condition: `$(CLANG_ENABLE_MODULES) == YES`

| String value | Command Line Argument |
| ----- | -------- |
| `<<empty>>` |  |
| `<<otherwise>>` | `-fmodules-prune-after=$(value)` |



### `CLANG_MODULES_IGNORE_MACROS` (StringList)
Default value: **`$(GCC_PREPROCESSOR_DEFINITIONS_NOT_USED_IN_PRECOMPS)`**
Condition: `$(CLANG_ENABLE_MODULES) == YES`

| Command Line Argument |
| -------- |
| `-fmodules-ignore-macro=$(value)` |


### `CLANG_MODULES_VALIDATE_SYSTEM_HEADERS` (Boolean)
Condition: `$(CLANG_ENABLE_MODULES) == YES`

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fmodules-validate-system-headers` |



### `CLANG_MODULES_BUILD_SESSION_FILE` (String)
Condition: `$(CLANG_ENABLE_MODULES) == YES`

| String value | Command Line Argument |
| ----- | -------- |
| `<<empty>>` |  |
| `<<otherwise>>` | `-fbuild-session-file=$(value) -fmodules-validate-once-per-build-session` |



### `CLANG_ENABLE_MODULE_IMPLEMENTATION_OF` (Boolean)
Condition: `$(CLANG_ENABLE_MODULES) == YES && $(DEFINES_MODULE) == YES`

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| **`YES`** | `-fmodule-name=$(PRODUCT_MODULE_NAME)` |



### `CLANG_ENABLE_APP_EXTENSION` (Boolean)
Default value: **`$(APPLICATION_EXTENSION_API_ONLY)`**

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| `YES` | `-fapplication-extension` |


| Boolean value | Linker Argument |
| ----- | -------- |
| `NO` |  |
| `YES` | `-fapplication-extension` |



### `LLVM_OPTIMIZATION_LEVEL_VAL_0` (Boolean)
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `LLVM_OPTIMIZATION_LEVEL_VAL_1` (Boolean)
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `LLVM_OPTIMIZATION_LEVEL_VAL_2` (Boolean)
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `LLVM_OPTIMIZATION_LEVEL_VAL_3` (Boolean)
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `LLVM_OPTIMIZATION_LEVEL_VAL_s` (Boolean)
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `LLVM_OPTIMIZATION_LEVEL_VAL_fast` (Boolean)
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `LLVM_IMPLICIT_AGGRESSIVE_OPTIMIZATIONS` (Boolean)
Default value: **`$(LLVM_OPTIMIZATION_LEVEL_VAL_$(GCC_OPTIMIZATION_LEVEL))`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Incorrect Uses of Nullable Values - `CLANG_WARN_NULLABLE_TO_NONNULL_CONVERSION` (Boolean)
Warns when a nullable expression is used somewhere it’s not allowed, such as when passed as a `_Nonnull` parameter.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Wnullable-to-nonnull-conversion` |



### `GCC_WARN_MULTIPLE_DEFINITION_TYPES_FOR_SELECTOR` (Boolean)
File types: Objective-C, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-selector` |
| `YES` | `-Wselector` |



### `GCC_PRODUCT_TYPE_PREPROCESSOR_DEFINITIONS` (StringList)
Default value: **""**

| Command Line Argument |
| -------- |
| `-D$(value)` |


### `USE_HEADERMAP` (Boolean)
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `HEADERMAP_FILE_FORMAT` (Enumeration)

| Enumeration value |
| -------- |
| **`traditional`** |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CPP_HEADERMAP_FILE` (Path)
Default value: **`$(TEMP_DIR)/$(PRODUCT_NAME).hmap`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CPP_HEADERMAP_FILE_FOR_GENERATED_FILES` (Path)
Default value: **`$(TEMP_DIR)/$(PRODUCT_NAME)-generated-files.hmap`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CPP_HEADERMAP_FILE_FOR_OWN_TARGET_HEADERS` (Path)
Default value: **`$(TEMP_DIR)/$(PRODUCT_NAME)-own-target-headers.hmap`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CPP_HEADERMAP_FILE_FOR_ALL_TARGET_HEADERS` (Path)
Default value: **`$(TEMP_DIR)/$(PRODUCT_NAME)-all-target-headers.hmap`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CPP_HEADERMAP_FILE_FOR_ALL_NON_FRAMEWORK_TARGET_HEADERS` (Path)
Default value: **`$(TEMP_DIR)/$(PRODUCT_NAME)-all-non-framework-target-headers.hmap`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CPP_HEADERMAP_FILE_FOR_PROJECT_FILES` (Path)
Default value: **`$(TEMP_DIR)/$(PRODUCT_NAME)-project-headers.hmap`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CPP_HEADERMAP_PRODUCT_HEADERS_VFS_FILE` (Path)
Default value: **`$(PROJECT_TEMP_DIR)/all-product-headers.yaml`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `USE_HEADER_SYMLINKS` (Boolean)
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CPP_HEADER_SYMLINKS_DIR` (Path)
Default value: **`$(TEMP_DIR)/$(PRODUCT_NAME).hdrs`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `SDKROOT` (Path)

| Command Line Argument |
| -------- |
| `-isysroot $(path)` |


### `GCC_USE_GCC3_PFE_SUPPORT` (Boolean)
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `GCC_PFE_FILE_C_DIALECTS` (StringList)
Default value: **`c objective-c c++ objective-c++`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `ENABLE_APPLE_KEXT_CODE_GENERATION` (Boolean)
File types: C++, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fapple-kext` |



### Enable Exceptions - `GCC_ENABLE_EXCEPTIONS` (Boolean)
Enable exception handling. Generates extra code needed to propagate exceptions. For some targets, this implies GCC will generate frame unwind information for all functions, which can produce significant data size overhead, although it does not affect execution. If you do not specify this option, GCC will enable it by default for languages like C++ and Objective-C that normally require exception handling, and disable it for languages like C that do not normally require it. However, you may need to enable this option when compiling C code that needs to interoperate properly with exception handlers written in other languages. You may also wish to disable this option if you are compiling older programs that don't use exception handling.
Default value: **`NO`**

| Command Line Argument |
| -------- |
| `-fexceptions` |


### `GCC_MACOSX_VERSION_MIN` (String)
Default value: **`$($(DEPLOYMENT_TARGET_SETTING_NAME))`**
Condition: `$(USE_LLVM_TARGET_TRIPLES_FOR_CLANG) != YES`

| String value | Command Line Argument |
| ----- | -------- |
| `<<empty>>` |  |
| `<<otherwise>>` | `-$(DEPLOYMENT_TARGET_CLANG_FLAG_NAME)=$(value)` |



### `GCC_DEBUG_INFORMATION_FORMAT` (Enumeration)
Default value: **`$(DEBUG_INFORMATION_FORMAT)`**
Condition: `$(GCC_GENERATE_DEBUGGING_SYMBOLS)`

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `dwarf` | `-g` |
| `dwarf-with-dsym` | `-g` |



### Enable SSE3 Extensions - `GCC_ENABLE_SSE3_EXTENSIONS` (Boolean)
Specifies whether the binary uses the builtin functions that provide access to the SSE3 extensions to the IA-32 architecture.

Architectures: `i386, x86_64`

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` |  |



### `GCC_ENABLE_SUPPLEMENTAL_SSE3_INSTRUCTIONS` (Boolean)
Architectures: `i386, x86_64`

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` |  |



### Enable SSE4.1 Extensions - `GCC_ENABLE_SSE41_EXTENSIONS` (Boolean)
Specifies whether the binary uses the builtin functions that provide access to the SSE4.1 extensions to the IA-32 architecture.

Architectures: `i386, x86_64`

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` |  |



### Enable SSE4.2 Extensions - `GCC_ENABLE_SSE42_EXTENSIONS` (Boolean)
Specifies whether the binary uses the builtin functions that provide access to the SSE4.2 extensions to the IA-32 architecture.

Architectures: `i386, x86_64`

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` |  |



### `DEFAULT_SSE_LEVEL_3_YES` (String)
Default value: **`sse3`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `DEFAULT_SSE_LEVEL_3_NO` (String)
Default value: **`default`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `DEFAULT_SSE_LEVEL_3_SUPPLEMENTAL_YES` (String)
Default value: **`ssse3`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `DEFAULT_SSE_LEVEL_3_SUPPLEMENTAL_NO` (String)
Default value: **`$(DEFAULT_SSE_LEVEL_3_$(GCC_ENABLE_SSE3_EXTENSIONS))`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `DEFAULT_SSE_LEVEL_4_1_YES` (String)
Default value: **`sse4.1`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `DEFAULT_SSE_LEVEL_4_1_NO` (String)
Default value: **`$(DEFAULT_SSE_LEVEL_3_SUPPLEMENTAL_$(GCC_ENABLE_SUPPLEMENTAL_SSE3_INSTRUCTIONS))`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `DEFAULT_SSE_LEVEL_4_2_YES` (String)
Default value: **`sse4.2`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `DEFAULT_SSE_LEVEL_4_2_NO` (String)
Default value: **`$(DEFAULT_SSE_LEVEL_4_1_$(GCC_ENABLE_SSE41_EXTENSIONS))`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `GCC_OBJC_ABI_VERSION` (Enumeration)
Default value: **`$(OBJC_ABI_VERSION)`**
File types: Objective-C, Objective-C++

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `<<empty>>` |  |
| `1` | ``-fobjc-abi-version=1`` |
| `2` | ``-fobjc-abi-version=2`` |



### `GCC_OBJC_LEGACY_DISPATCH` (Boolean)
File types: Objective-C, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fobjc-legacy-dispatch` |



### `CLANG_INSTRUMENT_FOR_OPTIMIZATION_PROFILING` (Boolean)

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fprofile-instr-generate` |


| Boolean value | Linker Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fprofile-instr-generate` |



### `CLANG_COVERAGE_MAPPING` (Boolean)
Condition: `$(CLANG_ENABLE_CODE_COVERAGE)`

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fprofile-instr-generate -fcoverage-mapping` |



### `CLANG_COVERAGE_MAPPING_LINKER_ARGS` (Boolean)
Default value: **`$(CLANG_COVERAGE_MAPPING)`**

| Boolean value | Linker Argument |
| ----- | -------- |
| `NO` |  |
| `YES` | `-fprofile-instr-generate` |



### `CLANG_BITCODE_GENERATION_MODE` (Enumeration)
Default value: **`$(BITCODE_GENERATION_MODE)`**
Condition: `$(ENABLE_BITCODE) == YES`
Architectures: `arm64, armv7, armv7s, armv7k`

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `bitcode` | `-fembed-bitcode` |
| `marker` | `-fembed-bitcode-marker` |
| `none` |  |



### `CLANG_ADDRESS_SANITIZER` (Boolean)
Default value: **`$(ENABLE_ADDRESS_SANITIZER)`**

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| `YES` | `-fsanitize=address` |


| Boolean value | Linker Argument |
| ----- | -------- |
| `NO` |  |
| `YES` | `-fsanitize=address` |



### `CLANG_ADDRESS_SANITIZER_USE_AFTER_SCOPE` (Boolean)
Condition: `$(CLANG_ADDRESS_SANITIZER) == YES`

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fsanitize-address-use-after-scope` |



### `CLANG_UNDEFINED_BEHAVIOR_SANITIZER` (Boolean)
Default value: **`$(ENABLE_UNDEFINED_BEHAVIOR_SANITIZER)`**

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| `YES` | `-fsanitize=undefined -fno-sanitize=enum,return,float-divide-by-zero,function,vptr` |


| Boolean value | Linker Argument |
| ----- | -------- |
| `NO` |  |
| `YES` | `-fsanitize=undefined` |



### `CLANG_INDEX_STORE_PATH` (Path)
Default value: **`$(INDEX_DATA_STORE_DIR)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CLANG_INDEX_STORE_ENABLE` (Boolean)
Default value: **`$(INDEX_ENABLE_DATA_STORE)`**
Condition: `$(COMPILER_INDEX_STORE_ENABLE) == YES  ||  ( $(COMPILER_INDEX_STORE_ENABLE) == Default  &&  $(GCC_OPTIMIZATION_LEVEL) == 0 )`

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| `YES` | `-index-store-path $(CLANG_INDEX_STORE_PATH)` |



### `CLANG_THREAD_SANITIZER` (Boolean)
Default value: **`$(ENABLE_THREAD_SANITIZER)`**
Architectures: `x86_64, arm64`

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| `YES` | `-fsanitize=thread` |



### `CLANG_ARC_MIGRATE_PRECHECK` (Enumeration)

| Enumeration value | Command Line Argument |
| ----- | -------- |
| **`donothing`** |  |
| `precheck` | `-ccc-arcmt-check` |



### `CLANG_ARC_MIGRATE_DIR` (Path)

| Command Line Argument |
| -------- |
| `-ccc-arcmt-migrate $(path)` |


### `CLANG_OBJC_MIGRATE_DIR` (Path)

| Command Line Argument |
| -------- |
| `-ccc-objcmt-migrate $(path)` |


### `CLANG_ARC_MIGRATE_EMIT_ERROR` (Boolean)

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-arcmt-migrate-emit-errors` |



### `CLANG_ARC_MIGRATE_REPORT_OUTPUT` (Path)

| Command Line Argument |
| -------- |
| `-arcmt-migrate-report-output $(path)` |




## Preprocessing
### Preprocessor Macros - `GCC_PREPROCESSOR_DEFINITIONS` (StringList)
Space-separated list of preprocessor macros of the form `foo` or `foo=bar`.
Default value: **""**

| Command Line Argument |
| -------- |
| `-D$(value)` |


### Preprocessor Macros Not Used In Precompiled Headers - `GCC_PREPROCESSOR_DEFINITIONS_NOT_USED_IN_PRECOMPS` (StringList)
Space-separated list of preprocessor macros of the form `foo` or `foo=bar`. These macros are not used when precompiling a prefix header file.
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Enable Foundation Assertions - `ENABLE_NS_ASSERTIONS` (Boolean)
Controls whether assertion logic provided by `NSAssert` is included in the preprocessed source code or is elided during preprocessing. Disabling assertions can improve code performance.
File types: Objective-C, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-DNS_BLOCK_ASSERTIONS=1` |
| **`YES`** |  |



### Enable Strict Checking of objc_msgSend Calls - `ENABLE_STRICT_OBJC_MSGSEND` (Boolean)
Controls whether `objc_msgSend` calls must be cast to the appropriate function pointer type before being called.
File types: Objective-C, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-DOBJC_OLD_DISPATCH_PROTOTYPES=1` |
| `YES` | `-DOBJC_OLD_DISPATCH_PROTOTYPES=0` |





## Undefined Behavior Sanitizer
### Enable Extra Integer Checks - `CLANG_UNDEFINED_BEHAVIOR_SANITIZER_INTEGER` (Boolean)
Check for unsigned integer overflow, in addition to checks for signed integer overflow.
Condition: `$(CLANG_UNDEFINED_BEHAVIOR_SANITIZER) == YES`

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fsanitize=integer` |



### Enable Nullability Annotation Checks - `CLANG_UNDEFINED_BEHAVIOR_SANITIZER_NULLABILITY` (Boolean)
Check for violations of nullability annotations in function calls, return statements, and assignments.
Condition: `$(CLANG_UNDEFINED_BEHAVIOR_SANITIZER) == YES`

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-fsanitize=nullability` |





## Warnings - All languages
### Treat Missing Function Prototypes as Errors - `GCC_TREAT_IMPLICIT_FUNCTION_DECLARATIONS_AS_ERRORS` (Boolean)
Causes warnings about missing function prototypes to be treated as errors. Only applies to C and Objective-C.
File types: C, Objective-C

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Werror=implicit-function-declaration` |



### Treat Incompatible Pointer Type Warnings as Errors - `GCC_TREAT_INCOMPATIBLE_POINTER_TYPE_WARNINGS_AS_ERRORS` (Boolean)
Enabling this option causes warnings about incompatible pointer types to be treated as errors.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Werror=incompatible-pointer-types` |



### Missing Fields in Structure Initializers - `GCC_WARN_ABOUT_MISSING_FIELD_INITIALIZERS` (Boolean)
Warn if a structure's initializer has some fields missing. For example, the following code would cause such a warning because `x.h` is implicitly zero:

    struct s { int f, g, h; };
    struct s x = { 3, 4 };

This option does not warn about designated initializers, so the following modification would not trigger a warning:

    struct s { int f, g, h; };
    struct s x = { .f = 3, .g = 4 };

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-missing-field-initializers` |
| `YES` | `-Wmissing-field-initializers` |



### Missing Function Prototypes - `GCC_WARN_ABOUT_MISSING_PROTOTYPES` (Boolean)
Causes warnings to be emitted about missing prototypes.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-missing-prototypes` |
| `YES` | `-Wmissing-prototypes` |



### Mismatched Return Type - `GCC_WARN_ABOUT_RETURN_TYPE` (Enumeration)
Causes warnings to be emitted when a function with a defined return type (not `void`) contains a return statement without a return-value or when it does not contain any return statements. Also emits a warning when a function without a return type tries to return a value.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-return-type` |
| `YES` |  |
| `YES_ERROR` | `-Werror=return-type` |



### Documentation Comments - `CLANG_WARN_DOCUMENTATION_COMMENTS` (Boolean)
Warns about issues in documentation comments (`doxygen`-style) such as missing or incorrect documentation tags.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Wdocumentation` |



### Unreachable Code - `CLANG_WARN_UNREACHABLE_CODE` (Enumeration)
Warns about potentially unreachable code.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Wunreachable-code` |
| `YES_AGGRESSIVE` | `-Wunreachable-code-aggressive` |



### Quoted Include In Framework Header - `CLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER` (Enumeration)
Warns when a quoted include is used instead of a framework style include in a framework header.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Wquoted-include-in-framework-header` |
| `YES_ERROR` | `-Wquoted-include-in-framework-header -Werror=quoted-include-in-framework-header` |



### Typecheck Calls to printf/scanf - `GCC_WARN_TYPECHECK_CALLS_TO_PRINTF` (Boolean)
Check calls to `printf` and `scanf` to make sure that the arguments supplied have types appropriate to the format string specified, and that the conversions specified in the format string make sense.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-format` |
| **`YES`** |  |



### Initializer Not Fully Bracketed - `GCC_WARN_INITIALIZER_NOT_FULLY_BRACKETED` (Boolean)
Warn if an aggregate or union initializer is not fully bracketed. In the following example, the initializer for `a` is not fully bracketed, but the initializer for `b` is fully bracketed.

	int a[2][2] = { 0, 1, 2, 3 };
	int b[2][2] = { { 0, 1 }, { 2, 3 } };


| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-missing-braces` |
| `YES` | `-Wmissing-braces` |



### Missing Braces and Parentheses - `GCC_WARN_MISSING_PARENTHESES` (Boolean)
Warn if parentheses are omitted in certain contexts, such as when there is an assignment in a context where a truth value is expected, or when operators are nested whose precedence causes confusion. Also, warn about constructions where there may be confusion as to which `if` statement an `else` branch belongs. For example:

    {
      if (a)
        if (b)
          foo ();
      else
        bar ();
    }

In C, every `else` branch belongs to the innermost possible `if` statement, which in the example above is `if (b)`. This is often not what the programmer expects, as illustrated by indentation used in the example above. This build setting causes GCC to issue a warning when there is the potential for this confusion. To eliminate the warning, add explicit braces around the innermost `if` statement so there is no way the `else` could belong to the enclosing `if`. For example:

    {
      if (a)
        {
          if (b)
            foo ();
          else
            bar ();
        }
    }


| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-parentheses` |
| **`YES`** | `-Wparentheses` |



### Check Switch Statements - `GCC_WARN_CHECK_SWITCH_STATEMENTS` (Boolean)
Warn whenever a switch statement has an index of enumeral type and lacks a case for one or more of the named codes of that enumeration. The presence of a default label prevents this warning. Case labels outside the enumeration range also provoke warnings when this option is used.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-switch` |
| **`YES`** | `-Wswitch` |



### Unused Functions - `GCC_WARN_UNUSED_FUNCTION` (Boolean)
Warn whenever a static function is declared but not defined or a noninline static function is unused.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-unused-function` |
| `YES` | `-Wunused-function` |



### Unused Labels - `GCC_WARN_UNUSED_LABEL` (Boolean)
Warn whenever a label is declared but not used.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-unused-label` |
| `YES` | `-Wunused-label` |



### Empty Loop Bodies - `CLANG_WARN_EMPTY_BODY` (Boolean)
Warn about loop bodies that are suspiciously empty.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-empty-body` |
| `YES` | `-Wempty-body` |



### Uninitialized Variables - `GCC_WARN_UNINITIALIZED_AUTOS` (Enumeration)
Warn if a variable might be clobbered by a `setjmp` call or if an automatic variable is used without prior initialization.

The compiler may not detect all cases where an automatic variable is initialized or all usage patterns that may lead to use prior to initialization. You can toggle between the normal uninitialized value checking or the more aggressive (conservative) checking, which finds more issues but the checking is much stricter.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-uninitialized` |
| `YES` | `-Wuninitialized` |
| `YES_AGGRESSIVE` | `-Wuninitialized -Wconditional-uninitialized` |



### Unknown Pragma - `GCC_WARN_UNKNOWN_PRAGMAS` (Boolean)
Warn when a `#pragma` directive is encountered that is not understood by GCC. If this command line option is used, warnings will even be issued for unknown pragmas in system header files. This is not the case if the warnings were only enabled by the `-Wall` command-line option.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-unknown-pragmas` |
| `YES` | `-Wunknown-pragmas` |



### Hidden Local Variables - `GCC_WARN_SHADOW` (Boolean)
Warn whenever a local variable shadows another local variable, parameter or global variable or whenever a builtin function is shadowed.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-shadow` |
| `YES` | `-Wshadow` |



### Four Character Literals - `GCC_WARN_FOUR_CHARACTER_CONSTANTS` (Boolean)
Warn about four-char literals (for example, macOS-style `OSTypes`: `'APPL'`).

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-four-char-constants` |
| `YES` | `-Wfour-char-constants` |



### Suspicious Implicit Conversions - `CLANG_WARN_SUSPICIOUS_IMPLICIT_CONVERSION` (Enumeration)
Warn about various implicit conversions that can lose information or are otherwise suspicious.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-conversion` |
| `YES` | `-Wconversion` |
| `YES_ERROR` | `-Werror=conversion` |



### Implicit Constant Conversions - `CLANG_WARN_CONSTANT_CONVERSION` (Enumeration)
Warn about implicit conversions of constant values that cause the constant value to change, either through a loss of precision, or entirely in its meaning.
Default value: **`$(CLANG_WARN_SUSPICIOUS_IMPLICIT_CONVERSION)`**

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-constant-conversion` |
| `YES` | `-Wconstant-conversion` |
| `YES_ERROR` | `-Werror=constant-conversion` |



### Implicit Integer to Pointer Conversions - `CLANG_WARN_INT_CONVERSION` (Enumeration)
Warn about implicit conversions between pointers and integers. For example, this can catch issues when one incorrectly intermixes using `NSNumber*`'s and raw integers.
Default value: **`$(CLANG_WARN_SUSPICIOUS_IMPLICIT_CONVERSION)`**

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-int-conversion` |
| `YES` | `-Wint-conversion` |
| `YES_ERROR` | `-Werror=int-conversion` |



### Implicit Boolean Conversions - `CLANG_WARN_BOOL_CONVERSION` (Enumeration)
Warn about implicit conversions to boolean values that are suspicious. For example, writing `if (foo)` where `foo` is the name a function will trigger a warning.
Default value: **`$(CLANG_WARN_SUSPICIOUS_IMPLICIT_CONVERSION)`**

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-bool-conversion` |
| `YES` | `-Wbool-conversion` |
| `YES_ERROR` | `-Werror=bool-conversion` |



### Implicit Enum Conversions - `CLANG_WARN_ENUM_CONVERSION` (Enumeration)
Warn about implicit conversions between different kinds of enum values. For example, this can catch issues when using the wrong enum flag as an argument to a function or method.
Default value: **`$(CLANG_WARN_SUSPICIOUS_IMPLICIT_CONVERSION)`**

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-enum-conversion` |
| `YES` | `-Wenum-conversion` |
| `YES_ERROR` | `-Werror=enum-conversion` |



### Implicit Float Conversions - `CLANG_WARN_FLOAT_CONVERSION` (Enumeration)
Warn about implicit conversions that turn floating-point numbers into integers.
Default value: **`$(CLANG_WARN_SUSPICIOUS_IMPLICIT_CONVERSION)`**

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-float-conversion` |
| `YES` | `-Wfloat-conversion` |
| `YES_ERROR` | `-Werror=float-conversion` |



### Implicit Non-Literal Null Conversions - `CLANG_WARN_NON_LITERAL_NULL_CONVERSION` (Enumeration)
Warn about non-literal expressions that evaluate to zero being treated as a null pointer.
Default value: **`$(CLANG_WARN_SUSPICIOUS_IMPLICIT_CONVERSION)`**

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-non-literal-null-conversion` |
| `YES` | `-Wnon-literal-null-conversion` |
| `YES_ERROR` | `-Werror=non-literal-null-conversion` |



### Suspicious Pragma Pack - `CLANG_WARN_PRAGMA_PACK` (Enumeration)
Warn when a translation unit is missing terminating '#pragma pack (pop)' directives or when the '#pragma pack' state immediately after an #include is different from the state immediately before.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-pragma-pack` |
| **`YES`** |  |
| `YES_ERROR` | `-Werror=pragma-pack` |



### Outdated Private Module Map - `CLANG_WARN_PRIVATE_MODULE` (Boolean)
Warn about private modules that do not use the recommended private module layout.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-private-module` |
| **`YES`** |  |



### Out-of-Range Enum Assignments - `CLANG_WARN_ASSIGN_ENUM` (Boolean)
Warn about assigning integer constants to enum values that are out of the range of the enumerated type.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Wassign-enum` |



### Sign Comparison - `GCC_WARN_SIGN_COMPARE` (Boolean)
Warn when a comparison between signed and unsigned values could produce an incorrect result when the signed value is converted to unsigned.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Wsign-compare` |



### Unused Parameters - `GCC_WARN_UNUSED_PARAMETER` (Boolean)
Warn whenever a function parameter is unused aside from its declaration.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-unused-parameter` |
| `YES` | `-Wunused-parameter` |



### Unused Variables - `GCC_WARN_UNUSED_VARIABLE` (Boolean)
Warn whenever a local variable or nonconstant static variable is unused aside from its declaration.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-unused-variable` |
| `YES` | `-Wunused-variable` |



### Unused Values - `GCC_WARN_UNUSED_VALUE` (Boolean)
Warn whenever a statement computes a result that is explicitly not used.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-unused-value` |
| **`YES`** | `-Wunused-value` |



### Deprecated Functions - `GCC_WARN_ABOUT_DEPRECATED_FUNCTIONS` (Boolean)
Warn about the use of deprecated functions, variables, and types (as indicated by the `deprecated` attribute).

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-deprecated-declarations` |
| **`YES`** | `-Wdeprecated-declarations` |



### Pointer Sign Comparison - `GCC_WARN_ABOUT_POINTER_SIGNEDNESS` (Boolean)
Warn when pointers passed via arguments or assigned to a variable differ in sign.
File types: C, Objective-C

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-pointer-sign` |
| **`YES`** | `-Wpointer-sign` |



### Missing Newline At End Of File - `GCC_WARN_ABOUT_MISSING_NEWLINE` (Boolean)
Warn when a source file does not end with a newline.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-newline-eof` |
| `YES` | `-Wnewline-eof` |



### Implicit Signedness Conversions - `CLANG_WARN_IMPLICIT_SIGN_CONVERSION` (Enumeration)
Warn about implicit integer conversions that change the signedness of an integer value.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-sign-conversion` |
| `YES` | `-Wsign-conversion` |
| `YES_ERROR` | `-Werror=sign-conversion` |



### Implicit Conversion to 32 Bit Type - `GCC_WARN_64_TO_32_BIT_CONVERSION` (Enumeration)
Warn if a value is implicitly converted from a 64-bit type to a 32-bit type. This is a subset of the warnings provided by -Wconversion.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-shorten-64-to-32` |
| `YES` | `-Wshorten-64-to-32` |
| `YES_ERROR` | `-Werror=shorten-64-to-32` |



### Infinite Recursion - `CLANG_WARN_INFINITE_RECURSION` (Boolean)
Warn if all paths through a function call itself.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-infinite-recursion` |
| `YES` | `-Winfinite-recursion` |



### Suspicious Commas - `CLANG_WARN_COMMA` (Enumeration)
Warn about suspicious uses of the comma operator.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-comma` |
| `YES` | `-Wcomma` |
| `YES_ERROR` | `-Werror=comma` |



### Block Capture of Autoreleasing - `CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING` (Enumeration)
Warn about block captures of implicitly autoreleasing parameters.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-block-capture-autoreleasing` |
| `YES` | `-Wblock-capture-autoreleasing` |
| `YES_ERROR` | `-Werror=block-capture-autoreleasing` |



### Strict Prototypes - `CLANG_WARN_STRICT_PROTOTYPES` (Enumeration)
Warn about non-prototype declarations.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-strict-prototypes` |
| `YES` | `-Wstrict-prototypes` |
| `YES_ERROR` | `-Werror=strict-prototypes` |



### Semicolon Before Method Body - `CLANG_WARN_SEMICOLON_BEFORE_METHOD_BODY` (Boolean)
Warn about ignored semicolon between a method implementation's signature and body.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-semicolon-before-method-body` |
| `YES` | `-Wsemicolon-before-method-body` |



### Unguarded availability - `CLANG_WARN_UNGUARDED_AVAILABILITY` (Enumeration)
Warn if an API that is newer than the deployment target is used without "if (@available(...))" guards.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-unguarded-availability` |
| **`YES`** |  |
| `YES_AGGRESSIVE` | `-Wunguarded-availability` |





## Warnings - C++
### Nonvirtual Destructor - `GCC_WARN_NON_VIRTUAL_DESTRUCTOR` (Boolean)
Warn when a class declares an nonvirtual destructor that should probably be virtual, because it looks like the class will be used polymorphically. This is only active for C++ or Objective-C++ sources.
File types: C++, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-non-virtual-dtor` |
| `YES` | `-Wnon-virtual-dtor` |



### Overloaded Virtual Functions - `GCC_WARN_HIDDEN_VIRTUAL_FUNCTIONS` (Boolean)
Warn when a function declaration hides virtual functions from a base class.

For example, in the following example, the `A` class version of `f()` is hidden in `B`.

	struct A {
	  virtual void f();
	};

	struct B: public A {
	  void f(int);
	};

As a result, the following code will fail to compile.

	B* b;
	b->f();

This setting only applies to C++ and Objective-C++ sources.
File types: C++, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-overloaded-virtual` |
| `YES` | `-Woverloaded-virtual` |



### Exit-Time C++ Destructors - `CLANG_WARN__EXIT_TIME_DESTRUCTORS` (Boolean)
Warn about destructors for C++ objects that are called when an application is terminating.
File types: C++, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-exit-time-destructors` |
| `YES` | `-Wexit-time-destructors` |



### Ambiguous C++ Parsing Situation - `CLANG_WARN_VEXING_PARSE` (Enumeration)
Warn about a parsing ambiguity between a variable declaration and a function-style cast.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-vexing-parse` |
| **`YES`** |  |
| `YES_ERROR` | `-Werror=vexing-parse` |



### Deleting Instance of Polymorphic Class with No Virtual Destructor - `CLANG_WARN_DELETE_NON_VIRTUAL_DTOR` (Enumeration)
Warn when deleting an instance of a polymorphic class with virtual functions but without a virtual destructor.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-delete-non-virtual-dtor` |
| **`YES`** |  |
| `YES_ERROR` | `-Werror=delete-non-virtual-dtor` |



### Using C++11 extensions in earlier versions of C++ - `CLANG_WARN_CXX0X_EXTENSIONS` (Boolean)
When compiling C++ code using a language standard older than C++11, warn about the use of C++11 extensions.
File types: C++, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-c++11-extensions` |
| `YES` | `-Wc++11-extensions` |



### Usage of implicit sequentially-consistent atomics - `CLANG_WARN_ATOMIC_IMPLICIT_SEQ_CST` (Boolean)
Warns when an atomic is used with an implicitly sequentially-consistent memory order, instead of explicitly specifying memory order.
File types: C, Objective-C, C++, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Watomic-implicit-seq-cst` |



### Undefined Use of offsetof Macro - `GCC_WARN_ABOUT_INVALID_OFFSETOF_MACRO` (Boolean)
Unchecking this setting will suppress warnings from applying the `offsetof` macro to a non-POD type. According to the 1998 ISO C++ standard, applying `offsetof` to a non-POD type is undefined. In existing C++ implementations, however, `offsetof` typically gives meaningful results even when applied to certain kinds of non-POD types, such as a simple struct that fails to be a POD type only by virtue of having a constructor. This flag is for users who are aware that they are writing nonportable code and who have deliberately chosen to ignore the warning about it.

The restrictions on `offsetof` may be relaxed in a future version of the C++ standard.
File types: C++, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-invalid-offsetof` |
| **`YES`** | `-Winvalid-offsetof` |



### Suspicious Moves - `CLANG_WARN_SUSPICIOUS_MOVE` (Boolean)
Warn about suspicious uses of `std::move`.
File types: C++, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-move` |
| `YES` | `-Wmove` |



### Range-based For Loops - `CLANG_WARN_RANGE_LOOP_ANALYSIS` (Boolean)
Warn about ranged-based for loops.
File types: C++, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-range-loop-analysis` |
| `YES` | `-Wrange-loop-analysis` |





## Warnings - Objective-C
### Implicit Atomic Objective-C Properties - `CLANG_WARN_OBJC_IMPLICIT_ATOMIC_PROPERTIES` (Boolean)
Warn about `@property` declarations that are implicitly atomic.
File types: Objective-C, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-implicit-atomic-properties` |
| `YES` | `-Wimplicit-atomic-properties` |



### Direct usage of 'isa' - `CLANG_WARN_DIRECT_OBJC_ISA_USAGE` (Enumeration)
Warn about direct accesses to the Objective-C `isa` pointer instead of using a runtime API.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-deprecated-objc-isa-usage` |
| **`YES`** |  |
| `YES_ERROR` | `-Werror=deprecated-objc-isa-usage` |



### Interface Declarations of Instance Variables - `CLANG_WARN_OBJC_INTERFACE_IVARS` (Enumeration)
Warn about instance variable declarations in `@interface`.
File types: Objective-C, Objective-C++

| Enumeration value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-objc-interface-ivars` |
| `YES` | `-Wobjc-interface-ivars` |
| `YES_ERROR` | `-Werror=objc-interface-ivars` |



### Implicit Synthesized Properties - `CLANG_WARN_OBJC_MISSING_PROPERTY_SYNTHESIS` (Boolean)
Starting in Xcode 4.4, Apple Clang will implicitly synthesize properties that are not explicitly synthesized using `@synthesize`. This setting warns about such implicit behavior, even though the property is still synthesized. This is essentially a backwards compatibility warning, or for those who wish to continue to explicitly use `@synthesize`.
File types: Objective-C, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Wobjc-missing-property-synthesis` |



### Unintentional Root Class - `CLANG_WARN_OBJC_ROOT_CLASS` (Enumeration)
Warn about classes that unintentionally do not subclass a root class, such as `NSObject`.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-objc-root-class` |
| **`YES`** |  |
| `YES_ERROR` | `-Werror=objc-root-class` |



### Duplicate Method Definitions - `CLANG_WARN__DUPLICATE_METHOD_MATCH` (Boolean)
Warn about declaring the same method more than once within the same `@interface`.
File types: Objective-C, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Wduplicate-method-match` |



### Implicit Objective-C Literal Conversions - `CLANG_WARN_OBJC_LITERAL_CONVERSION` (Enumeration)
Warn about implicit conversions from Objective-C literals to values of incompatible type.
Default value: **`$(CLANG_WARN_SUSPICIOUS_IMPLICIT_CONVERSION)`**

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-objc-literal-conversion` |
| `YES` | `-Wobjc-literal-conversion` |
| `YES_ERROR` | `-Werror=objc-literal-conversion` |



### Missing Noescape Annotation - `CLANG_WARN_MISSING_NOESCAPE` (Enumeration)
Warn about noescape annotations that are missing in a method's signature.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-missing-noescape` |
| **`YES`** |  |
| `YES_ERROR` | `-Werror=missing-noescape` |



### Strict Selector Matching - `GCC_WARN_STRICT_SELECTOR_MATCH` (Boolean)
Warn if multiple methods with differing argument and/or return types are found for a given selector when attempting to send a message using this selector to a receiver of type `id` or `Class`. When this setting is disabled, the compiler will omit such warnings if any differences found are confined to types that share the same size and alignment.
File types: Objective-C, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-strict-selector-match` |
| `YES` | `-Wstrict-selector-match` |



### Undeclared Selector - `GCC_WARN_UNDECLARED_SELECTOR` (Boolean)
Warn if a `@selector(...)` expression referring to an undeclared selector is found. A selector is considered undeclared if no method with that name has been declared before the `@selector(...)` expression, either explicitly in an `@interface` or `@protocol` declaration, or implicitly in an `@implementation` section. This option always performs its checks as soon as a `@selector(...)` expression is found, while `-Wselector` only performs its checks in the final stage of compilation. This also enforces the coding style convention that methods and selectors must be declared before being used.
File types: Objective-C, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-undeclared-selector` |
| `YES` | `-Wundeclared-selector` |



### Overriding Deprecated Objective-C Methods - `CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS` (Boolean)
Warn if an Objective-C class either subclasses a deprecated class or overrides a method that has been marked deprecated or unavailable.
File types: Objective-C, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-deprecated-implementations` |
| `YES` | `-Wdeprecated-implementations` |



### Incomplete Objective-C Protocols - `GCC_WARN_ALLOW_INCOMPLETE_PROTOCOL` (Boolean)
Warn if methods required by a protocol are not implemented in the class adopting it. Only applies to Objective-C.
File types: Objective-C, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-protocol` |
| **`YES`** | `-Wprotocol` |





## Warnings - Objective-C and ARC
### Repeatedly using a __weak reference - `CLANG_WARN_OBJC_REPEATED_USE_OF_WEAK` (Enumeration)
Warn about repeatedly using a weak reference without assigning the weak reference to a strong reference. This is often symptomatic of a race condition where the weak reference can become `nil` between accesses, resulting in unexpected behavior. Assigning to temporary strong reference ensures the object stays alive during the related accesses.
File types: Objective-C, Objective-C++

| Enumeration value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Wno-arc-repeated-use-of-weak` |
| `YES` | `-Warc-repeated-use-of-weak -Wno-arc-maybe-repeated-use-of-weak` |
| `YES_AGGRESSIVE` | `-Warc-repeated-use-of-weak -Warc-maybe-repeated-use-of-weak` |



### Implicit ownership types on out parameters - `CLANG_WARN_OBJC_EXPLICIT_OWNERSHIP_TYPE` (Boolean)
Warn about implicit ownership types on Objective-C object references as out parameters. For example, declaring a parameter with type `NSObject**` will produce a warning because the compiler will assume that the out parameter's ownership type is `__autoreleasing`.
File types: Objective-C, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Wexplicit-ownership-type` |



### Implicit retain of 'self' within blocks - `CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF` (Boolean)
Warn about implicit retains of `self` within blocks, which can create a retain-cycle.
File types: Objective-C, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Wimplicit-retain-self` |



### Using __bridge Casts Outside of ARC - `CLANG_WARN__ARC_BRIDGE_CAST_NONARC` (Boolean)
Warn about using `__bridge` casts when not using ARC, where they have no effect.
File types: Objective-C, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Wno-arc-bridge-casts-disallowed-in-nonarc` |
| **`YES`** |  |





## Warning Policies
### Treat Warnings as Errors - `GCC_TREAT_WARNINGS_AS_ERRORS` (Boolean)
Enabling this option causes all warnings to be treated as errors.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Werror` |



### Inhibit All Warnings - `GCC_WARN_INHIBIT_ALL_WARNINGS` (Boolean)
Inhibit all warning messages.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-w` |



### Pedantic Warnings - `GCC_WARN_PEDANTIC` (Boolean)
Issue all the warnings demanded by strict ISO C and ISO C++; reject all programs that use forbidden extensions, and some other programs that do not follow ISO C and ISO C++. For ISO C, follows the version of the ISO C standard specified by any `-std` option used.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-pedantic` |





# Apple Clang
Apple Clang compiler

# Static Analyzer
Apple Clang Static Analyzer
File types: C, Objective-C, C++, Objective-C++
Source File Option: `--analyze`

Special meanings:
`$(value)` is replaced by the selected value or the default value.

## None
### `CLANG_ANALYZER_EXEC` (Path)
Default value: **`clang`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CLANG_INDEX_STORE_ENABLE` (Boolean)

| Command Line Argument |
| -------- |
| `` |


### `CLANG_ANALYZER_DEFINES` (String)
Default value: **`-D__clang_analyzer__`**

| Command Line Argument |
| -------- |
| `$(value)` |


### `CLANG_ANALYZER_OUTPUT_DIR` (Path)
Default value: **`$(TEMP_DIR)`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CLANG_ANALYZER_OUTPUT` (Enumeration)

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `default` |  |
| **`plist-multi-file`** | ``-Xclang -analyzer-output=plist-multi-file`` |



### `CLANG_ANALYZER_ALTERNATE_EDGES` (Boolean)

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-config -Xclang path-diagnostics-alternate=false` |
| **`YES`** | `-Xclang -analyzer-config -Xclang path-diagnostics-alternate=true` |



### `CLANG_ANALYZER_REPORT_MAIN_SOURCE_FILE` (Boolean)

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| **`YES`** | `-Xclang -analyzer-config -Xclang report-in-main-source-file=true` |



### `CLANG_STATIC_ANALYZER_MODE_ACTION_shallow` (String)
Default value: **`Shallow`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CLANG_STATIC_ANALYZER_MODE_ACTION_deep` (String)
Default value: **""**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CLANG_ANALYZER_MALLOC` (Boolean)
Default value: **`YES`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### *EXPERIMENTAL* Buffer overflows - `CLANG_ANALYZER_SECURITY_BUFFER_OVERFLOW_EXPERIMENTAL` (Boolean)
Check for potential buffer overflows.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Xclang -analyzer-checker -Xclang core.experimental.Overflow -Xclang -analyzer-checker -Xclang security.experimental.ArrayBoundV2 -Xclang -analyzer-max-loop -Xclang 100` |



### `CLANG_ANALYZER_OTHER_CHECKERS` (StringList)
File types: C, Objective-C, C++, Objective-C++

| Command Line Argument |
| -------- |
| `-Xclang -analyzer-checker -Xclang $(value)` |


### `CLANG_ANALYZER_OTHER_FLAGS` (StringList)
File types: C, Objective-C, C++, Objective-C++

| Command Line Argument |
| -------- |
| `-Xclang $(value)` |




## Issues - Apple APIs
### Misuse of Collections API - `CLANG_ANALYZER_OBJC_COLLECTIONS` (Boolean)
Warn if `CF` collections are created with non-pointer-size values. Check if `NS` collections are initialized with non-Objective-C type elements.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-disable-checker -Xclang osx.coreFoundation.containers.PointerSizedValues -Xclang -analyzer-disable-checker -Xclang osx.cocoa.VariadicMethodTypes -Xclang -analyzer-disable-checker -Xclang osx.cocoa.NilArg` |
| **`YES`** |  |



### Improper Handling of CFError and NSError - `CLANG_ANALYZER_OBJC_NSCFERROR` (Boolean)
Warn if functions accepting `CFErrorRef` or `NSError` cannot indicate that an error occurred.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-disable-checker -Xclang osx.coreFoundation.CFError -Xclang -analyzer-disable-checker -Xclang osx.cocoa.NSError` |
| **`YES`** |  |



### Misuse of Grand Central Dispatch - `CLANG_ANALYZER_GCD` (Boolean)
Check for misuses of the Grand Central Dispatch API.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-disable-checker -Xclang osx.API` |
| **`YES`** |  |



### Suspicious Conversions of NSNumber and CFNumberRef - `CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION` (Enumeration)
Warn when a number object, such as an instance of `NSNumber`, `CFNumberRef`, `OSNumber`, or `OSBoolean` is compared or converted to a primitive value instead of another object.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-disable-checker -Xclang osx.NumberObjectConversion` |
| **`YES`** |  |
| `YES_AGGRESSIVE` | `-Xclang -analyzer-config -Xclang osx.NumberObjectConversion:Pedantic=true` |



### Missing Localizability - `CLANG_ANALYZER_LOCALIZABILITY_NONLOCALIZED` (Enumeration)
Warn when a nonlocalized string is passed to a user interface method expecting a localized string.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Xclang -analyzer-checker -Xclang optin.osx.cocoa.localizability.NonLocalizedStringChecker` |



### Missing Localization Context Comment - `CLANG_ANALYZER_LOCALIZABILITY_EMPTY_CONTEXT` (Enumeration)
Warn when a call to an `NSLocalizedString()` macro is missing a context comment for the localizer.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Xclang -analyzer-checker -Xclang optin.osx.cocoa.localizability.EmptyLocalizationContextChecker` |



### Performance Anti-Patterns with Grand Central Dispatch - `CLANG_ANALYZER_GCD_PERFORMANCE` (Enumeration)
Check for Grand Central Dispatch idioms that may lead to poor performance.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Xclang -analyzer-checker -Xclang optin.performance.GCDAntipattern` |



### Violation of IOKit and libkern Reference Counting Rules - `CLANG_ANALYZER_LIBKERN_RETAIN_COUNT` (Boolean)
Finds leaks and overreleases associated with objects inheriting from OSObject

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-config -Xclang osx.cocoa.RetainCount:CheckOSObject=false` |
| **`YES`** |  |





## Generic Issues
### Dead Stores - `CLANG_ANALYZER_DEADCODE_DEADSTORES` (Boolean)
Check for values stored to variables and never read again.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-disable-checker -Xclang deadcode.DeadStores` |
| **`YES`** |  |



### Improper Memory Management - `CLANG_ANALYZER_MEMORY_MANAGEMENT` (Boolean)
Warn about memory leaks, use-after-free, and other API misuses.
Default value: **`$(CLANG_ANALYZER_MALLOC)`**

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-disable-checker -Xclang unix.Malloc -Xclang -analyzer-disable-checker -Xclang unix.MallocSizeof -Xclang -analyzer-disable-checker -Xclang unix.MismatchedDeallocator -Xclang -analyzer-disable-checker -Xclang cplusplus.NewDelete` |
| `YES` |  |



### Misuse of 'nonnull' - `CLANG_ANALYZER_NONNULL` (Enumeration)
Check for misuses of `nonnull` parameter and return types.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-disable-checker -Xclang nullability` |
| `YES` |  |
| **`YES_NONAGGRESSIVE`** | `-Xclang -analyzer-config -Xclang nullability:NoDiagnoseCallsToSystemHeaders=true` |



### Use-After-Move Errors in C++ - `CLANG_ANALYZER_USE_AFTER_MOVE` (Enumeration)
Warn when a C++ object is used after it has been moved from.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-disable-checker -Xclang cplusplus.Move` |
| `YES` | `-Xclang -analyzer-config -Xclang cplusplus.Move:WarnOn=KnownsOnly` |
| **`YES_AGGRESSIVE`** |  |





## Issues - Objective-C
### Method Signatures Mismatch - `CLANG_ANALYZER_OBJC_INCOMP_METHOD_TYPES` (Boolean)
Warn about Objective-C method signatures with type incompatibilities.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-disable-checker -Xclang osx.cocoa.IncompatibleMethodTypes` |
| **`YES`** |  |



### Unused Ivars - `CLANG_ANALYZER_OBJC_UNUSED_IVARS` (Boolean)
Warn about private ivars that are never used.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-disable-checker -Xclang osx.cocoa.UnusedIvars` |
| **`YES`** |  |



### Misuse of Objective-C generics - `CLANG_ANALYZER_OBJC_GENERICS` (Boolean)
Warn if a specialized generic type is converted to an incompatible type.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-disable-checker -Xclang osx.cocoa.ObjCGenerics` |
| **`YES`** |  |



### Violation of Reference Counting Rules - `CLANG_ANALYZER_OBJC_RETAIN_COUNT` (Boolean)
Warn on leaks and improper reference count management.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-disable-checker -Xclang osx.cocoa.RetainCount -Xclang -analyzer-disable-checker -Xclang osx.cocoa.ClassRelease` |
| **`YES`** |  |



### @synchronized with nil mutex - `CLANG_ANALYZER_OBJC_ATSYNC` (Boolean)
Warn on `nil` pointers used as mutexes for `@synchronized`.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-disable-checker -Xclang osx.cocoa.AtSync` |
| **`YES`** |  |



### Improper Instance Cleanup in '-dealloc' - `CLANG_ANALYZER_OBJC_DEALLOC` (Boolean)
Warn when an instance is improperly cleaned up in `-dealloc`.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-disable-checker -Xclang osx.cocoa.Dealloc` |
| **`YES`** |  |



### Violation of 'self = [super init]' Rule - `CLANG_ANALYZER_OBJC_SELF_INIT` (Boolean)
Check that `super init` is properly called within an Objective-C initialization method.
File types: Objective-C, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-disable-checker -Xclang osx.cocoa.SelfInit` |
| **`YES`** |  |





## Analysis Policy
### Analyze During 'Build' - `RUN_CLANG_STATIC_ANALYZER` (Boolean)
Activating this setting will cause Xcode to run the `Clang` static analysis tool on qualifying source files during every build.
Default value: **`NO`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### Mode of Analysis for 'Build' - `CLANG_STATIC_ANALYZER_MODE` (Enumeration)
The depth the static analyzer uses during the Build action. Use `Deep` to exercise the full power of the analyzer. Use `Shallow` for faster analysis.

| Enumeration value | Command Line Argument |
| ----- | -------- |
| `deep` |  |
| **`shallow`** | `-Xclang -analyzer-config -Xclang mode=shallow` |



### Mode of Analysis for 'Analyze' - `CLANG_STATIC_ANALYZER_MODE_ON_ANALYZE_ACTION` (Enumeration)
The depth the static analyzer uses during the Analyze action. Use `Deep` to exercise the full power of the analyzer. Use `Shallow` for faster analysis.

| Enumeration value |
| -------- |
| `shallow` |
| **`deep`** |

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.




## Issues - Security
### Misuse of Keychain Services API - `CLANG_ANALYZER_SECURITY_KEYCHAIN_API` (Boolean)
Check for leaks of keychain attribute lists and data buffers returned by the Keychain Services API.
File types: Objective-C, Objective-C++

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-disable-checker -Xclang osx.SecKeychainAPI` |
| **`YES`** |  |



### Floating Point Value Used as Loop Counter - `CLANG_ANALYZER_SECURITY_FLOATLOOPCOUNTER` (Boolean)
Warn on using a floating point value as a loop counter (CERT: FLP30-C, FLP30-CPP).

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-Xclang -analyzer-checker -Xclang security.FloatLoopCounter` |



### Unchecked Return Values - `CLANG_ANALYZER_SECURITY_INSECUREAPI_UNCHECKEDRETURN` (Boolean)
Warn on uses of sensitive functions whose return values must be always checked.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-disable-checker -Xclang security.insecureAPI.UncheckedReturn` |
| **`YES`** | `-Xclang -analyzer-checker -Xclang security.insecureAPI.UncheckedReturn` |



### Use of 'getpw', 'gets' (Buffer Overflow) - `CLANG_ANALYZER_SECURITY_INSECUREAPI_GETPW_GETS` (Boolean)
Warn on uses of `getpw` and `gets`. The functions are dangerous as they may trigger a buffer overflow.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-disable-checker -Xclang security.insecureAPI.getpw -Xclang -analyzer-disable-checker -Xclang security.insecureAPI.gets` |
| **`YES`** | `-Xclang -analyzer-checker -Xclang security.insecureAPI.getpw -Xclang -analyzer-checker -Xclang security.insecureAPI.gets` |



### Use of 'mktemp' or Predictable 'mktemps' - `CLANG_ANALYZER_SECURITY_INSECUREAPI_MKSTEMP` (Boolean)
Warn on uses of `mktemp`, which produces predictable temporary files. It is obsoleted by `mktemps`. Warn when `mkstemp` is passed fewer than 6 `X`'s in the format string.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-disable-checker -Xclang security.insecureAPI.mkstemp -Xclang -analyzer-disable-checker -Xclang security.insecureAPI.mktemp` |
| **`YES`** | `-Xclang -analyzer-checker -Xclang security.insecureAPI.mkstemp -Xclang -analyzer-checker -Xclang security.insecureAPI.mktemp` |



### Use of 'rand' Functions - `CLANG_ANALYZER_SECURITY_INSECUREAPI_RAND` (Boolean)
Warn on uses of `rand`, `random`, and related functions, which produce predictable random number sequences. Use `arc4random` instead.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Xclang -analyzer-disable-checker -Xclang security.insecureAPI.rand` |
| `YES` | `-Xclang -analyzer-checker -Xclang security.insecureAPI.rand` |



### Use of 'strcpy' and 'strcat' - `CLANG_ANALYZER_SECURITY_INSECUREAPI_STRCPY` (Boolean)
Warn on uses of the `strcpy` and `strcat` functions, which can result in buffer overflows. Use `strlcpy` or `strlcat` instead.

| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** | `-Xclang -analyzer-disable-checker -Xclang security.insecureAPI.strcpy` |
| `YES` | `-Xclang -analyzer-checker -Xclang security.insecureAPI.strcpy` |



### Use of 'vfork' - `CLANG_ANALYZER_SECURITY_INSECUREAPI_VFORK` (Boolean)
Warn on uses of the `vfork` function, which is inherently insecure. Use the safer `posix_spawn` function instead.

| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` | `-Xclang -analyzer-disable-checker -Xclang security.insecureAPI.vfork` |
| **`YES`** | `-Xclang -analyzer-checker -Xclang security.insecureAPI.vfork` |





# ObjC Migrator
Apple Clang ObjC Migrator
File types: Objective-C, Objective-C++
Source File Option: `--migrate`

Special meanings:
`$(value)` is replaced by the selected value or the default value.

## Modernizer
### Infer readwrite properties - `CLANG_MIGRATOR_READWRITE_PROPERTY` (Boolean)
Infer readwrite properties from a getter and setter method.


| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| **`YES`** | `-objcmt-migrate-readwrite-property` |



### Infer readonly properties - `CLANG_MIGRATOR_READONLY_PROPERTY` (Boolean)
Infer readonly properties from getter methods.


| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| **`YES`** | `-objcmt-migrate-readonly-property` |



### Add attribute annotations - `CLANG_MIGRATOR_ANNOTATIONS` (Boolean)
Add attribute annotations to properties and methods.


| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| **`YES`** | `-objcmt-migrate-annotation` |



### Infer instancetype for method result type - `CLANG_MIGRATOR_INSTANCE_TYPE` (Boolean)
Infer `instancetype` for method result type instead of `id`.


| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| **`YES`** | `-objcmt-migrate-instancetype` |



### Use NS_ENUM/NS_OPTIONS macros - `CLANG_MIGRATOR_NSENUM_MACROS` (Boolean)
Use `NS_ENUM`/`NS_OPTIONS` macros for enumerators.


| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| **`YES`** | `-objcmt-migrate-ns-macros` |



### Infer protocol conformance - `CLANG_MIGRATOR_PROTOCOL_CONFORMANCE` (Boolean)
Infer protocol conformance from the interface methods.


| Boolean value | Command Line Argument |
| ----- | -------- |
| **`NO`** |  |
| `YES` | `-objcmt-migrate-protocol-conformance` |



### Atomicity of inferred properties - `CLANG_MIGRATOR_PROPERTY_ATOMICITY` (Enumeration)
Choose the atomicity of the inferred properties.


| Enumeration value | Command Line Argument |
| ----- | -------- |
| **`NS_NONATOMIC_IOSONLY`** | `-objcmt-ns-nonatomic-iosonly` |
| `atomic` | `-objcmt-atomic-property` |
| `nonatomic` |  |



### Only modify public headers - `CLANG_MIGRATOR_PUBLIC_HEADERS_ONLY` (Boolean)
Only modify public headers of a target.


| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| **`YES`** | `-objcmt-white-list-dir-path=$(TARGET_BUILD_DIR)/$(PUBLIC_HEADERS_FOLDER_PATH)` |



### ObjC literals - `CLANG_MIGRATOR_OBJC_LITERALS` (Boolean)
Enable migration to modern ObjC literals syntax.


| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| **`YES`** | `-objcmt-migrate-literals -Qunused-arguments` |



### ObjC property-dot syntax - `CLANG_MIGRATOR_PROPERTY_DOT_SYNTAX` (Boolean)
Enable migration of setter/getter messages to property-dot syntax.


| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| **`YES`** | `-objcmt-migrate-property-dot-syntax` |



### ObjC subscripting - `CLANG_MIGRATOR_OBJC_SUBSCRIPTING` (Boolean)
Enable migration to modern ObjC subscripting syntax.


| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| **`YES`** | `-objcmt-migrate-subscripting -Qunused-arguments` |



### Infer designated initializer methods - `CLANG_MIGRATOR_OBJC_DESIGNATED_INIT` (Boolean)
Infer `NS_DESIGNATED_INITIALIZER` for designated initializer methods.


| Boolean value | Command Line Argument |
| ----- | -------- |
| `NO` |  |
| **`YES`** | `-objcmt-migrate-designated-init -Qunused-arguments` |





## None
### `CLANG` (Path)
Default value: **`clang`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CLANG_INDEX_STORE_ENABLE` (Boolean)

| Command Line Argument |
| -------- |
| `` |




# XCTest Migrator
Apple Clang XCTest Migrator
File types: Objective-C, Objective-C++
Source File Option: `--migrate-xct`

Special meanings:
`$(value)` is replaced by the selected value or the default value.

## None
### `CLANG` (Path)
Default value: **`clang`**

The option only sets an internal value, which is used by other options as a condition or as an internal parameter.


### `CLANG_INDEX_STORE_ENABLE` (Boolean)

| Command Line Argument |
| -------- |
| `` |




# AST Builder
Apple Clang AST Builder 9.0
File types: C, Objective-C, C++, Objective-C++
Source File Option: `-fsyntax-only`

| Overriding Properties | Value |
| -------- | --------  |
| `CLANG_RETAIN_COMMENTS_FROM_SYSTEM_HEADERS` | `YES` |
| `CLEAN_PRECOMPS` | `NO` |
| `ENABLE_HEADER_DEPENDENCIES` | `YES` |
| `SHARED_PRECOMPS_DIR` | `$(INDEX_PRECOMPS_DIR)` |

