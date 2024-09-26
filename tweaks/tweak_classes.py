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
            divider_below: bool = False
        ):
        self.label = label
        self.key = key
        self.subkey = subkey
        self.value = value
        self.min_version = min_version
        self.edit_type = edit_type
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
    

class BasicPlistTweak(Tweak):
    def __init__(
            self, label: str,
            file_location: FileLocation,
            key: str,
            value: any = True,
            edit_type: TweakModifyType = TweakModifyType.TOGGLE,
            min_version: Version = Version("1.0"),
            divider_below: bool = False
        ):
        super.__init__(label=label, key=key, subkey=None, value=value, edit_type=edit_type, min_version=min_version, divider_below=divider_below)
        self.file_location = file_location

    def apply_tweak(self, other_tweaks: dict) -> dict:
        if not self.enabled:
            return other_tweaks
        if self.file_location in other_tweaks:
            other_tweaks[self.file_location][self.key] = self.value
        else:
            other_tweaks[self.file_location] = {self.key: self.value}
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
        if not self.enabled:
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