from devicemanagement.constants import Version
from .tweak_classes import MobileGestaltTweak, MobileGestaltMultiTweak, MobileGestaltPickerTweak, FeatureFlagTweak, TweakModifyType, BasicPlistTweak, RdarFixTweak
from .eligibility_tweak import EligibilityTweak, AITweak
from .basic_plist_locations import FileLocation

    
tweaks = {
    ## MobileGestalt Tweaks
    "DynamicIsland": MobileGestaltPickerTweak("Toggle Dynamic Island", "oPeik/9e8lQWMszEjbPzng", "ArtworkDeviceSubType", [2436, 2556, 2796, 2976, 2622, 2868]),
    "RdarFix": RdarFixTweak(),
    "ModelName": MobileGestaltTweak("Set Device Model Name", "oPeik/9e8lQWMszEjbPzng", "ArtworkDeviceProductDescription", "", TweakModifyType.TEXT),
    "BootChime": MobileGestaltTweak("Toggle Boot Chime", "QHxt+hGLaBPbQJbXiUJX3w"),
    "ChargeLimit": MobileGestaltTweak("Toggle Charge Limit", "37NVydb//GP/GrhuTN+exg"),
    "CollisionSOS": MobileGestaltTweak("Toggle Collision SOS", "HCzWusHQwZDea6nNhaKndw"),
    "TapToWake": MobileGestaltTweak("Toggle Tap To Wake (iPhone SE)", "yZf3GTRMGTuwSV/lD7Cagw"),
    "CameraButton": MobileGestaltMultiTweak("Toggle iPhone 16 Settings", {"CwvKxM2cEogD3p+HYgaW0Q": 1, "oOV1jhJbdV3AddkcCg0AEA": 1}, min_version=Version("18.0")),
    "Parallax": MobileGestaltTweak("Disable Wallpaper Parallax", "UIParallaxCapability", value=0),
    "StageManager": MobileGestaltTweak("Toggle Stage Manager Supported (WARNING: risky on some devices, mainly phones)", "qeaj75wk3HF4DwQ8qbIi7g", value=1),
    "Medusa": MobileGestaltMultiTweak("Toggle Medusa (iPad Multitasking) (WARNING: may be risky on some phones)", {"mG0AnH/Vy1veoqoLRAIgTA": 1, "UCG5MkVahJxG1YULbbd5Bg": 1, "ZYqko/XM5zD3XBfN5RmaXA": 1, "nVh/gwNpy7Jv1NOk00CMrw": 1, "uKc7FPnEO++lVhHWHFlGbQ": 1}),
    "iPadApps": MobileGestaltTweak("Allow iPad Apps on iPhone", "9MZ5AdH43csAUajl/dU+IQ", value=[1, 2]),
    "Shutter": MobileGestaltMultiTweak("Disable Region Restrictions (ie. Shutter Sound)", {"h63QSdBCiT/z0WU6rdQv6Q": "US", "zHeENZu+wbg7PUprwNwBWg": "LL/A"}),
    "FindMyFriends": MobileGestaltTweak("Toggle Find My Friends", "Y2Y67z0Nq/XdDXgW2EeaVg"),
    "Pencil": MobileGestaltTweak("Toggle Apple Pencil", "yhHcB0iH0d1XzPO/CFd3ow"),
    "ActionButton": MobileGestaltTweak("Toggle Action Button", "cT44WE1EohiwRzhsZ8xEsw"),
    "InternalStorage": MobileGestaltTweak("Toggle Internal Storage (WARNING: risky for some devices, mainly iPads)", "LBJfwOEzExRxzlAnSuI7eg"),
    "InternalInstall": MobileGestaltTweak("Set as Apple Internal Install (ie Metal HUD in any app)", "EqrsVvjcYDdxHBiQmGhAWw", divider_below=True),
    "EUEnabler": EligibilityTweak("EU Enabler", divider_below=True),
    "AOD": MobileGestaltMultiTweak("Always On Display",
                            {"2OOJf1VhaM7NxfRok3HbWQ": 1, "j8/Omm6s1lsmTDFsXjsBfA": 1},
                            min_version=Version("18.0")),

    ## Feature Flag Tweaks
    "ClockAnim": FeatureFlagTweak("Toggle Lockscreen Clock Animation", flag_category='SpringBoard',
                     flag_names=['SwiftUITimeAnimation'],
                     min_version=Version("18.0")),
    "Lockscreen": FeatureFlagTweak("Toggle Duplicate Lockscreen Button and Lockscreen Quickswitch", flag_category="SpringBoard",
                     flag_names=['AutobahnQuickSwitchTransition', 'SlipSwitch', 'PosterEditorKashida'],
                     min_version=Version("18.0")),
    "PhotoUI": FeatureFlagTweak("Enable Old Photo UI", flag_category='Photos', flag_names=['Lemonade'], is_list=False, inverted=True, min_version=Version("18.0")),
    "AI": FeatureFlagTweak("Enable Apple Intelligence", flag_category='SpringBoard', flag_names=['Domino', 'SuperDomino'], min_version=Version("18.1"), divider_below=True),

    ## AI Enabler
    "AIEligibility": AITweak(),
    "AIGestalt": MobileGestaltTweak("Enable Apple Intelligence (for Unsupported Devices) (Gestalt)", "A62OafQ85EJAiiqKn4agtg", min_version=Version("18.1")),
    "SpoofModel": MobileGestaltPickerTweak("Spoofed Device Model", "h9jDsbgj7xIVeIQ8S3/X3Q", values=["iPhone16,2", "iPhone17,3", "iPhone17,4", "iPad16,3"], min_version=Version("18.1"), divider_below=True),

    ## Springboard Tweaks
    "LockScreenFootnote": BasicPlistTweak(
        "Set Lock Screen Footnote Text",
        FileLocation.footnote,
        key="LockScreenFootnote", value="",
        edit_type=TweakModifyType.TEXT
    ),
    "SBDontLockAfterCrash": BasicPlistTweak(
        "Disable Lock After Respring",
        FileLocation.springboard,
        "SBDontLockAfterCrash"
    ),
    "SBDontDimOrLockOnAC": BasicPlistTweak(
        "Disable Screen Dimming While Charging",
        FileLocation.springboard,
        "SBDontDimOrLockOnAC"
    ),
    "SBHideLowPowerAlerts": BasicPlistTweak(
        "Disable Low Battery Alerts",
        FileLocation.springboard,
        "SBHideLowPowerAlerts"
    ),
    "SBNeverBreadcrumb": BasicPlistTweak(
        "Disable Breadcrumb",
        FileLocation.springboard,
        "SBNeverBreadcrumb"
    ),
    "SBShowSupervisionTextOnLockScreen": BasicPlistTweak(
        "Show Supervision Text on Lock Screen",
        FileLocation.springboard,
        "SBShowSupervisionTextOnLockScreen"
    ),
    "AirplaySupport": BasicPlistTweak(
        "Enable AirPlay support for Stage Manager",
        FileLocation.springboard,
        "SBExtendedDisplayOverrideSupportForAirPlayAndDontFileRadars",
        divider_below=True
    ),

    ## Internal Options
    "SBBuildNumber": BasicPlistTweak(
        "Show Build Version in Status Bar",
        FileLocation.globalPreferences,
        "UIStatusBarShowBuildVersion"
    ),
    "RTL": BasicPlistTweak(
        "Force Right-to-Left Layout",
        FileLocation.globalPreferences,
        "NSForceRightToLeftWritingDirection"
    ),
    "MetalForceHudEnabled": BasicPlistTweak(
        "Enable Metal HUD Debug",
        FileLocation.globalPreferences,
        "MetalForceHudEnabled"
    ),
    "AccessoryDeveloperEnabled": BasicPlistTweak(
        "Enable Accessory Debugging",
        FileLocation.globalPreferences,
        "AccessoryDeveloperEnabled"
    ),
    "iMessageDiagnosticsEnabled": BasicPlistTweak(
        "Enable iMessage Debugging",
        FileLocation.globalPreferences,
        "iMessageDiagnosticsEnabled"
    ),
    "IDSDiagnosticsEnabled": BasicPlistTweak(
        "Enable Continuity Debugging",
        FileLocation.globalPreferences,
        "IDSDiagnosticsEnabled"
    ),
    "VCDiagnosticsEnabled": BasicPlistTweak(
        "Enable FaceTime Debugging",
        FileLocation.globalPreferences,
        "VCDiagnosticsEnabled"
    ),
    "AppStoreDebug": BasicPlistTweak(
        "Enable App Store Debug Gesture",
        FileLocation.appStore,
        "debugGestureEnabled"
    ),
    "NotesDebugMode": BasicPlistTweak(
        "Enable Notes App Debug Mode",
        FileLocation.notes,
        "DebugModeEnabled"
    ),
    "BKDigitizerVisualizeTouches": BasicPlistTweak(
        "Show Touches With Debug Info",
        FileLocation.backboardd,
        "BKDigitizerVisualizeTouches"
    ),
    "BKHideAppleLogoOnLaunch": BasicPlistTweak(
        "Hide Respring Icon",
        FileLocation.backboardd,
        "BKHideAppleLogoOnLaunch"
    ),
    "EnableWakeGestureHaptic": BasicPlistTweak(
        "Vibrate on Raise-to-Wake",
        FileLocation.coreMotion,
        "EnableWakeGestureHaptic"
    ),
    "PlaySoundOnPaste": BasicPlistTweak(
        "Play Sound on Paste",
        FileLocation.pasteboard,
        "PlaySoundOnPaste"
    ),
    "AnnounceAllPastes": BasicPlistTweak(
        "Show Notifications for System Pastes",
        FileLocation.pasteboard,
        "AnnounceAllPastes"
    )
}