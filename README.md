# Nugget
Unlock your device's full potential!

Sparserestore works on all versions iOS 17.0-17.7 and iOS 18.0-18.1 beta 4. There is partial support for iOS 17.7.1 and iOS 18.1 beta 5+.

This uses the sparserestore exploit to write to files outside of the intended restore location, like mobilegestalt.

Note: I am not responsible if your device bootloops. Please back up your data before using!

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
- EU Enabler
- AI Enabler
- Springboard Options (from Cowabunga Lite)
- Internal Options (from Cowabunga Lite)

## Running the Program
**Requirements:**
- pymobiledevice3
- Python 3.8 or newer

- **Windows:**
  - Either [Apple Devices (from Microsoft Store)](https://apps.microsoft.com/detail/9np83lwlpz9k%3Fhl%3Den-US%26gl%3DUS&ved=2ahUKEwjE-svo7qyJAxWTlYkEHQpbH3oQFnoECBoQAQ&usg=AOvVaw0rZTXCFmRaHAifkEEu9tMI) app or [iTunes (from Apple website)](https://support.apple.com/en-us/106372)
- **Linux:**
  - [usbmuxd](https://github.com/libimobiledevice/usbmuxd) and [libimobiledevice](https://github.com/libimobiledevice/libimobiledevice)

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
To obtain the mobilegestalt file specific to your device, you can use one of the following methods:

### Method 1: Using Shortcuts

1. Install the **Shortcuts** app from the iOS App Store.
2. Download this shortcut: [Download Shortcut](https://www.icloud.com/shortcuts/d6f0a136ddda4714a80750512911c53b).
3. Save the file and share it to your computer.
4. Place it in the same folder as the Python file (or specify the path in the program).

### Method 2: Direct File Path

1. Paste this path into the search bar of the **Notes** app or **Settings** app:  
   `file://a/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist`.   
2. Select all the text and share it to your computer.
3. Place the file in the same folder as the Python file (or specify the path in the program).


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
- [sneakyf1shy](https://github.com/f1shy-dev) for [AI Enabler](https://gist.github.com/f1shy-dev/23b4a78dc283edd30ae2b2e6429129b5)

