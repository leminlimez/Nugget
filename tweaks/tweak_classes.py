from enum import Enum
from devicemanagement.constants import Version
from .basic_plist_locations import FileLocation

class TweakModifyType(Enum):
    TOGGLE = 1
    TEXT = 2
    PICKER = 3

class Tweak:
    def __init__(
            self, label: str,
            key: str, subkey: str = None,
            value: any = 1,
            edit_type: TweakModifyType = TweakModifyType.TOGGLE,
            min_version: Version = Version("1.0"),
            owner: int = 501, group: int = 501,
            divider_below: bool = False
        ):
        self.label = label
        self.key = key
        self.subkey = subkey
        self.value = value
        self.min_version = min_version
        self.edit_type = edit_type
        self.owner = owner
        self.group = group
        self.divider_below = divider_below
        self.enabled = False

    def set_enabled(self, value: bool):
        self.enabled = value
    def toggle_enabled(self):
        self.enabled = not self.enabled
    def set_value(self, new_value: any, toggle_enabled: bool = True):
        self.value = new_value
        if toggle_enabled:
            self.enabled = True

    def is_compatible(self, device_ver: str):
        return Version(device_ver) >= self.min_version

    def apply_tweak(self):
        raise NotImplementedError
    
class NullifyFileTweak(Tweak):
    def __init__(
            self, label: str,
            file_location: FileLocation,
            min_version: Version = Version("1.0"),
            owner: int = 501, group: int = 501,
            divider_below: bool = False
        ):
        super().__init__(label=label, key=None, value=None, min_version=min_version, owner=owner, group=group, divider_below=divider_below)
        self.file_location = file_location

    def apply_tweak(self, other_tweaks: dict):
        if self.enabled:
            other_tweaks[self.file_location] = b""
    

class BasicPlistTweak(Tweak):
    def __init__(
            self, label: str,
            file_location: FileLocation,
            key: str,
            value: any = True,
            edit_type: TweakModifyType = TweakModifyType.TOGGLE,
            min_version: Version = Version("1.0"),
            owner: int = 501, group: int = 501,
            is_risky: bool = False,
            divider_below: bool = False
        ):
        super().__init__(label=label, key=key, subkey=None, value=value, edit_type=edit_type, min_version=min_version, owner=owner, group=group, divider_below=divider_below)
        self.file_location = file_location
        self.is_risky = is_risky

    def apply_tweak(self, other_tweaks: dict, risky_allowed: bool = False) -> dict:
        if not self.enabled or (self.is_risky and not risky_allowed):
            return other_tweaks
        if self.file_location in other_tweaks:
            other_tweaks[self.file_location][self.key] = self.value
        else:
            other_tweaks[self.file_location] = {self.key: self.value}
        return other_tweaks
    
class AdvancedPlistTweak(BasicPlistTweak):
    def __init__(
        self, label: str,
        file_location: FileLocation,
        keyValues: dict,
        edit_type: TweakModifyType = TweakModifyType.TOGGLE,
        min_version: Version = Version("1.0"),
        owner: int = 501, group: int = 501,
        is_risky: bool = False,
        divider_below: bool = False
    ):
        super().__init__(label=label, file_location=file_location, key=None, value=keyValues, edit_type=edit_type, min_version=min_version, owner=owner, group=group, is_risky=is_risky, divider_below=divider_below)

    def set_multiple_values(self, keys: list[str], value: any):
        for key in keys:
            self.value[key] = value

    def apply_tweak(self, other_tweaks: dict, risky_allowed: bool = False) -> dict:
        if not self.enabled or (self.is_risky and not risky_allowed):
            return other_tweaks
        plist = {}
        for key in self.value:
            plist[key] = self.value[key]
        other_tweaks[self.file_location] = plist
        return other_tweaks
    

