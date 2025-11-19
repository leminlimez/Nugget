from sys import platform, argv
import os
import PyInstaller.__main__

# Detect target architecture from CLI args
target_arch = next((arg for arg in argv if arg.startswith("--target-arch=")), None)
if target_arch:
	print(f"[+] Target arch: {target_arch}")

# Base PyInstaller args
args = [
	'main_app.py',
	'--name=Nugget',
	'--icon=nugget.ico',
	'--onedir',
	'--noconfirm',
	'--collect-all=devicemanagement',
	'--add-data=files/:files',
	'--copy-metadata=pyimg4',
	'--hidden-import=zeroconf',
	'--hidden-import=pyimg4',
	'--hidden-import=zeroconf._utils.ipaddress',
	'--hidden-import=zeroconf._handlers.answers',
	'--hidden-import=inquirer',
	'--hidden-import=readchar',
	'--copy-metadata=readchar'
]

# Use --optimize only if target arch not specified
if not target_arch:
	args.append('--optimize=2')
else:
	args.append(target_arch)

# macOS-specific flags
if platform == "darwin":
	args.append('--windowed')
	args.append('--osx-bundle-identifier=com.leemin.Nugget')

	# Try codesign if secrets module available
	try:
		import secrets_nugget.compile_config as compile_config
		args.append('--osx-entitlements-file=entitlements.plist')
		args.append(f"--codesign-identity={compile_config.CODESIGN_HASH}")
	except ImportError:
		print("[!] Codesign skipped: compile_config not found")

# Windows-specific flags
elif os.name == 'nt':
	import site
	site_packages_path = site.getsitepackages()[1]
	args.append('--version-file=version.txt')
	args.append('--add-binary=status_setter_windows.exe;.')
	args.append('--add-data=nugget.ico;.')
	args.append('--add-binary')
	args.append(f"{site_packages_path}/pytun_pmd3/*;pytun_pmd3")

	# Optional: bundle ffmpeg if available
	if os.path.isdir("ffmpeg/bin"):
		args.append('--add-data=ffmpeg/bin;ffmpeg/bin')
	else:
		print("[!] ffmpeg not bundled: folder not found")

PyInstaller.__main__.run(args)
