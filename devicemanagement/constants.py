from enum import Enum
from pymobiledevice3.lockdown import LockdownClient

class Device:
    def __init__(self, uuid: int, name: str, version: str, build: str, model: str, locale: str, ld: LockdownClient):
        self.uuid = uuid
        self.name = name
        self.version = version
        self.build = build
        self.model = model
        self.locale = locale
        self.ld = ld

    def supported(self) -> bool:
        parsed_ver: Version = Version(self.version)
        if parsed_ver > Version("18.1"):
            return False
        if (parsed_ver == Version("18.1")
            and self.build != "22B5007p" and self.build != "22B5023e"
            and self.build != "22B5034e" and self.build != "22B5045g"):
            return False
        return True

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