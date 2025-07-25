from .tweaks import tweaks
from .tweak_classes import MobileGestaltTweak, MobileGestaltMultiTweak, MobileGestaltPickerTweak, RdarFixTweak, FeatureFlagTweak, BasicPlistTweak, FileLocation, AdvancedPlistTweak, NullifyFileTweak
from .eligibility_tweak import EligibilityTweak, AITweak
from devicemanagement.constants import Device, Version

def get_mobilegestalt_tweaks() -> dict:
    return {
        "DynamicIsland": MobileGestaltPickerTweak("oPeik/9e8lQWMszEjbPzng", subkey="ArtworkDeviceSubType", values=[2436, 2556, 2796, 2976, 2622, 2868]),
        "ModelName": MobileGestaltTweak("oPeik/9e8lQWMszEjbPzng", subkey="ArtworkDeviceProductDescription", value=""),
        "BootChime": MobileGestaltTweak("QHxt+hGLaBPbQJbXiUJX3w"),
        "ChargeLimit": MobileGestaltTweak("37NVydb//GP/GrhuTN+exg"),
        "CollisionSOS": MobileGestaltTweak("HCzWusHQwZDea6nNhaKndw"),
        "TapToWake": MobileGestaltTweak("yZf3GTRMGTuwSV/lD7Cagw"),
        "CameraButton": MobileGestaltMultiTweak({"CwvKxM2cEogD3p+HYgaW0Q": 1, "oOV1jhJbdV3AddkcCg0AEA": 1}),
        "Parallax": MobileGestaltTweak("UIParallaxCapability", value=0),
        "StageManager": MobileGestaltTweak("qeaj75wk3HF4DwQ8qbIi7g", value=1),
        "Medusa": MobileGestaltMultiTweak({"mG0AnH/Vy1veoqoLRAIgTA": 1, "UCG5MkVahJxG1YULbbd5Bg": 1, "ZYqko/XM5zD3XBfN5RmaXA": 1, "nVh/gwNpy7Jv1NOk00CMrw": 1, "uKc7FPnEO++lVhHWHFlGbQ": 1}),
        "iPadApps": MobileGestaltTweak("9MZ5AdH43csAUajl/dU+IQ", value=[1, 2]),
        "Shutter": MobileGestaltMultiTweak({"h63QSdBCiT/z0WU6rdQv6Q": "US", "zHeENZu+wbg7PUprwNwBWg": "LL/A"}),
        "FindMyFriends": MobileGestaltTweak("Y2Y67z0Nq/XdDXgW2EeaVg"),
        "Pencil": MobileGestaltTweak("yhHcB0iH0d1XzPO/CFd3ow"),
        "ActionButton": MobileGestaltTweak("cT44WE1EohiwRzhsZ8xEsw"),
        "InternalStorage": MobileGestaltTweak("LBJfwOEzExRxzlAnSuI7eg"),
        "InternalInstall": MobileGestaltTweak("EqrsVvjcYDdxHBiQmGhAWw"),
        "AOD": MobileGestaltMultiTweak(
                                {"2OOJf1VhaM7NxfRok3HbWQ": 1, "j8/Omm6s1lsmTDFsXjsBfA": 1}),
        "AODVibrancy": MobileGestaltTweak("ykpu7qyhqFweVMKtxNylWA")
    }

def load_rdar_fix(dev: Device):
    if "RdarFix" in tweaks:
        return
    tweaks.update({"RdarFix": RdarFixTweak()})
    if dev != None:
        # load settings
        tweaks["RdarFix"].get_rdar_mode(dev.model)

def load_mobilegestalt(dev: Device):
    load_rdar_fix(dev)
    if "DynamicIsland" in tweaks:
        return
    additional_tweaks = get_mobilegestalt_tweaks()
    # add to tweaks
    tweaks.update(additional_tweaks)

def load_eligibility(dev: Device):
    if "AIGestalt" in tweaks:
        return
    additional_tweaks = {
        "EUEnabler": EligibilityTweak(),
        "AIEligibility": AITweak(),
        "AIGestalt": MobileGestaltTweak("A62OafQ85EJAiiqKn4agtg"),
        "SpoofModel": MobileGestaltPickerTweak("h9jDsbgj7xIVeIQ8S3/X3Q", values=[
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
        ]),
        "SpoofHardware": MobileGestaltPickerTweak("oYicEKzVTz4/CxxE05pEgQ", values=[
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
        ]),
        "SpoofCPU": MobileGestaltPickerTweak("5pYKlGnYYBzGvAlIU8RjEQ", values=[
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
        ])
    }
    # load settings
    if dev != None:
        additional_tweaks["SpoofModel"].value[0] = dev.model
        additional_tweaks["SpoofHardware"].value[0] = dev.hardware
        additional_tweaks["SpoofCPU"].value[0] = dev.cpu
    # add to tweaks
    tweaks.update(additional_tweaks)

def load_featureflags():
    if "ClockAnim" in tweaks:
        return
    additional_tweaks = {
        "ClockAnim": FeatureFlagTweak(flag_category='SpringBoard',
                     flag_names=['SwiftUITimeAnimation']),
        "Lockscreen": FeatureFlagTweak(flag_category="SpringBoard",
                        flag_names=['AutobahnQuickSwitchTransition', 'SlipSwitch', 'PosterEditorKashida']),
        "PhotoUI": FeatureFlagTweak(flag_category='Photos', flag_names=['Lemonade'], is_list=False, inverted=True),
        "AI": FeatureFlagTweak(flag_category='SpringBoard', flag_names=['Domino', 'SuperDomino'])
    }
    tweaks.update(additional_tweaks)

