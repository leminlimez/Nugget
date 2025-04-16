from . import TemplateOption

import os
from dataclasses import dataclass
from typing import Optional
from enum import Enum
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QColorDialog

from controllers.xml_handler import set_xml_value, set_xml_values

class SetterType(Enum):
    textbox = "textbox"
    slider = "slider"
    toggle = "toggle"
    color_picker = "color_picker"

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

    # color picker options
    sets_opacity: bool = False # whether or not the color_picker sets the opacity value

    value: any = 0 # whether or not to delete the file
    value_tag: Optional[str] = None # the value tag in the caml (ie "scale(0 0 0)")

    def split_value(self, value):
        if value == None:
            return None
        if isinstance(value, str) and ' ' in value:
            # first get the value tag
            rm = value
            if '(' in value and ')' in value:
                rm = value.split('(')
                self.value_tag = rm[0]
                rm = rm[1]
                rm.removesuffix(')')
            # split into values
            spl = rm.split(' ')
            parsed_spl = list(map(self.convert_str, spl))
            # convert to color
            if self.setter_type == SetterType.color_picker:
                # get optional alpha
                alpha: int = 255
                if len(parsed_spl) >= 4:
                    self.sets_opacity = True
                    alpha = self.convert_color(parsed_spl[3])
                return QColor(
                    self.convert_color(parsed_spl[0]),
                    self.convert_color(parsed_spl[1]),
                    self.convert_color(parsed_spl[2]),
                    alpha
                )
            return parsed_spl
        return value

    def __init__(self, data: dict):
        super().__init__(data=data)
        self.label_objects = None # for updating the qt label
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

        # color picker options
        if 'sets_opacity' in data:
            self.sets_opacity = data['sets_opacity']

        if 'default_value' in data:
            self.value = data['default_value']
        else:
            if self.setter_type == SetterType.toggle:
                self.value = False
            elif self.min_value != None:
                self.value = self.min_value
            elif self.max_value != None:
                self.value = self.max_value

        # convert values
        self.min_value = self.split_value(self.min_value)
        self.max_value = self.split_value(self.max_value)
        self.step = self.split_value(self.step)
        self.value = self.split_value(self.value)

    def get_stylesheet(self, color: QColor) -> str:
        return f"background-color: rgba({color.red()}, {color.green()}, {color.blue()}, {color.alphaF()}); border: 2px solid #3b3b3b;"

    # Converter functions
    def convert_float(self, value: float):
        if not self.is_float:
            return value
        return int(value * 1000)
    def convert_int(self, value: int):
        if not self.is_float:
            return value
        return float(value) / 1000.0
    def convert_str(self, value: str):
        # convert string to either float or int
        if self.is_float:
            return self.convert_float(float(value))
        if isinstance(value, int) or (isinstance(value, str) and value.isdigit() and not '.' in value):
            return int(value)
        else:
            self.is_float = self.setter_type == SetterType.slider
            return self.convert_float(float(value))
    def convert_color(self, value: float):
        return round(min(1, value) * 255)
    def convert_back(self, value):
        back_list = value
        if isinstance(value, QColor):
            # convert color back to string
            back_list = [str(value.redF()), str(value.greenF()), str(value.blueF())]
        elif not isinstance(value, list):
            return value
        elif isinstance(value, list):
            # convert values to strings
            for i in range(len(back_list)):
                back_list[i] = str(back_list[i])
        back_str = ' '.join(back_list)
        if self.value_tag != None:
            back_str = self.value_tag + "(" + back_str + ")"
        return back_str

    def get_parsed_value(self, value):
        if self.is_float:
            if isinstance(value, list):
                # convert list
                return list(map(self.convert_int, value))
            return self.convert_int(value)
        return value
    def get_value(self):
        return self.get_parsed_value(self.value)
    def get_min(self):
        return self.get_parsed_value(self.min_value)
    def get_max(self):
        return self.get_parsed_value(self.max_value)
    
    def update_value(self, nv: int, index: int=None):
        if isinstance(self.value, list):
            self.value[index] = nv
        else:
            self.value = nv
        if self.label_objects != None:
            if index != None:
                val = self.get_value()
                if isinstance(self.value, list):
                    val = val[index]
                self.label_objects[index].setText(f"{self.label}: {val}")
            else:
                self.label_objects.setText(f"{self.label}: {self.get_value()}")
    def update_color(self):
        color = QColorDialog.getColor(initial=self.value, options=QColorDialog.ColorDialogOption.ShowAlphaChannel)
        if color.isValid():
            self.value = color
            self.label_objects[0].setStyleSheet(self.get_stylesheet(color=color))

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
            # set opacity if it has that
            if self.sets_opacity and isinstance(self.value, QColor):
                set_xml_values(file=path, id=self.identifier, keys=[self.key, "opacity"], values=[self.convert_back(apply_val), str(self.value.alphaF())], use_ca_id=self.use_ca_id)
            else:
                set_xml_value(file=path, id=self.identifier, key=self.key, val=self.convert_back(apply_val), use_ca_id=self.use_ca_id)