from . import TemplateOption

import os
import glob
from dataclasses import dataclass
from typing import Optional
from enum import Enum
from PySide6.QtGui import QColor
from PySide6 import QtWidgets, QtCore

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
    value_type = int # value types

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

        if 'value_type' in data:
            self.value_type = data['value_type']

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

    # Creating UI
    def get_stylesheet(self, color: QColor) -> str:
        return f"background-color: rgba({color.red()}, {color.green()}, {color.blue()}, {color.alphaF()}); border: 2px solid #3b3b3b;"
    
    def create_interface(self, options_widget: QtWidgets.QWidget, options_layout: QtWidgets.QVBoxLayout):
        if self.setter_type == SetterType.toggle:
            # remove object/setter toggle
            remove_chk = QtWidgets.QCheckBox(options_widget)
            remove_chk.setText(self.label)
            remove_chk.setChecked(self.value)
            remove_chk.toggled.connect(self.set_option)
            options_layout.addWidget(remove_chk)
        elif self.setter_type == SetterType.textbox:
            # textbox input
            bx_widget = QtWidgets.QWidget(options_widget)
            bx_layout = QtWidgets.QVBoxLayout(options_widget)
            bx_layout.setContentsMargins(0, 2, 0, 2)
            bx_lbl = QtWidgets.QLabel(bx_widget)
            bx_lbl.setText(self.label)
            bx_layout.addWidget(bx_lbl)
            textbox = QtWidgets.QLineEdit(bx_widget)
            textbox.setPlaceholderText("Value")
            textbox.setText(self.value)
            textbox.textEdited.connect(self.update_value)
            bx_layout.addWidget(textbox)
            bx_widget.setLayout(bx_layout)
            options_layout.addWidget(bx_widget)
        elif self.setter_type == SetterType.slider:
            vals = self.value
            self.label_objects = []
            list_len = 1
            if isinstance(vals, list):
                list_len = len(vals)
            else:
                vals = [vals]
            for i in range(list_len):
                # slider input
                slid_widget = QtWidgets.QWidget(options_widget)
                slid_layout = QtWidgets.QVBoxLayout(options_widget)
                slid_layout.setContentsMargins(0, 2, 0, 2)
                slid_lbl = QtWidgets.QLabel(slid_widget)
                slid_lbl.setText(f"{self.label}: {vals[i]}")
                slid_layout.addWidget(slid_lbl)
                self.label_objects.append(slid_lbl)
                # widget for min and max values with slider
                val_widget = QtWidgets.QWidget(slid_widget)
                val_layout = QtWidgets.QHBoxLayout(slid_widget)
                min_lbl = QtWidgets.QLabel(val_widget)

                min_val_fixed = self.min_value
                min_val = self.convert_float(self.min_value)
                max_val_fixed = self.max_value
                max_val = self.convert_float(self.max_value)
                step = self.convert_float(self.step)
                val = self.convert_float(self.value)
                if isinstance(min_val, list):
                    min_val_fixed = min_val_fixed[i]
                    min_val = min_val[i]
                    max_val_fixed = max_val_fixed[i]
                    max_val = max_val[i]
                    step = step[i]
                    val = val[i]
                min_lbl.setText(str(min_val_fixed))
                val_layout.addWidget(min_lbl)
                slider = QtWidgets.QSlider(val_widget)
                slider.setMinimum(min_val)
                slider.setMaximum(max_val)
                slider.setTickInterval(step)
                slider.setSingleStep(step)
                slider.setValue(val)
                slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
                slider.valueChanged.connect(lambda v, idx=i: self.update_value(v, idx))
                val_layout.addWidget(slider)
                max_lbl = QtWidgets.QLabel(val_widget)
                max_lbl.setText(str(max_val_fixed))
                val_layout.addWidget(max_lbl)
                # add to layout and widget
                val_widget.setLayout(val_layout)
                slid_layout.addWidget(val_widget)
                slid_widget.setLayout(slid_layout)
                options_layout.addWidget(slid_widget)
        elif self.setter_type == SetterType.color_picker:
            # color picker input
            col_widget = QtWidgets.QWidget(options_widget)
            col_layout = QtWidgets.QHBoxLayout(options_widget)
            col_layout.setContentsMargins(0, 2, 0, 2)
            col_lbl = QtWidgets.QLabel(col_widget)
            col_lbl.setText(self.label)
            col_layout.addWidget(col_lbl)
            col_picker_bg = QtWidgets.QWidget(col_widget)
            col_picker_bg_layout = QtWidgets.QStackedLayout(col_widget)
            col_picker_bg_layout.setStackingMode(QtWidgets.QStackedLayout.StackAll)
            col_picker_img = QtWidgets.QToolButton(col_picker_bg)
            col_picker_img.setText("")
            col_picker_img.setStyleSheet("background-image: url(:/gui/transparent.png); border-radius: 10px;")
            col_picker = QtWidgets.QToolButton(col_picker_bg)
            col_picker.setText("")
            self.label_objects = [col_picker]
            col_picker.setStyleSheet(self.get_stylesheet(color=self.value))
            col_picker.clicked.connect(self.update_color)
            col_picker_bg_layout.addWidget(col_picker_img)
            col_picker_bg_layout.addWidget(col_picker)
            col_picker_bg.setLayout(col_picker_bg_layout)
            col_picker_bg.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            col_layout.addWidget(col_picker_bg)
            col_widget.setLayout(col_layout)
            options_layout.addWidget(col_widget)

    # correcting the slider position
    def correct_slider_pos(self, pos: int, index: int = 0):
        # check if slider is divisible. If not, set it to a divisible value
        step = self.convert_float(self.step)
        if isinstance(step, list):
            step = step[index]
        if pos%step != 0:
            # pos needs updated
            min_val = self.convert_float(self.min_value)
            max_val = self.convert_float(self.max_value)
            if isinstance(min_val, list):
                min_val = min_val[index]
                max_val = max_val[index]
            if pos%step < step/2:
                # set to left
                pos = pos - (pos%step)
            else:
                # set to right
                pos = pos + (step - (pos%step))
            # make sure it is within bounds
            if pos < min_val:
                pos = min_val
            elif pos > max_val:
                pos = max_val
        return pos

    # Converter functions
    def convert_float(self, value: float) -> int:
        if self.value_type != "float":
            return value
        if isinstance(value, list):
            new_list = value
            for i in range(len(new_list)):
                new_list[i] = self.convert_float(new_list[i])
            return new_list
        return int(value * 1000)
    def convert_str(self, value: str):
        # convert string to either float or int
        if self.value_type == "float":
            return float(value)
        if isinstance(value, int) or (isinstance(value, str) and value.isdigit() and not '.' in value):
            return int(value)
        else:
            if self.setter_type == SetterType.slider:
                self.value_type == "float"
            return float(value)
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

    # def get_parsed_value(self, value):
    #     if self.value_type == "float":
    #         if isinstance(value, list):
    #             # convert list
    #             return list(map(self.convert_int, value))
    #         return self.convert_int(value)
    #     return value
    # def get_value(self):
    #     return self.get_parsed_value(self.value)
    # def get_min(self):
    #     return self.get_parsed_value(self.min_value)
    # def get_max(self):
    #     return self.get_parsed_value(self.max_value)
    
    def update_value(self, nv: int, index: int=None):
        if self.setter_type == SetterType.slider:
            # correct it to the step
            nv = self.correct_slider_pos(nv, index)
            if self.value_type == "float":
                nv = float(nv) / 1000.0
        if isinstance(self.value, list):
            self.value[index] = nv
        else:
            self.value = nv
        if self.label_objects != None:
            if index != None:
                val = self.value
                if isinstance(self.value, list):
                    val = val[index]
                self.label_objects[index].setText(f"{self.label}: {val}")
            else:
                self.label_objects.setText(f"{self.label}: {self.get_value()}")
    def update_color(self):
        color = QtWidgets.QColorDialog.getColor(initial=self.value, options=QtWidgets.QColorDialog.ColorDialogOption.ShowAlphaChannel)
        if color.isValid():
            self.value = color
            self.label_objects[0].setStyleSheet(self.get_stylesheet(color=color))

    def apply(self, container_path: str):
        apply_val = self.value
        if self.setter_type == SetterType.toggle:
            if self.inverted:
                # invert toggle
                apply_val = not apply_val
            if apply_val and self.toggle_on_value != None:
                apply_val = self.toggle_on_value
            elif not apply_val and self.toggle_off_value != None:
                apply_val = self.toggle_off_value
        # wildcard support
        for file in self.files:
            path = os.path.join(container_path, *file.split('/'))
            for full_path in glob.glob(path, recursive=True):
                # set opacity if it has that
                if self.sets_opacity and isinstance(self.value, QColor):
                    set_xml_values(file=full_path, id=self.identifier, keys=[self.key, "opacity"], values=[self.convert_back(apply_val), str(self.value.alphaF())], use_ca_id=self.use_ca_id)
                else:
                    set_xml_value(file=full_path, id=self.identifier, key=self.key, val=self.convert_back(apply_val), use_ca_id=self.use_ca_id)