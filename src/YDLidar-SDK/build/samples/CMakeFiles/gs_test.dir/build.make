# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/bi/dev_ws/src/YDLidar-SDK

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/bi/dev_ws/src/YDLidar-SDK/build

# Include any dependencies generated for this target.
include samples/CMakeFiles/gs_test.dir/depend.make

# Include the progress variables for this target.
include samples/CMakeFiles/gs_test.dir/progress.make

# Include the compile flags for this target's objects.
include samples/CMakeFiles/gs_test.dir/flags.make

samples/CMakeFiles/gs_test.dir/gs_test.cpp.o: samples/CMakeFiles/gs_test.dir/flags.make
samples/CMakeFiles/gs_test.dir/gs_test.cpp.o: ../samples/gs_test.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/bi/dev_ws/src/YDLidar-SDK/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object samples/CMakeFiles/gs_test.dir/gs_test.cpp.o"
	cd /home/bi/dev_ws/src/YDLidar-SDK/build/samples && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/gs_test.dir/gs_test.cpp.o -c /home/bi/dev_ws/src/YDLidar-SDK/samples/gs_test.cpp

samples/CMakeFiles/gs_test.dir/gs_test.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gs_test.dir/gs_test.cpp.i"
	cd /home/bi/dev_ws/src/YDLidar-SDK/build/samples && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/bi/dev_ws/src/YDLidar-SDK/samples/gs_test.cpp > CMakeFiles/gs_test.dir/gs_test.cpp.i

samples/CMakeFiles/gs_test.dir/gs_test.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gs_test.dir/gs_test.cpp.s"
	cd /home/bi/dev_ws/src/YDLidar-SDK/build/samples && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/bi/dev_ws/src/YDLidar-SDK/samples/gs_test.cpp -o CMakeFiles/gs_test.dir/gs_test.cpp.s

# Object files for target gs_test
gs_test_OBJECTS = \
"CMakeFiles/gs_test.dir/gs_test.cpp.o"

# External object files for target gs_test
gs_test_EXTERNAL_OBJECTS =

gs_test: samples/CMakeFiles/gs_test.dir/gs_test.cpp.o
gs_test: samples/CMakeFiles/gs_test.dir/build.make
gs_test: libydlidar_sdk.a
gs_test: samples/CMakeFiles/gs_test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/bi/dev_ws/src/YDLidar-SDK/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../gs_test"
	cd /home/bi/dev_ws/src/YDLidar-SDK/build/samples && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/gs_test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
samples/CMakeFiles/gs_test.dir/build: gs_test

.PHONY : samples/CMakeFiles/gs_test.dir/build

samples/CMakeFiles/gs_test.dir/clean:
	cd /home/bi/dev_ws/src/YDLidar-SDK/build/samples && $(CMAKE_COMMAND) -P CMakeFiles/gs_test.dir/cmake_clean.cmake
.PHONY : samples/CMakeFiles/gs_test.dir/clean

samples/CMakeFiles/gs_test.dir/depend:
	cd /home/bi/dev_ws/src/YDLidar-SDK/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/bi/dev_ws/src/YDLidar-SDK /home/bi/dev_ws/src/YDLidar-SDK/samples /home/bi/dev_ws/src/YDLidar-SDK/build /home/bi/dev_ws/src/YDLidar-SDK/build/samples /home/bi/dev_ws/src/YDLidar-SDK/build/samples/CMakeFiles/gs_test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : samples/CMakeFiles/gs_test.dir/depend

