cmake_minimum_required(VERSION 3.10)
project(MonkGame)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Detect OS and set platform-specific options
if (WIN32)
    message("Building for Windows")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DWIN32")
elseif (APPLE)
    message("Building for macOS")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DAPPLE")
elseif (UNIX)
    message("Building for Linux")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DUNIX")
endif()

# Include all source files
set(SOURCES 
    src/main.cpp
    src/game.cpp
    src/monk.cpp
    src/dungeon.cpp
    src/combat.cpp
    src/room.cpp
    src/utils.cpp
)

# Include directories
include_directories(src)

# Define executable
add_executable(MonkGame ${SOURCES})
