import os
import shutil
import sys

required_dlls = ["libgcc_s_seh-1.dll", "libstdc++-6.dll", "libwinpthread-1.dll"]

search_roots = [
    r"C:\Program Files\Git\mingw64\bin",
    r"C:\Program Files\Git\usr\bin",
    r"C:\MinGW\bin",
    r"C:\msys64\mingw64\bin",
    r"C:\msys64\ucrt64\bin",
    os.path.expanduser("~") + r"\scoop\apps\gcc\current\bin",
    os.path.expanduser("~") + r"\scoop\apps\git\current\mingw64\bin",
]

project_dir = os.path.dirname(os.path.abspath(__file__))
found_count = 0

print(f"[*] Searching for missing DLLs in common locations...")

for root_path in search_roots:
    if not os.path.exists(root_path):
        continue
        
    for filename in required_dlls:
        src = os.path.join(root_path, filename)
        dst = os.path.join(project_dir, filename)
        
        if os.path.exists(src) and not os.path.exists(dst):
            try:
                print(f"[+] Found {filename} in {root_path}")
                shutil.copy2(src, dst)
                print(f"    -> Copied to project folder.")
                found_count += 1
            except Exception as e:
                print(f"[!] Failed to copy {filename}: {e}")

if found_count > 0:
    print(f"\n[SUCCESS] Found and copied {found_count} DLLs.")
    print("You can now run 'python compile.py' again.")
else:
    print("\n[FAILED] Could not find the DLLs in standard locations.")
    print("Please install 'Git for Windows' or download MinGW-w64.")