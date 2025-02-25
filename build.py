import os
import subprocess
import platform
import sys

def run_command(command, cwd=None):
    """Helper function to run shell commands."""
    try:
        result = subprocess.run(command, cwd=cwd, check=True, shell=True)
        print(f"Command {' '.join(command)} executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(command)}")
        sys.exit(1)

def cmake_build():
    """Run cmake and build the project based on the operating system."""
    # Get the current platform
    current_platform = platform.system().lower()

    # Path to your source directory (assuming it's the current directory for this script)
    source_dir = os.getcwd()

    # Create a build directory
    build_dir = os.path.join(source_dir, "build")
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    # Run CMake command to configure the project
    if current_platform == "windows":
        # On Windows, use 'cmake' to generate Visual Studio project files
        cmake_command = ["cmake", "-G", "Visual Studio 16 2019", source_dir]
    elif current_platform == "darwin":  # macOS
        cmake_command = ["cmake", "-G", "Unix Makefiles", source_dir]
    elif current_platform == "linux":
        cmake_command = ["cmake", "-G", "Unix Makefiles", source_dir]
    else:
        print("Unsupported platform")
        sys.exit(1)

    run_command(cmake_command, cwd=build_dir)

    # Run the build command
    if current_platform == "windows":
        # On Windows, build using Visual Studio
        build_command = ["cmake", "--build", ".", "--config", "Release"]
    else:
        # On Linux and macOS, use make
        build_command = ["make"]

    run_command(build_command, cwd=build_dir)

    # Run the executable
    executable_name = "MonkGame" 
    executable_path = os.path.join(build_dir, "Release", executable_name) if current_platform == "windows" else os.path.join(build_dir, executable_name)

    if os.path.exists(executable_path):
        print(f"Running the executable: {executable_path}")
        run_command([f'"{executable_path}"'])

if __name__ == "__main__":
    cmake_build()
