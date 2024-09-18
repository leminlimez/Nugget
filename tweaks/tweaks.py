from devicemanagement.constants import Version
from .tweak_classes import MobileGestaltTweak, MobileGestaltMultiTweak, MobileGestaltPickerTweak, FeatureFlagTweak, TweakModifyType
from .eligibility_tweak import EligibilityTweak

    
tweaks = {
    "DynamicIsland": MobileGestaltPickerTweak("Toggle Dynamic Island", "oPeik/9e8lQWMszEjbPzng", "ArtworkDeviceSubType", [2436, 2556, 2796, 2976, 2622, 2868]),
    "ModelName": MobileGestaltTweak("Set Device Model Name", "oPeik/9e8lQWMszEjbPzng", "ArtworkDeviceProductDescription", "", TweakModifyType.TEXT),
    # MobileGestaltTweak("Fix Dynamic Island", "YlEtTtHlNesRBMal1CqRaA"),
    # MobileGestaltTweak("Set Dynamic Island Location", "Zg7DduDoSCy6vY6mhy3n2w", value="{ x: 390.000000, y: 205.848432, width: 50.000000, height: 105.651573 }"), # not sure what value this is supposed to be but it removes the island currently
    "BootChime": MobileGestaltTweak("Toggle Boot Chime", "QHxt+hGLaBPbQJbXiUJX3w"),
    "ChargeLimit": MobileGestaltTweak("Toggle Charge Limit", "37NVydb//GP/GrhuTN+exg"),
    "CollisionSOS": MobileGestaltTweak("Toggle Collision SOS", "HCzWusHQwZDea6nNhaKndw"),
    "TapToWake": MobileGestaltTweak("Toggle Tap To Wake (iPhone SE)", "yZf3GTRMGTuwSV/lD7Cagw"),
    "CameraButton": MobileGestaltMultiTweak("Toggle iPhone 16 Settings", {"CwvKxM2cEogD3p+HYgaW0Q": 1, "oOV1jhJbdV3AddkcCg0AEA": 1}, min_version=Version("18.0")),
    "Parallax": MobileGestaltTweak("Disable Wallpaper Parallax", "UIParallaxCapability", value=0),
    "StageManager": MobileGestaltTweak("Toggle Stage Manager Supported (WARNING: risky on some devices, mainly phones)", "qeaj75wk3HF4DwQ8qbIi7g", value=1),
    "iPadApps": MobileGestaltTweak("Allow iPad Apps on iPhone", "9MZ5AdH43csAUajl/dU+IQ", value=[1, 2]),
    "Shutter": MobileGestaltMultiTweak("Disable Region Restrictions (ie. Shutter Sound)", {"h63QSdBCiT/z0WU6rdQv6Q": "US", "zHeENZu+wbg7PUprwNwBWg": "LL/A"}),
    "Pencil": MobileGestaltTweak("Toggle Apple Pencil", "yhHcB0iH0d1XzPO/CFd3ow"),
    "ActionButton": MobileGestaltTweak("Toggle Action Button", "cT44WE1EohiwRzhsZ8xEsw"),
    "InternalStorage": MobileGestaltTweak("Toggle Internal Storage (WARNING: risky for some devices, mainly iPads)", "LBJfwOEzExRxzlAnSuI7eg"),
    "InternalInstall": MobileGestaltTweak("Set as Apple Internal Install (ie Metal HUD in any app)", "EqrsVvjcYDdxHBiQmGhAWw", divider_below=True),
    "EUEnabler": EligibilityTweak("EU Enabler", divider_below=True),
    "AOD": MobileGestaltMultiTweak("Always On Display",
                            {"2OOJf1VhaM7NxfRok3HbWQ": 1, "j8/Omm6s1lsmTDFsXjsBfA": 1},
                            min_version=Version("18.0")),
    "SleepApnea": MobileGestaltTweak("Toggle Sleep Apnea (real) [for apple watches]", "e0HV2blYUDBk/MsMEQACNA", min_version=Version("18.0"), divider_below=True),
    "ClockAnim": FeatureFlagTweak("Toggle Lockscreen Clock Animation", flag_category='SpringBoard',
                     flag_names=['SwiftUITimeAnimation'],
                     min_version=Version("18.0")),
    "Lockscreen": FeatureFlagTweak("Toggle Duplicate Lockscreen Button and Lockscreen Quickswitch", flag_category="SpringBoard",
                     flag_names=['AutobahnQuickSwitchTransition', 'SlipSwitch', 'PosterEditorKashida'],
                     min_version=Version("18.0")),
    "PhotoUI": FeatureFlagTweak("Enable Old Photo UI", flag_category='Photos', flag_names=['Lemonade'], is_list=False, inverted=True, min_version=Version("18.0")),
    "AI": FeatureFlagTweak("Enable Apple Intelligence", flag_category='SpringBoard', flag_names=['Domino', 'SuperDomino'], min_version=Version("18.1"))
}