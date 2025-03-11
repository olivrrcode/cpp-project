import os
import subprocess
import platform
import sys

def get_vs_generator():
    """Detect installed Visual Studio version"""
    vs_versions = [
        ("2022", "Visual Studio 17 2022"),
        ("2019", "Visual Studio 16 2019"),
        ("2017", "Visual Studio 15 2017")
    ]
    
    for year, generator in vs_versions:
        try:
            subprocess.run(f'cmake --help | findstr "{generator}"', shell=True, check=True)
            return generator
        except subprocess.CalledProcessError:
            continue
    
    print("Error: No compatible Visual Studio version found!")
    print("Please install Visual Studio 2017, 2019, or 2022 with C++ development tools")
    sys.exit(1)

def run_command(command, cwd=None):
    """Helper function to run shell commands."""
    try:
        if isinstance(command, list):
            command = " ".join(command)
        
        # Use shell=True for Windows commands
        result = subprocess.run(command, cwd=cwd, check=True, shell=True, 
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Error output: {e.stderr}")
        sys.exit(1)

def cmake_build():
    """Run cmake and build the project based on the operating system."""
    current_platform = platform.system().lower()
    source_dir = os.getcwd()
    build_dir = os.path.join(source_dir, "build")
    
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    if current_platform == "windows":
        generator = get_vs_generator()
        cmake_command = f'cmake -G "{generator}" -A x64 "{source_dir}"'
        run_command(cmake_command, cwd=build_dir)
        
        # Build using CMake --build
        build_command = 'cmake --build . --config Release'
        run_command(build_command, cwd=build_dir)
        
        # Run the executable
        executable_path = os.path.join(build_dir, "Release", "MonkGame.exe")
    else:
        cmake_command = f'cmake -G "Unix Makefiles" "{source_dir}"'
        run_command(cmake_command, cwd=build_dir)
        run_command("make", cwd=build_dir)
        executable_path = os.path.join(build_dir, "MonkGame")

    if os.path.exists(executable_path):
        run_command("clear || cls")
        run_command(f'"{executable_path}"')
    else:
        print(f"Error: Executable not found at {executable_path}")
        sys.exit(1)

if __name__ == "__main__":
    print(f"Building on {platform.system()}")
    cmake_build()
