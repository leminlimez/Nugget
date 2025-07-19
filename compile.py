from sys import platform, argv
import os

import PyInstaller.__main__

target_arch=None

for n in argv:
    if n.startswith("--target-arch="):
        print(f"Target arch: {n}")
        target_arch=n

args = [
    'main_app.py',
    # '--hidden-import=ipsw_parser',
    '--hidden-import=zeroconf',
    '--hidden-import=pyimg4',
    '--hidden-import=zeroconf._utils.ipaddress',
    '--hidden-import=zeroconf._handlers.answers',
    '--collect-all=devicemanagement',
    '--add-data=files/:./files',
    '--copy-metadata=pyimg4',
    '--onedir',
    '--noconfirm',
    '--name=Nugget',
    '--icon=nugget.ico'
]

if target_arch == None:
    args.append('--optimize=2')

if platform == "darwin":
    # add --windowed arg for macOS
    args.append('--windowed')
    args.append('--osx-bundle-identifier=com.leemin.Nugget')
    if target_arch != None:
        args.append(target_arch)
    # codesigning resources
    try:
        import secrets.compile_config as compile_config
        args.append('--osx-entitlements-file=entitlements.plist')
        args.append(f"--codesign-identity={compile_config.CODESIGN_HASH}")
    except ImportError:
        print("No compile_config found, ignoring codesign...")
elif os.name == 'nt':
    # add windows version info
    args.append('--version-file=version.txt')
    # add the status bar executable
    args.append('--add-binary=.\\status_setter_windows.exe;.')
    if os.path.exists("ffmpeg/bin"):
        args.append('--add-data=ffmpeg/bin:ffmpeg/bin')
    else:
        print("ffmpeg not found!")

PyInstaller.__main__.run(args)
