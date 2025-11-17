from enum import Enum
from pymobiledevice3.lockdown import LockdownClient

class Device:
    def __init__(self, uuid: int, usb: bool, name: str, version: str, build: str, model: str, hardware: str, cpu: str, locale: str, ld: LockdownClient):
        self.uuid = uuid
        self.connected_via_usb = usb
        self.name = name
        self.version = version
        self.build = build
        self.model = model
        self.hardware = hardware
        self.cpu = cpu
        self.locale = locale
        self.ld = ld

    def is_exploit_fully_patched(self) -> bool:
        # mobile gestalt methods are completely patched on iOS 26.2 beta 2+
        return not (self.has_bookrestore() or self.has_partial_sparserestore())
    
    def has_bookrestore(self) -> bool:
        parsed_ver: Version = Version(self.version)
        if (parsed_ver <= Version("26.1") or self.build == "23C5027f"):
            return True
        return False
    
    def has_partial_sparserestore(self) -> bool:
        parsed_ver: Version = Version(self.version)
        if (parsed_ver < Version("18.2")
            or self.build == "22C5109p" or self.build == "22C5125e"):
            return True
        return False

    def has_exploit(self) -> bool:
        parsed_ver: Version = Version(self.version)
        # make sure versions past 17.7.1 but before 18.0 aren't supported
        if (parsed_ver >= Version("17.7.1") and parsed_ver < Version("18.0")):
            return False
        if (parsed_ver < Version("18.1")
            or self.build == "22B5007p" or self.build == "22B5023e"
            or self.build == "22B5034e" or self.build == "22B5045g"):
            return True
        return False

    def supported(self) -> bool:
        return self.has_exploit()

class Version:
    def __init__(self, major: int, minor: int = 0, patch: int = 0):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __init__(self, ver: str):
        nums: list[str] = ver.split(".")
        self.major = int(nums[0])
        self.minor = int(nums[1]) if len(nums) > 1 else 0
        self.patch = int(nums[2]) if len(nums) > 2 else 0

    # Comparison Functions
    def compare_to(self, other) -> int:
        if self.major > other.major:
            return 1
        elif self.major < other.major:
            return -1
        if self.minor > other.minor:
            return 1
        elif self.minor < other.minor:
            return -1
        if self.patch > other.patch:
            return 1
        elif self.patch < other.patch:
            return -1
        return 0
        
    def __gt__(self, other) -> bool:
        return self.compare_to(other) == 1
    def __ge__(self, other) -> bool:
        comp: int = self.compare_to(other)
        return comp == 0 or comp == 1
    
    def __lt__(self, other) -> bool:
        return self.compare_to(other) == -1
    def __le__(self, other) -> bool:
        comp: int = self.compare_to(other)
        return comp == 0 or comp == -1
    
    def __eq__(self, other) -> bool:
        return self.compare_to(other) == 0
    
class Tweak(Enum):
    StatusBar = 'Status Bar'
    SpringboardOptions = 'Springboard Options'
    InternalOptions = 'Internal Options'
    SkipSetup = 'Setup Options'

class FileLocation(Enum):
    # Control Center
    mute = "ControlCenter/ManagedPreferencesDomain/mobile/com.apple.control-center.MuteModule.plist"
    focus = "ControlCenter/ManagedPreferencesDomain/mobile/com.apple.FocusUIModule.plist"
    spoken = "ControlCenter/ManagedPreferencesDomain/mobile/com.apple.siri.SpokenNotificationsModule.plist"
    module_config = "ControlCenter/HomeDomain/Library/ControlCenter/ModuleConfiguration.plist"
    replay_kit_audio = "ControlCenter/ManagedPreferencesDomain/mobile/com.apple.replaykit.AudioConferenceControlCenterModule.plist"
    replay_kit_video = "ControlCenter/ManagedPreferencesDomain/mobile/com.apple.replaykit.VideoConferenceControlCenterModule.plist"

    # Status Bar
    status_bar = "StatusBar/HomeDomain/Library/SpringBoard/statusBarOverrides"
    
    # Springboard Options
    springboard = "SpringboardOptions/ManagedPreferencesDomain/mobile/com.apple.springboard.plist"
    footnote = "SpringboardOptions/ConfigProfileDomain/Library/ConfigurationProfiles/SharedDeviceConfiguration.plist"
    wifi = "SpringboardOptions/SystemPreferencesDomain/SystemConfiguration/com.apple.wifi.plist"
    uikit = "SpringboardOptions/ManagedPreferencesDomain/mobile/com.apple.UIKit.plist"
    accessibility = "SpringboardOptions/ManagedPreferencesDomain/mobile/com.apple.Accessibility.plist"
    wifi_debug = "SpringboardOptions/ManagedPreferencesDomain/mobile/com.apple.MobileWiFi.debug.plist"
    airdrop = "SpringboardOptions/ManagedPreferencesDomain/mobile/com.apple.sharingd.plist"
    
    # Internal Options
    global_prefs = "InternalOptions/ManagedPreferencesDomain/mobile/hiddendotGlobalPreferences.plist"
    app_store = "InternalOptions/ManagedPreferencesDomain/mobile/com.apple.AppStore.plist"
    backboardd = "InternalOptions/ManagedPreferencesDomain/mobile/com.apple.backboardd.plist"
    core_motion = "InternalOptions/ManagedPreferencesDomain/mobile/com.apple.CoreMotion.plist"
    pasteboard = "InternalOptions/HomeDomain/Library/Preferences/com.apple.Pasteboard.plist"
    notes = "InternalOptions/ManagedPreferencesDomain/mobile/com.apple.mobilenotes.plist"
    maps = "InternalOptions/AppDomain-com.apple.Maps/Library/Preferences/com.apple.Maps.plist"
    weather = "InternalOptions/AppDomain-com.apple.weather/Library/Preferences/com.apple.weather.plist"
    
    # Setup Options
    cloud_config = "SkipSetup/ConfigProfileDomain/Library/ConfigurationProfiles/CloudConfigurationDetails.plist"