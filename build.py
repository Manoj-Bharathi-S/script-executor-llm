import subprocess
import sys
import os
import urllib.request
import zipfile
import shutil

def main():
    print("Preparing portable build system...")
    
    # 1. Install ziglang if it's not present
    print("Installing portable C compiler (Zig) via pip...")
    subprocess.run([sys.executable, "-m", "pip", "install", "ziglang"], check=True)
    
    # 2. Build the engine
    os.makedirs("build", exist_ok=True)
    
    # Gather C files
    c_files = ["host/nd_dump.c"]
    src_dir = "engine/src"
    for f in os.listdir(src_dir):
        if f.endswith(".c"):
            c_files.append(os.path.join(src_dir, f))
            
    print(f"Compiling {len(c_files)} C files into build/nd_dump.exe...")
    
    # Run zig cc
    cmd = [
        sys.executable, "-m", "ziglang", "cc",
        "-O3",                      # Optimize for speed
        "-Iengine/include",         # Include header files
        "-o", "build/nd_dump.exe",  # Output executable
    ] + c_files
    
    # Windows-specific libraries needed for networking/sockets if applicable, though C99 engine usually just needs standard libs
    # No extra libs needed for this barebones engine.
    
    result = subprocess.run(cmd)
    
    if result.returncode == 0:
        print("\nBuild successful! Executable created at build/nd_dump.exe")
    else:
        print("\nBuild failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