def load_springboard():
    if "LockScreenFootnote" in tweaks:
        return
    additional_tweaks = {
        "LockScreenFootnote": BasicPlistTweak(
            FileLocation.footnote,
            key="LockScreenFootnote", value=""
        ),
        "SBDontLockAfterCrash": BasicPlistTweak(
            FileLocation.springboard,
            "SBDontLockAfterCrash"
        ),
        "SBDontDimOrLockOnAC": BasicPlistTweak(
            FileLocation.springboard,
            "SBDontDimOrLockOnAC"
        ),
        "SBHideLowPowerAlerts": BasicPlistTweak(
            FileLocation.springboard,
            "SBHideLowPowerAlerts"
        ),
        "SBHideACPower": BasicPlistTweak(
            FileLocation.springboard,
            "SBHideACPower"
        ),
        "SBNeverBreadcrumb": BasicPlistTweak(
            FileLocation.springboard,
            "SBNeverBreadcrumb"
        ),
        "SBShowSupervisionTextOnLockScreen": BasicPlistTweak(
            FileLocation.springboard,
            "SBShowSupervisionTextOnLockScreen"
        ),
        "AirplaySupport": BasicPlistTweak(
            FileLocation.springboard,
            "SBExtendedDisplayOverrideSupportForAirPlayAndDontFileRadars"
        ),
        "SBMinimumLockscreenIdleTime": BasicPlistTweak(
            FileLocation.springboard,
            key="SBMinimumLockscreenIdleTime",
            value=5
        ),
        "SBAlwaysShowSystemApertureInSnapshots": BasicPlistTweak(
            FileLocation.springboard,
            "SBAlwaysShowSystemApertureInSnapshots"
        )
    }
    tweaks.update(additional_tweaks)

def load_internal():
    if "RTL" in tweaks:
        return
    additional_tweaks = {
        "SBBuildNumber": BasicPlistTweak(
            FileLocation.globalPreferences,
            "UIStatusBarShowBuildVersion"
        ),
        "RTL": BasicPlistTweak(
            FileLocation.globalPreferences,
            "NSForceRightToLeftWritingDirection"
        ),
        "SBIconVisibility": BasicPlistTweak(
            FileLocation.globalPreferences,
            "SBIconVisibility"
        ),
        "MetalForceHudEnabled": BasicPlistTweak(
            FileLocation.globalPreferences,
            "MetalForceHudEnabled"
        ),
        "iMessageDiagnosticsEnabled": BasicPlistTweak(
            FileLocation.globalPreferences,
            "iMessageDiagnosticsEnabled"
        ),
        "IDSDiagnosticsEnabled": BasicPlistTweak(
            FileLocation.globalPreferences,
            "IDSDiagnosticsEnabled"
        ),
        "VCDiagnosticsEnabled": BasicPlistTweak(
            FileLocation.globalPreferences,
            "VCDiagnosticsEnabled"
        ),
        "AppStoreDebug": BasicPlistTweak(
            FileLocation.appStore,
            "debugGestureEnabled"
        ),
        "NotesDebugMode": BasicPlistTweak(
            FileLocation.notes,
            "DebugModeEnabled"
        ),
        "BKDigitizerVisualizeTouches": BasicPlistTweak(
            FileLocation.backboardd,
            "BKDigitizerVisualizeTouches"
        ),
        "BKHideAppleLogoOnLaunch": BasicPlistTweak(
            FileLocation.backboardd,
            "BKHideAppleLogoOnLaunch"
        ),
        "EnableWakeGestureHaptic": BasicPlistTweak(
            FileLocation.coreMotion,
            "EnableWakeGestureHaptic"
        ),
        "PlaySoundOnPaste": BasicPlistTweak(
            FileLocation.pasteboard,
            "PlaySoundOnPaste"
        ),
        "AnnounceAllPastes": BasicPlistTweak(
            FileLocation.pasteboard,
            "AnnounceAllPastes"
        )
    }
    tweaks.update(additional_tweaks)

def load_risky():
    if "CustomResolution" in tweaks:
        return
    additional_tweaks = {
        "DisableOTAFile": AdvancedPlistTweak(
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
            FileLocation.resolution,
            {}, # empty as to not cause issues when only 1 value is inputted
            is_risky=True
        )
    }
    tweaks.update(additional_tweaks)

def load_daemons():
    if "Daemons" in tweaks:
        return
    additional_tweaks = {
        "Daemons": AdvancedPlistTweak(
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
        "ClearScreenTimeAgentPlist": NullifyFileTweak(FileLocation.screentime),
    }
    tweaks.update(additional_tweaks)

def load_all_tweaks(version: str):
    parsed_ver = Version(version)
    if parsed_ver <= Version("18.2"):
        # load mobilegestalt + eligibility tweaks
        load_mobilegestalt()
        load_eligibility()
    if parsed_ver < Version("18.1"):
        # load feature flags
        load_featureflags()
    load_springboard()
    load_internal()
    load_daemons()
    load_risky()
