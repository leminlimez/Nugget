from enum import Enum

class FileLocation(Enum):
    # Mobile Gestalt
    resolution = "/var/Managed Preferences/mobile/com.apple.iokit.IOMobileGraphicsFamily.plist"
    
    # Springboard Options
    springboard = "/var/Managed Preferences/mobile/com.apple.springboard.plist"
    footnote = "/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/SharedDeviceConfiguration.plist"
    
    # Internal Options
    globalPreferences = "/var/Managed Preferences/mobile/.GlobalPreferences.plist"
    appStore = "/var/Managed Preferences/mobile/com.apple.AppStore.plist"
    backboardd = "/var/Managed Preferences/mobile/com.apple.backboardd.plist"
    coreMotion = "/var/Managed Preferences/mobile/com.apple.CoreMotion.plist"
    pasteboard = "/var/Managed Preferences/mobile/com.apple.Pasteboard.plist"
    notes = "/var/Managed Preferences/mobile/com.apple.mobilenotes.plist"
    uikit = "/var/Managed Preferences/mobile/com.apple.UIKit.plist"

    # Daemons
    disabledDaemons = "/var/db/com.apple.xpc.launchd/disabled.plist"
    screentime = "/var/mobile/Library/Preferences/ScreenTimeAgent.plist"

    # Risky Options
    ota = "/var/Managed Preferences/mobile/com.apple.MobileAsset.plist"
