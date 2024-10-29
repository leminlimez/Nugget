from sys import platform

import PyInstaller.__main__

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
    '--icon=nugget.ico'
]

if platform == "darwin":
    # add --windowed arg for macOS
    args.append('--windowed')

PyInstaller.__main__.run(args)
