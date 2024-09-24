# Nugget
Unlock your device's full potential! Works on iOS 17.0 - 18.1 beta 4

This uses the sparserestore exploit to write to files outside of the intended restore location, like mobilegestalt.

Note: I am not responsible if your device bootloops. Please back up your data before using.

## Features
- Enable Dynamic Island on any device
- Enable iPhone X gestures on iPhone SEs
- Change Device Model Name (ie what shows in the Settings app)
- Enable Boot Chime
- Enable Charge Limit
- Enable Tap to Wake on unsupported devices (ie iPhone SEs)
- Enable iPhone 16 Settings
- Enable Collision SOS
- Enable Stage Manager
- Disable the Wallpaper Parallax
- Disable Region Restrictions (ie. Shutter Sound)
  - Note: This does not include enabling EU sideloading outside the EU. That will come later.
- Enable AOD on any device
- Show the Apple Pencil options in Settings app
- Show the Action Button options in Settings app
- Show Internal Storage info (Might cause problems on some devices, use at your own risk)
- Enabling lock screen clock animation, lock screen page duplication button, and more!
- Disabling the new iOS 18 Photos UI
- EU Enabler on <17.4.1

## Running the Program
Requirements:
- pymobiledevice3
- Python 3.8 or newer

Note: It is highly recommended to use a virtual environment:
```
python3 -m venv .env # only needed once
# macOS/Linux:  source .env/bin/activate
# Windows:      .env/Scripts/activate.bat
pip3 install -r requirements.txt # only needed once
python3 main_app.py
```
Note: It may be either `python`/`pip` or `python3`/`pip3` depending on your path.

The CLI version can be ran with `python3 cli_app.py`.

## Getting the File
You need to get the mobilegestalt file that is specific to your device. To do that, follow these steps:
1. Install the `Shortcuts` app from the iOS app store.
2. Download this shortcut: https://www.icloud.com/shortcuts/d6f0a136ddda4714a80750512911c53b
3. Save the file and share it to your computer.
4. Place it in the same folder as the python file (or specify the path in the program)

## Building
To compile `mainwindow.ui` for Python, run the following command:
`pyside6-uic qt/mainwindow.ui -o qt/ui_mainwindow.py`

To compile the resources file for Python, run the following command:
`pyside6-rcc qt/resources.qrc -o resources_rc.py`

The application itself can be compiled by running `compile.py`.

## Credits
- [JJTech](https://github.com/JJTech0130) for Sparserestore/[TrollRestore](https://github.com/JJTech0130/TrollRestore)
- [pymobiledevice3](https://github.com/doronz88/pymobiledevice3)
- [disfordottie](https://x.com/disfordottie) for some global flag features

