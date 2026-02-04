from enum import Enum
from json import loads
from .tweak_classes import MobileGestaltTweak

class ValueType(Enum):
    Integer = "Integer"
    Float = "Float"
    String = "String"
    Array = "Array"
    Dictionary = "Dictionary"

ValueTypeStrings: list[ValueType] = [
    ValueType.Integer.value, ValueType.Float.value,
    ValueType.String.value,
    ValueType.Array.value, ValueType.Dictionary.value
]

class CustomGestaltTweak:
    def __init__(self, tweak: MobileGestaltTweak, value_type: ValueType):
        self.tweak = tweak
        self.value_type = value_type
        self.deactivated = False

    # TODO: change everything to not return the dict since it is passed by reference
    def apply_tweak(self, plist: dict) -> dict:
        if self.deactivated or self.tweak.key == "":
            # key was not set, don't apply (maybe user added it by accident)
            return plist
        self.tweak.enabled = True
        # set the value to be as the specified value type
        if self.value_type == ValueType.Integer:
            self.tweak.value = int(self.tweak.value)
        elif self.value_type == ValueType.Float:
            self.tweak.value = float(self.tweak.value)
        elif self.value_type == ValueType.Array or self.value_type == ValueType.Dictionary:
            # json convert string to array/dict
            self.tweak.value = loads(self.tweak.value)
        
        # apply the tweak after updating the value
        plist = self.tweak.apply_tweak(plist)
        return plist
            

class CustomGestaltTweaks:
    custom_tweaks: list[CustomGestaltTweak] = []

    def create_tweak(key: str="", value: str="1", value_type: ValueType = ValueType.Integer) -> int:
        new_tweak = MobileGestaltTweak(key, value=value)
        CustomGestaltTweaks.custom_tweaks.append(CustomGestaltTweak(new_tweak, value_type))
        # return the tweak id
        return len(CustomGestaltTweaks.custom_tweaks) - 1
    
    def set_tweak_key(id: int, key: str):
        CustomGestaltTweaks.custom_tweaks[id].tweak.key = key
            
    def set_tweak_value(id: int, value: str):
        CustomGestaltTweaks.custom_tweaks[id].tweak.value = value
            
    def set_tweak_value_type(id: int, value_type) -> str:
        new_value_type = value_type
        if isinstance(value_type, str):
            # based on string value
            new_value_type = ValueType(value_type)
        elif isinstance(value_type, int):
            # based on index of the string
            new_value_type = ValueType(ValueTypeStrings[value_type])

        CustomGestaltTweaks.custom_tweaks[id].value_type = new_value_type
        # update the value to be of the new type
        new_value = 1
        new_str = "1"
        if new_value_type == ValueType.Float:
            new_value = 1.0
            new_str = "1.0"
        elif new_value_type == ValueType.String:
            new_value = ""
            new_str = ""
        elif new_value_type == ValueType.Array:
            new_value = []
            new_str = "[  ]"
        elif new_value_type == ValueType.Dictionary:
            new_value = {}
            new_str = "{  }"
        CustomGestaltTweaks.custom_tweaks[id].tweak.value = new_value
        return new_str
    
    def deactivate_tweak(id: int):
        CustomGestaltTweaks.custom_tweaks[id].deactivated = True
        CustomGestaltTweaks.custom_tweaks[id].tweak = None

    def apply_tweaks(plist: dict):
        for tweak in CustomGestaltTweaks.custom_tweaks:
            plist = tweak.apply_tweak(plist)
        return plist