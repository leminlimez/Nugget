# CODENAME Nugget
Unlock your device's full potential! Works on all versions iOS 16.0+

Note: I am not responsible if your device bootloops. Please back up your data before using.

## Features
- Enable Dynamic Island on any device
- Change Device Model Name
- Enable Boot Chime
- Enable Charge Limit
- Enable Stage Manager

## Running the Program
Requirements:
- pymobiledevice3

Note: It is highly recommended to use a virtual environment:
```
python -m venv .env # only needed once
source .env/bin/activate
pip install -r requirements.txt # only needed once
python main_app.py
```

## Getting the File
You need to get the mobilegestalt file that is specific to your device. To do that, follow these steps:
1. Install the `Shortcuts` app from the iOS app store.
2. Download this shortcut: https://www.icloud.com/shortcuts/d6f0a136ddda4714a80750512911c53b
3. Save the file and share it to your computer.
4. Place it in the same folder as the python file (or specify the path in the program)

## Credits
- [JJTech](https://github.com/JJTech0130) for Sparserestore/[TrollRestore](https://github.com/JJTech0130/TrollRestore)
- [pymobiledevice3](https://github.com/doronz88/pymobiledevice3)

