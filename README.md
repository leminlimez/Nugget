![Artboard][NuggetLogo]

# Nugget
Unlock your device's full potential!

Customize your device with animated wallpapers, disable pesky daemons, and more!

Make sure you have installed the [requirements](#requirements) if you are on Windows or Linux.

> [!NOTE]
> Please back up your data before using this Project! Nugget may cause unforeseen problems, so it is better to be safe than sorry. We are not responsible for any damage done to your device.

## Features
<details>
<summary>iOS 17.0+</summary>

- PosterBoard: Animated wallpapers and descriptors.
  - Community wallpapers can be found [here][WallpapersWebsite]
  - Converting videos to wallpapers
  - Customizing community-made wallpapers via batter files
  - See documentation on the structure of tendies and batter files in [documentation.md](documentation.md)
- Springboard Options (from [Cowabunga Lite][CowabungaLite])
  - Set Lock Screen Footnote
  - Disable Lock After Respring
  - Disable Screen Dimming While Charging
  - Disable Low Battery Alerts
- Internal Options (from [Cowabunga Lite][CowabungaLite])
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
- Risky (Hidden) Options:
  - Disable thermalmonitord
  - OTA Killer
  - Custom Resolution
</details>
<details>
<summary>iOS 17.0 - iOS 18.1.1</summary>

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
</details>
<details>
<summary>iOS 18.0 - iOS 18.0.1</summary>

- Feature Flags (iOS 18.1b4-):
  - Enabling lock screen clock animation, lock screen page duplication button, and more!
  - Disabling the new iOS 18 Photos UI (iOS 18.0 betas only, unknown which patched it)
</details>
<details>
<summary>iOS 18.0 - iOS 18.1.1</summary>

- Enable iPhone 16 camera button page in the Settings app
- Enable AOD & AOD Vibrancy on any device
</details>
<details>
<summary>iOS 18.1 - iOS 18.1.1</summary>

- AI Enabler
- Device Spoofing
</details>

## Requirements:
<details>
<summary>Windows</summary>
  
  - Either the [Apple Devices (from Microsoft Store)][AppleDevices] App or [iTunes (from Apple website)][iTunes]
</details>

<details>
<summary>Linux</summary>

  - [usbmuxd][usbmuxdGitHub]
  - [libimobiledevice][libimobiledeviceGitHub]
</details>

<details>
<summary>For Running Python</summary>

  - [pymobiledevice3][pymobiledevice3GitHub]
  - [PySide6][PySide6Doc]
  - Python 3.8 or newer
</details>

## Running the Python Program
> [!NOTE]
> It is highly recommended to use a virtual environment:
> ```py
> python3 -m venv .env # only needed once
> ```
macOS/Linux:
```py
source .env/bin/activate
```
Windows:
```py
.env/Scripts/activate.bat
```
Install Packages:
```py
pip3 install -r requirements.txt # only needed once
python3 main_app.py
```
> [!NOTE]
> Depending on your system configuration, use either `python/pip` or `python3/pip3`.

The CLI version can be run with:
```py 
python3 cli_app.py
```

## Getting the File
On iOS 18.1.1 and below, you may need to get the mobilegestalt file that is specific to your device. To do that, follow these steps:
1. Install the [Shortcuts][ShortcutsApp] app from the iOS app store.
2. Download this shortcut: [Save MobileGestalt][MobilegestaltShortcut]
3. Save the file and share it to your computer.
4. Place it in the same folder as the python file (or specify the path in the program)

## Building
To compile `mainwindow.ui` for Python, run the following command:
```py
pyside6-uic qt/mainwindow.ui -o qt/ui_mainwindow.py
```

To compile the resources file for Python, run the following command:
```py
pyside6-rcc resources.qrc -o resources_rc.py
```

The application itself can be compiled by running `compile.py`.

## Sparserestore Info
This uses the sparserestore exploit to write to files outside of the intended restore location, like mobilegestalt. Read the [Getting the File](#getting-the-file) section to learn how to get your mobilegestalt file.

Sparserestore works on all versions iOS 17.0-18.1.1. There is partial support for iOS 18.2 developer beta 3 and newer not using any exploits.

> [!NOTE]
> **Mobilegestalt and AI Enabler tweaks are not supported on iOS 18.2+.** It will never be supported, do not make issues asking for when it is supported.

## Read More
If you would like to read more about the inner workings of the exploit and iOS restore system, I made a write up which you can read [here][ReadMoreGist].
For clarity, up to iOS 18.2 developer beta 2 (public beta 1) is fully supported by Nugget. I said iOS 18.1.1 because mentioning the betas confused people.

## Arbitrary Star Graph
<a href="https://www.star-history.com/#leminlimez/Nugget&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=leminlimez/Nugget&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=leminlimez/Nugget&type=Date" />
    <img alt="Star History" src="https://api.star-history.com/svg?repos=leminlimez/Nugget&type=Date" />
  </picture>
</a>

## Credits
- [JJTech][JJTechGitHub] for Sparserestore/[TrollRestore][TrollStoreGitHub]
- [PosterRestore][PosterRestoreDiscord] for their help with PosterBoard
  - Special thanks to [dootskyre][dootskyreX], [Middo][MiddoX], [dulark][dularkGitHub], forcequitOS, and pingubow for their work on this. It would not have been possible without them!
  - Thanks to [Snoolie for aar handling][python-aar-stuffGitHub]!
  - Thanks to [SerStars][SerStarsX] for creating [the website][WallpapersWebsite]!
- [disfordottie][disfordottieX] for some global flag features
- [Mikasa-san][Mikasa-sanGitHub] for [Quiet Daemon][QuietDaemonGitHub]
- [sneakyf1shy][sneakyf1shyGitHub] for [AI Eligibility][AIEligibilityGist] (iOS 18.1 beta 4 and below)
- [lrdsnow][lrdsnowGitHub] for [EU Enabler][EUEnablerGitHub]
- [pymobiledevice3][pymobiledevice3GitHub] for restoring and device algorithms.
- [PySide6][PySide6Doc] for the GUI library.

[NuggetLogo]: https://raw.githubusercontent.com/leminlimez/Nugget/refs/heads/main/credits/small_nugget.png
[CowabungaLite]: https://github.com/leminlimez/CowabungaLite
[WallpapersWebsite]: https://cowabun.ga/wallpapers
[AppleDevices]: https://apps.microsoft.com/detail/9np83lwlpz9k
[iTunes]: https://support.apple.com/en-us/106372
[usbmuxdGitHub]: https://github.com/libimobiledevice/usbmuxd
[libimobiledeviceGitHub]: https://github.com/libimobiledevice/libimobiledevice
[ShortcutsApp]: https://apps.apple.com/us/app/shortcuts/id915249334
[MobilegestaltShortcut]: https://www.icloud.com/shortcuts/d6f0a136ddda4714a80750512911c53b
[ReadMoreGist]: https://gist.github.com/leminlimez/c602c067349140fe979410ef69d39c28

[JJTechGitHub]: https://github.com/JJTech0130
[TrollStoreGitHub]: https://github.com/JJTech0130/TrollRestore
[PosterRestoreDiscord]: https://discord.gg/gWtzTVhMvh
[dootskyreX]: https://x.com/dootskyre
[MiddoX]: https://x.com/MWRevamped
[dularkGitHub]: https://github.com/dularkian
[SerStarsX]: https://x.com/SerStars_lol
[disfordottieX]: https://x.com/disfordottie
[Mikasa-sanGitHub]: https://github.com/Mikasa-san
[QuietDaemonGitHub]: https://github.com/Mikasa-san/QuietDaemon
[sneakyf1shyGitHub]: https://github.com/f1shy-dev
[lrdsnowGitHub]: https://github.com/Lrdsnow
[EUEnablerGitHub]: https://github.com/Lrdsnow/EUEnabler
[pymobiledevice3GitHub]: https://github.com/doronz88/pymobiledevice3
[PySide6Doc]: https://doc.qt.io/qtforpython-6/
[python-aar-stuffGitHub]: https://github.com/0xilis/python-aar-stuff
[AIEligibilityGist]: https://gist.github.com/f1shy-dev/23b4a78dc283edd30ae2b2e6429129b5
