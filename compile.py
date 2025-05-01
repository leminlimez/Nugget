from sys import platform
import os

import PyInstaller.__main__

# configuration
universal: bool = False # issues with cross compiling since cpython only gives a single arch

args = [
    'main_app.py',
    # '--hidden-import=ipsw_parser',
    '--hidden-import=zeroconf',
    '--hidden-import=pyimg4',
    '--hidden-import=zeroconf._utils.ipaddress',
    '--hidden-import=zeroconf._handlers.answers',
    '--add-data=files/:./files',
    '--copy-metadata=pyimg4',
    '--onedir',
    '--noconfirm',
    '--name=Nugget',
    '--icon=nugget.ico',
    '--optimize=2'
]

if platform == "darwin":
    # add --windowed arg for macOS
    args.append('--windowed')
    args.append('--osx-bundle-identifier=com.leemin.Nugget')
    if universal:
        args.append('--target-arch=universal2')
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

PyInstaller.__main__.run(args)
