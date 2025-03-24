# Nugget
Unlock your device's full potential!

Sparserestore works on all versions iOS 17.0-18.2 developer beta 2. There is partial support for iOS 18.2 developer beta 3 and newer.

**Mobilegestalt and AI Enabler tweaks are not supported on iOS 18.2+.** It will never be supported, do not make issues asking for when it is supported.

Make sure you have installed the [requirements](#requirements) if you are on Windows or Linux.

This uses the sparserestore exploit to write to files outside of the intended restore location, like mobilegestalt. Read the [Getting the File](#getting-the-file) section to learn how to get your mobilegestalt file.

Note: I am not responsible if your device bootloops. Please back up your data before using!

## Features
### iOS 17.0+
- Enable Dynamic Island on any device
- Enable iPhone X gestures on iPhone SEs
- Change Device Model Name (ie what shows in the Settings app)
- Enable Boot Chime
- Enable Charge Limit
- Enable Tap to Wake on unsupported devices (ie iPhone SEs)
- Enable Collision SOS
- Enable Stage Manager
- Disable the Wallpaper Parallax
- Disable Region Restrictions (ie. Shutter Sound)
  - Note: This does not include enabling EU sideloading outside the EU. That will come later.
- Show the Apple Pencil options in Settings app
- Show the Action Button options in Settings app
- Show Internal Storage info (Might cause problems on some devices, use at your own risk)
- EU Enabler (iOS 17.6-)
- Springboard Options (from [Cowabunga Lite](https://github.com/leminlimez/CowabungaLite))
  - Set Lock Screen Footnote
  - Disable Lock After Respring
  - Disable Screen Dimming While Charging
  - Disable Low Battery Alerts
- Internal Options (from [Cowabunga Lite](https://github.com/leminlimez/CowabungaLite))
  - Build Version in Status Bar
  - Force Right to Left
  - Force Metal HUD Debug
  - iMessage Diagnostics
  - IDS Diagnostics
  - VC Diagnostics
  - App Store Debug Gesture
  - Notes App Debug Mode
- Disable Daemons:
  - OTAd
  - UsageTrackingAgent
  - Game Center
  - Screen Time Agent
  - Logs, Dumps, and Crash Reports
  - ATWAKEUP
  - Tipsd
  - VPN
  - Chinese WLAN service
  - HealthKit
  - AirPrint
  - Assistive Touch
  - iCloud
  - Internet Tethering (aka Personal Hotspot)
  - PassBook
  - Spotlight
  - Voice Control
- PosterBoard: Animated wallpapers and descriptors.
  - Community wallpapers can be found [here](https://cowabun.ga/wallpapers)
  - See documentation on the structure of tendies files in `documentation.md`
- Risky (Hidden) Options:
  - Disable thermalmonitord
  - OTA Killer
  - Custom Resolution
### iOS 18.0+
- Enable iPhone 16 camera button page in the Settings app
- Enable AOD & AOD Vibrancy on any device
- Feature Flags (iOS 18.1b4-):
  - Enabling lock screen clock animation, lock screen page duplication button, and more!
  - Disabling the new iOS 18 Photos UI (iOS 18.0 betas only, unknown which patched it)
### iOS 18.1+
- AI Enabler + Device Spoofing (fixed in iOS 18.2db3)

## Requirements:
- **Windows:**
  - Either [Apple Devices (from Microsoft Store)](https://apps.microsoft.com/detail/9np83lwlpz9k%3Fhl%3Den-US%26gl%3DUS&ved=2ahUKEwjE-svo7qyJAxWTlYkEHQpbH3oQFnoECBoQAQ&usg=AOvVaw0rZTXCFmRaHAifkEEu9tMI) app or [iTunes (from Apple website)](https://support.apple.com/en-us/106372)
- **Linux:**
  - [usbmuxd](https://github.com/libimobiledevice/usbmuxd) and [libimobiledevice](https://github.com/libimobiledevice/libimobiledevice)

- **For Running Python:**
  - pymobiledevice3
  - PySide6
  - Python 3.8 or newer

## Running the Python Program
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

## Read More
If you would like to read more about the inner workings of the exploit and iOS restore system, I made a write up which you can read [here](https://gist.github.com/leminlimez/c602c067349140fe979410ef69d39c28).

## Credits
- [JJTech](https://github.com/JJTech0130) for Sparserestore/[TrollRestore](https://github.com/JJTech0130/TrollRestore)
- [PosterRestore](https://discord.gg/gWtzTVhMvh) for their help with PosterBoard
  - Special thanks to dootskyre, [Middo](https://twitter.com/MWRevamped), [dulark](https://github.com/dularkian), forcequitOS, and pingubow for their work on this. It would not have been possible without them!
- [disfordottie](https://x.com/disfordottie) for some global flag features
- [Mikasa-san](https://github.com/Mikasa-san) for [Quiet Daemon](https://github.com/Mikasa-san/QuietDaemon)
- [sneakyf1shy](https://github.com/f1shy-dev) for [AI Eligibility](https://gist.github.com/f1shy-dev/23b4a78dc283edd30ae2b2e6429129b5) (iOS 18.1 beta 4 and below)
- [lrdsnow](https://github.com/Lrdsnow) for [EU Enabler](https://github.com/Lrdsnow/EUEnabler)
- [pymobiledevice3](https://github.com/doronz88/pymobiledevice3) for restoring and device algorithms.
- [PySide6](https://doc.qt.io/qtforpython-6/) for the GUI library.