class RdarFixTweak(BasicPlistTweak):
    def __init__(self, divider_below: bool = False):
        super().__init__(label="Fix RDAR (modifies resolution)", file_location=FileLocation.resolution, key=None, divider_below=divider_below)
        self.mode = 0
        self.di_type = -1

    def get_rdar_mode(self, model: str) -> int:
        if (model == "iPhone11,2" or model == "iPhone11,4" or model == "iPhone11,6"
            or model == "iPhone11,8"
            or model == "iPhone12,1" or model == "iPhone12,3" or model == "iPhone12,5"):
            self.mode = 1
        elif (model == "iPhone13,2" or model == "iPhone13,3" or model == "iPhone13,4"
              or model == "iPhone14,5" or model == "iPhone14,2" or model == "iPhone14,3"
              or model == "iPhone14,7" or model == "iPhone14,8"):
            self.mode = 2
        elif (model == "iPhone12,8" or model == "iPhone14,6"):
            self.mode = 3
        return self.mode
    
    def get_rdar_title(self) -> str:
        if self.mode == 1 or self.mode == 3:
            if self.di_type == -1:
                return "Revert RDAR fix"
            return "Fix RDAR"
        elif self.mode == 2:
            if self.di_type == -1:
                return "Revert Status Bar Fix"
            return "Dynamic Island Status Bar Fix"
        return "hide"
    
    def set_di_type(self, type: int):
        self.di_type = type

    def apply_tweak(self, other_tweaks: dict, risky_allowed: bool = False) -> dict:
        if not self.enabled:
            return other_tweaks
        if self.di_type == -1:
            # revert the fix
            other_tweaks[self.file_location] = {}
        elif self.mode == 1:
            # iPhone XR, XS, and 11
            plist = {
                "canvas_height": 1791,
                "canvas_width": 828
            }
            other_tweaks[self.file_location] = plist
        elif self.mode == 3:
            # iPhone SEs
            plist = {
                "canvas_height": 1779,
                "canvas_width": 1000
            }
            other_tweaks[self.file_location] = plist
        elif self.mode == 2:
            # Status bar fix (iPhone 12+)
            width = 2868
            height = 1320
            if self.di_type == 2556:
                width = 1179
                height = 2556
            elif self.di_type == 2796 or self.di_type == 2976:
                width = 1290
                height = 2796
            elif self.di_type == 2622:
                width = 1206
                height = 2622
            elif self.di_type == 2868:
                width = 1320
                height = 2868
            plist = {
                "canvas_height": height,
                "canvas_width": width
            }
            other_tweaks[self.file_location] = plist
        return other_tweaks


class MobileGestaltTweak(Tweak):
    def apply_tweak(self, plist: dict):
        if not self.enabled:
            return plist
        new_value = self.value
        if self.subkey == None:
            plist["CacheExtra"][self.key] = new_value
        else:
            plist["CacheExtra"][self.key][self.subkey] = new_value
        return plist
    
class MobileGestaltPickerTweak(Tweak):
    def __init__(
            self, label: str,
            key: str, subkey: str = None,
            values: list = [1],
            min_version: Version = Version("1.0"),
            divider_below: bool = False
        ):
        super().__init__(label=label, key=key, subkey=subkey, value=values, edit_type=TweakModifyType.PICKER, min_version=min_version, divider_below=divider_below)
        self.selected_option = 0 # index of the selected option

    def apply_tweak(self, plist: dict):
        if not self.enabled or self.value[self.selected_option] == "Placeholder":
            return plist
        new_value = self.value[self.selected_option]
        if self.subkey == None:
            plist["CacheExtra"][self.key] = new_value
        else:
            plist["CacheExtra"][self.key][self.subkey] = new_value
        return plist
    
    def set_selected_option(self, new_option: int):
        self.selected_option = new_option
        self.enabled = True

    def get_selected_option(self) -> int:
        return self.selected_option
    
class MobileGestaltMultiTweak(Tweak):
    def __init__(self, label: str, keyValues: dict, min_version: Version = Version("1.0"), divider_below: bool = False):
        super().__init__(label=label, key=None, min_version=min_version, divider_below=divider_below)
        self.keyValues = keyValues
        # key values looks like ["key name" = value]

    def apply_tweak(self, plist: dict):
        if not self.enabled:
            return plist
        for key in self.keyValues:
            plist["CacheExtra"][key] = self.keyValues[key]
        return plist
    
class FeatureFlagTweak(Tweak):
    def __init__(
            self, label: str,
                flag_category: str, flag_names: list,
                is_list: bool=True, inverted: bool=False,
                min_version: Version = Version("1.0"),
                divider_below: bool = False
            ):
        super().__init__(label=label, key=None, min_version=min_version, divider_below=divider_below)
        self.flag_category = flag_category
        self.flag_names = flag_names
        self.is_list = is_list
        self.inverted = inverted
        
    def apply_tweak(self, plist: dict):
        to_enable = self.enabled
        if self.inverted:
            to_enable = not self.enabled
        # create the category list if it doesn't exist
        if not self.flag_category in plist:
            plist[self.flag_category] = {}
        for flag in self.flag_names:
            if self.is_list:
                plist[self.flag_category][flag] = {
                    'Enabled': to_enable
                }
            else:
                plist[self.flag_category][flag] = to_enable
        return plist