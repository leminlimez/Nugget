from . import TemplateOption

import os
from dataclasses import dataclass
from typing import Optional
from enum import Enum

from controllers.xml_handler import set_xml_value

class SetterType(Enum):
    textbox = "textbox"
    slider = "slider"
    toggle = "toggle"

@dataclass
class SetOption(TemplateOption):
    identifier: str # nuggetId for properties in caml
    key: str # key of the property to change
    setter_type: SetterType # the type of input the user sees for setting the value
    use_ca_id: bool = False # whether or not to use the ca id over nuggetId

    # slider options
    min_value: Optional[int] = None # minimum value allowed for input
    max_value: Optional[int] = None # maximum value allowed for input
    step: int = 1 # the interval between each slider value
    is_float: bool = False # whether or not the values are a float (for qt slider)

    # toggle options
    inverted: bool = False # if set to true, the bool value will be inverted
    toggle_off_value: Optional[any] = None # the value to set when the toggle is off (for non-boolean values)
    toggle_on_value: Optional[any] = None # the value to set when the toggle is on (for non-boolean values)

    value: any = 0 # whether or not to delete the file

    def __init__(self, data: dict):
        super().__init__(data=data)
        self.label_object = None # for updating the qt label
        self.identifier = data['identifier']
        self.key = data['key']
        self.setter_type = SetterType[data['setter_type']]
        if 'use_ca_id' in data:
            self.use_ca_id = data['use_ca_id']

        # slider options
        if self.setter_type == SetterType.slider:
            # min and max values required
            self.min_value = data['min_value']
            self.max_value = data['max_value']
        elif self.setter_type == SetterType.textbox:
            # optional min and max values
            if 'min_value' in data:
                self.min_value = data['min_value']
            if 'max_value' in data:
                self.max_value = data['max_value']
        if 'step' in data:
            self.step = data['step']

        # toggle options
        if 'inverted' in data:
            self.inverted = data['inverted']
        if 'toggle_off_value' in data:
            self.toggle_off_value = data['toggle_off_value']
        if 'toggle_on_value' in data:
            self.toggle_on_value = data['toggle_on_value']

        if 'default_value' in data:
            self.value = data['default_value']
        else:
            if self.setter_type == SetterType.toggle:
                self.value = False
            elif self.min_value != None:
                self.value = self.min_value
            elif self.max_value != None:
                self.value = self.max_value

        # convert float to int for qt slider
        if self.setter_type == SetterType.slider and (isinstance(self.min_value, float)
                                                      or isinstance(self.max_value, float)
                                                      or isinstance(self.value, float)
                                                      or isinstance(self.step, float)):
            self.is_float = True
            self.min_value = int(self.min_value * 1000)
            self.max_value = int(self.max_value * 1000)
            self.step = int(self.step * 1000)
            self.value = int(self.value * 1000)

    def get_value(self):
        if self.is_float:
            return float(self.value) / 1000.0
        else:
            return self.value
    def get_min(self):
        if self.is_float:
            return float(self.min_value) / 1000.0
        else:
            return self.min_value
    def get_max(self):
        if self.is_float:
            return float(self.max_value) / 1000.0
        else:
            return self.max_value
    def update_value(self, nv: int):
        self.value = nv
        if self.label_object != None:
            self.label_object.setText(f"{self.label}: {self.get_value()}")

    def apply(self, container_path: str):
        apply_val = self.get_value()
        if self.setter_type == SetterType.toggle:
            if self.inverted:
                # invert toggle
                apply_val = not apply_val
            if apply_val and self.toggle_on_value != None:
                apply_val = self.toggle_on_value
            elif not apply_val and self.toggle_off_value != None:
                apply_val = self.toggle_off_value
        for file in self.files:
            path = os.path.join(container_path, file)
            set_xml_value(file=path, id=self.identifier, key=self.key, val=apply_val, use_ca_id=self.use_ca_id)