from devicemanagement.constants import Version
from .tweak_classes import MobileGestaltTweak, MobileGestaltMultiTweak, MobileGestaltPickerTweak, FeatureFlagTweak, TweakModifyType, BasicPlistTweak, AdvancedPlistTweak, RdarFixTweak
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
    "SpoofModel": MobileGestaltPickerTweak("Spoofed Device Model", "h9jDsbgj7xIVeIQ8S3/X3Q", values=[
        # Default
        "Placeholder", # 0 | Original

        # iPhone
        "iPhone16,1", # 1 | iPhone 15 Pro
        "iPhone16,2", # 2 | iPhone 15 Pro Max
        "iPhone17,3", # 3 | iPhone 16
        "iPhone17,4", # 4 | iPhone 16 Plus
        "iPhone17,1", # 5 | iPhone 16 Pro
        "iPhone17,2", # 6 | iPhone 16 Pro Max

        # A17 Pro iPads
        "iPad16,1", # 7 | iPad Mini (A17 Pro) (W)
        "iPad16,2", # 8 | iPad Mini (A17 Pro) (C)
    
        # M4 iPads
        "iPad16,5", # 9 | iPad Pro (13-inch) (M4) (W)
        "iPad16,6", # 10 | iPad Pro (13-inch) (M4) (C)
        "iPad16,3", # 11 | iPad Pro (11-inch) (M4) (W)
        "iPad16,4", # 12 | iPad Pro (11-inch) (M4) (C)

        # M2 iPads
        "iPad14,5", # 13 | iPad Pro (12.9-inch) (M2) (W)
        "iPad14,6", # 14 | iPad Pro (12.9-inch) (M2) (C)
        "iPad14,3", # 15 | iPad Pro (11-inch) (M2) (W)
        "iPad14,4", # 16 | iPad Pro (11-inch) (M2) (C)
        "iPad14,10", # 17 | iPad Air (13-inch) (M2) (W)
        "iPad14,11", # 18 | iPad Air (13-inch) (M2) (C)
        "iPad14,8", # 19 | iPad Air (11-inch) (M2) (W)
        "iPad14,9", # 20 | iPad Air (11-inch) (M2) (C)

        # M1 iPads
        "iPad13,4", # 21 | iPad Pro (11-inch) (M1) (W)
        "iPad13,5", # 22 | iPad Pro (11-inch) (M1) (C)
        "iPad13,8", # 23 | iPad Pro (12.9-inch) (M1) (W)
        "iPad13,9", # 24 | iPad Pro (12.9-inch) (M1) (C)
        "iPad13,16", # 25 | iPad Air (M1) (W)
        "iPad13,17", # 26 | iPad Air (M1) (C)
    ], min_version=Version("18.1")),
    "SpoofHardware": MobileGestaltPickerTweak("Spoof Hardware Model", "oYicEKzVTz4/CxxE05pEgQ", values=[
        # Default
        "Placeholder", # 0 | Original

        # iPhone
        "D83AP", # 1 | iPhone 15 Pro
        "D84AP", # 2 | iPhone 15 Pro Max
        "D47AP", # 3 | iPhone 16
        "D48AP", # 4 | iPhone 16 Plus
        "D93AP", # 5 | iPhone 16 Pro
        "D94AP", # 6 | iPhone 16 Pro Max

        # A17 Pro iPads
        "J410AP", # 7 | iPad Mini (A17 Pro) (W)
        "J411AP", # 8 | iPad Mini (A17 Pro) (C)
    
        # M4 iPads
        "J720AP", # 9 | iPad Pro (13-inch) (M4) (W)
        "J721AP", # 10 | iPad Pro (13-inch) (M4) (C)
        "J717AP", # 11 | iPad Pro (11-inch) (M4) (W)
        "J718AP", # 12 | iPad Pro (11-inch) (M4) (C)

        # M2 iPads
        "J620AP", # 13 | iPad Pro (12.9-inch) (M2) (W)
        "J621AP", # 14 | iPad Pro (12.9-inch) (M2) (C)
        "J617AP", # 15 | iPad Pro (11-inch) (M2) (W)
        "J618AP", # 16 | iPad Pro (11-inch) (M2) (C)
        "J537AP", # 17 | iPad Air (13-inch) (M2) (W)
        "J538AP", # 18 | iPad Air (13-inch) (M2) (C)
        "J507AP", # 19 | iPad Air (11-inch) (M2) (W)
        "J508AP", # 20 | iPad Air (11-inch) (M2) (C)

        # M1 iPads
        "J517AP", # 21 | iPad Pro (11-inch) (M1) (W)
        "J517xAP", # 22 | iPad Pro (11-inch) (M1) (C)
        "J522AP", # 23 | iPad Pro (12.9-inch) (M1) (W)
        "J522xAP", # 24 | iPad Pro (12.9-inch) (M1) (C)
        "J407AP", # 25 | iPad Air (M1) (W)
        "J408AP", # 26 | iPad Air (M1) (C)
    ], min_version=Version("18.1")),
    "SpoofCPU": MobileGestaltPickerTweak("Spoof CPU Model", "5pYKlGnYYBzGvAlIU8RjEQ", values=[
        # Default
        "Placeholder", # 0 | Original

        # iPhone
        "t8130", # 1 | iPhone 15 Pro
        "t8130", # 2 | iPhone 15 Pro Max
        "t8140", # 3 | iPhone 16
        "t8140", # 4 | iPhone 16 Plus
        "t8140", # 5 | iPhone 16 Pro
        "t8140", # 6 | iPhone 16 Pro Max

        # A17 Pro iPads
        "t8130", # 7 | iPad Mini (A17 Pro) (W)
        "t8130", # 8 | iPad Mini (A17 Pro) (C)
    
        # M4 iPads
        "t8182", # 9 | iPad Pro (13-inch) (M4) (W)
        "t8182", # 10 | iPad Pro (13-inch) (M4) (C)
        "t8182", # 11 | iPad Pro (11-inch) (M4) (W)
        "t8182", # 12 | iPad Pro (11-inch) (M4) (C)

        # M2 iPads
        "t8112", # 13 | iPad Pro (12.9-inch) (M2) (W)
        "t8112", # 14 | iPad Pro (12.9-inch) (M2) (C)
        "t8112", # 15 | iPad Pro (11-inch) (M2) (W)
        "t8112", # 16 | iPad Pro (11-inch) (M2) (C)
        "t8112", # 17 | iPad Air (13-inch) (M2) (W)
        "t8112", # 18 | iPad Air (13-inch) (M2) (C)
        "t8112", # 19 | iPad Air (11-inch) (M2) (W)
        "t8112", # 20 | iPad Air (11-inch) (M2) (C)

        # M1 iPads
        "t8103", # 21 | iPad Pro (11-inch) (M1) (W)
        "t8103", # 22 | iPad Pro (11-inch) (M1) (C)
        "t8103", # 23 | iPad Pro (12.9-inch) (M1) (W)
        "t8103", # 24 | iPad Pro (12.9-inch) (M1) (C)
        "t8103", # 25 | iPad Air (M1) (W)
        "t8103", # 26 | iPad Air (M1) (C)
    ], min_version=Version("18.1"), divider_below=True),

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
    ),

    ## Daemons
    "Daemons": AdvancedPlistTweak(
        "Disable Daemons",
        FileLocation.disabledDaemons,
        {
            "com.apple.magicswitchd.companion": True,
            "com.apple.security.otpaird": True,
            "com.apple.dhcp6d": True,
            "com.apple.bootpd": True,
            "com.apple.ftp-proxy-embedded": False,
            "com.apple.relevanced": True
        },
        owner=0, group=0
    ),

    ## Risky Options
    "DisableOTAFile": AdvancedPlistTweak(
        "Disable OTA Updates (file)",
        FileLocation.ota,
        {
            "MobileAssetServerURL-com.apple.MobileAsset.MobileSoftwareUpdate.UpdateBrain": "https://mesu.apple.com/assets/tvOS16DeveloperSeed",
            "MobileAssetSUAllowOSVersionChange": False,
            "MobileAssetSUAllowSameVersionFullReplacement": False,
            "MobileAssetServerURL-com.apple.MobileAsset.RecoveryOSUpdate": "https://mesu.apple.com/assets/tvOS16DeveloperSeed",
            "MobileAssetServerURL-com.apple.MobileAsset.RecoveryOSUpdateBrain": "https://mesu.apple.com/assets/tvOS16DeveloperSeed",
            "MobileAssetServerURL-com.apple.MobileAsset.SoftwareUpdate": "https://mesu.apple.com/assets/tvOS16DeveloperSeed",
            "MobileAssetAssetAudience": "65254ac3-f331-4c19-8559-cbe22f5bc1a6"
        }, is_risky=True
    ),
    "CustomResolution": AdvancedPlistTweak(
        "Set Custom Resolution real",
        FileLocation.resolution,
        {}, # empty as to not cause issues when only 1 value is inputted
        is_risky=True
    )
}