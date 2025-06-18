import os
import uuid
import zipfile
import fnmatch

from json import load
from typing import Optional
from tempfile import TemporaryDirectory
from shutil import rmtree

from PySide6 import QtWidgets, QtCore, QtGui

from .tendie_file import TendieFile
from .template_options import OptionType, TemplateOption, ReplaceOption, RemoveOption, SetOption, PickerOption
from tweaks.posterboard.template_options import OptionType as TemplateOptionTypePB
from exceptions.posterboard_exceptions import PBTemplateException
from gui.custom_qt_elements.resizable_image_label import ResizableImageLabel
from devicemanagement.constants import Version

CURRENT_FORMAT = 2

class TemplateFile(TendieFile):
    options: list[TemplateOption]
    json_path: str
    tmp_dir: str = None

    author: str = "" # author of template
    domain: str = "" # domain to restore to
    description: Optional[str] = None # description to go under the file

    change_bundle_id: bool = False # whether or not the user can change the bundle id
    bundle_id: str = None # bundle id of the app if changable

    min_version: Optional[str] = None # minimum supported iOS version
    max_version: Optional[str] = None # maximum supported iOS version

    resources: list[str] = [] # list of file paths for embedded resources
    previews: dict[str, str] = {} # list of resources to use as previews
    preview_layout: str = "horizontal" # the direction to lay out the preview images

    banner_text: Optional[str] = None # text to go as a banner
    banner_stylesheet: Optional[str] = None # style sheet of the banner
    format_version: int = CURRENT_FORMAT # format version of config

    def __init__(self, path: str, device_version: str = None):
        super().__init__(path=path)
        self.options = []
        self.json_path = None

        # find the config.json file
        with zipfile.ZipFile(path, mode="r") as archive:
            for option in archive.namelist():
                if "config.json" in option.lower() and not "descriptor" in option.lower() and not "container" in option.lower():
                    self.json_path = option
                    break
            if self.json_path != None:
                file = archive.open(self.json_path)
                data = load(file)
                # load the options
                if not 'options' in data:
                    raise PBTemplateException(path, QtCore.QCoreApplication.tr("No options were found in the config. Make sure that it is in the correct format."))
                if not 'domain' in data:
                    raise PBTemplateException(path, QtCore.QCoreApplication.tr("This config does not have a valid domain!"))
                self.domain = data['domain']
                # add backwards compatibility for my mistake in the v5.2 betas
                if self.domain == "com.apple.PosterBoard":
                    self.domain = "AppDomain-com.apple.PosterBoard"
                self.format_version = int(data['format_version'])
                if self.format_version > CURRENT_FORMAT:
                    raise PBTemplateException(path, QtCore.QCoreApplication.tr("This config requires a newer version of Nugget."))
                self.name = data['title']
                self.author = data['author']
                if 'description' in data:
                    self.description = data['description']

                if 'min_version' in data:
                    self.min_version = data['min_version']
                    # check the device version
                    # TODO: need to make this check also happen when connected device is updated
                    if Version(self.min_version) > Version(device_version):
                        raise PBTemplateException(path, QtCore.QCoreApplication.tr("This template requires iOS {0}.\nYour iOS version (iOS {1}) is too outdated!").format(self.min_version, device_version))
                if 'max_version' in data:
                    self.max_version = data['max_version']
                    if Version(self.max_version) < Version(device_version):
                        raise PBTemplateException(path, QtCore.QCoreApplication.tr("This template requires iOS {0}.\nYour iOS version (iOS {1}) is too new!").format(self.max_version, device_version))

                # load the previews
                prevs = []
                if 'previews' in data:
                    prevs = data['previews']
                    if 'preview_layout' in data:
                        self.preview_layout = data['preview_layout']
                # load the banner
                if 'banner_text' in data:
                    self.banner_text = data['banner_text']
                    if 'banner_stylesheet' in data:
                        self.banner_stylesheet = data['banner_stylesheet']
                # load the resources
                if 'resources' in data:
                    self.resources = data['resources']
                    # open the resources and put them in temp files
                    rcs_path = self.json_path.removesuffix("config.json")
                    for resource in self.resources:
                        # handle wildcards
                        rc_pattern = rcs_path + resource
                        for rc_path in fnmatch.filter(archive.namelist(), rc_pattern):
                            rc_data = archive.read(rc_path)
                            if rc_data != None:
                                # write it to a temp file
                                if self.tmp_dir == None:
                                    self.tmp_dir = TemporaryDirectory()
                                rc_full_path = os.path.join(self.tmp_dir.name, rc_path)
                                os.makedirs(os.path.dirname(rc_full_path), exist_ok=True)
                                with open(rc_full_path, "wb") as rc_fp:
                                    rc_fp.write(rc_data)
                                # update the url in the banner stylesheet
                                clean_path = rc_path.replace(rcs_path, "")
                                if self.banner_stylesheet != None:
                                    self.banner_stylesheet = self.banner_stylesheet.replace(f"url({clean_path})", f"url({rc_full_path})")
                                # set the preview images
                                if clean_path in prevs:
                                    self.previews[clean_path] = rc_full_path

                for option in data['options']:
                    opt_type = OptionType[option['type']]
                    if opt_type == OptionType.replace:
                        self.options.append(ReplaceOption(data=option))
                    elif opt_type == OptionType.remove:
                        self.options.append(RemoveOption(data=option))
                    elif opt_type == OptionType.set:
                        self.options.append(SetOption(data=option))
                    elif opt_type == OptionType.picker:
                        self.options.append(PickerOption(data=option))
                    elif opt_type == OptionType.bundle_id:
                        self.change_bundle_id = True
                        self.bundle_id = self.domain.removeprefix("AppDomain-") # set default value to the bundle id in the domain
                    else:
                        raise PBTemplateException(path, QtCore.QCoreApplication.tr("Invalid option type in template"))
            else:
                raise PBTemplateException(path, QtCore.QCoreApplication.tr("No config.json found in file!"))
    
    def clean_files(self):
        if self.tmp_dir != None:
            try:
                rmtree(self.tmp_dir.name)
            except Exception as e:
                print(f"Error when removing temp dir: {str(e)}")

    def extract(self, output_dir: str):
        zip_output = os.path.join(output_dir, str(uuid.uuid4()))
        os.makedirs(zip_output)
        with zipfile.ZipFile(self.path, 'r') as zip_ref:
            zip_ref.extractall(zip_output)

        # apply the options
        parent_path = os.path.join(zip_output, os.path.dirname(self.json_path))
        for option in self.options:
            option.apply(container_path=parent_path)

    def get_chevron_icon(self, is_up: bool):
        if is_up:
            return QtGui.QIcon(":/icon/chevron.up.svg")
        return QtGui.QIcon(":/icon/chevron.down.svg")
    
    def update_bundle_id(self, new_id: str):
        self.bundle_id = new_id
        self.domain_lbl.setText(f" (AppDomain-{self.bundle_id})")

    def create_ui(self, window, tweak, widgets: dict, templateLayout: QtWidgets.QVBoxLayout):
        if self.loaded:
            return
        widget = QtWidgets.QWidget()
        widgets[self] = widget
        options_widget = QtWidgets.QWidget(widget)

        # create the icon/label + delete button
        left_widget = QtWidgets.QWidget(widget)
        title_widget = QtWidgets.QWidget(left_widget)
        title_layout = QtWidgets.QVBoxLayout()
        if self.domain == "com.apple.PosterBoard":
            titleBtn = QtWidgets.QToolButton(title_widget)
            titleBtn.setIcon(QtGui.QIcon(self.get_icon()))
            titleBtn.setIconSize(QtCore.QSize(20, 20))
            titleBtn.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            titleBtn.setText(f"   {self.name}")
            titleBtn.setStyleSheet("QToolButton {\n    background-color: transparent;\n	icon-size: 20px; text-align:left;\n}")
            titleBtn.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            title_layout.addWidget(titleBtn)
        else:
            title_lbl = QtWidgets.QLabel(title_widget)
            title_lbl.setText(self.name)
            title_layout.addWidget(title_lbl)
        # author label
        auth_lbl = QtWidgets.QLabel(title_widget)
        auth_lbl.setText(f"by {self.author}")
        auth_lbl.setStyleSheet("QLabel { font-size: 12px; }")
        title_layout.addWidget(auth_lbl)
        title_widget.setLayout(title_layout)
        # domain label
        self.domain_lbl = QtWidgets.QLabel(left_widget)
        self.domain_lbl.setText(f" ({self.domain})")
        chevron = QtWidgets.QToolButton(left_widget)
        chevron.setIcon(self.get_chevron_icon(is_up=True)) # for opening/closing the options
        chevron.setStyleSheet("QToolButton {\n    background-color: transparent;\n	icon-size: 20px;\n}")
        chevron.clicked.connect(lambda _, get_chev=self.get_chevron_icon: (
            options_widget.setVisible(not options_widget.isVisible()),
            chevron.setIcon(get_chev(options_widget.isVisible()))
        ))
        spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        delBtn = QtWidgets.QToolButton(left_widget)
        delBtn.setIcon(QtGui.QIcon(":/icon/trash.svg"))
        delBtn.clicked.connect(lambda _, file=self: (
            widgets[file].deleteLater(),
            file.clean_files(),
            tweak.templates.remove(file)
        ))
        # align to top layout
        left_layout = QtWidgets.QHBoxLayout()
        left_layout.setContentsMargins(0, 0, 4, 0)
        left_layout.addWidget(title_widget)
        left_layout.addWidget(self.domain_lbl)
        left_layout.addItem(spacer)
        left_layout.addWidget(chevron)
        left_layout.addWidget(delBtn)
        left_widget.setLayout(left_layout)
        left_widget.setMinimumHeight(60)
        left_widget.setMaximumHeight(60)

        # main layout
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(4, 2, 4, 2)
        layout.addWidget(left_widget)
        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        line.setStyleSheet("QFrame {\n	color: #414141;\n}")
        layout.addWidget(line)

        # create options
        # options_widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        opt_layout = QtWidgets.QVBoxLayout()
        opt_layout.setContentsMargins(3, 0, 0, 0)

        # create previews
        prevs: dict[str, QtWidgets.QLabel] = {}
        if len(self.previews) > 0:
            prev_widget = QtWidgets.QWidget(options_widget)
            prev_widget.setMinimumHeight(250)
            prev_widget.setMaximumHeight(250)
            prev_widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            if self.preview_layout == "stacked":
                prev_layout = QtWidgets.QStackedLayout()
                prev_layout.setStackingMode(QtWidgets.QStackedLayout.StackAll)
            else:
                prev_layout = QtWidgets.QHBoxLayout()
            prev_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
            for prev in self.previews.keys():
                new_prev = ResizableImageLabel(prev_widget)
                new_prev.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                pixmap = QtGui.QPixmap(self.previews[prev])
                new_prev.setPixmap(pixmap)
                # new_prev.setScaledContents(True)
                prev_layout.addWidget(new_prev)
                prevs[prev] = new_prev
            prev_widget.setLayout(prev_layout)
            opt_layout.addWidget(prev_widget)

        # make banner
        if self.banner_text != None:
            banner = QtWidgets.QLabel(options_widget)
            banner.setText(self.banner_text)
            banner.setAlignment(QtCore.Qt.AlignCenter)
            if self.banner_stylesheet != None:
                banner.setStyleSheet(self.banner_stylesheet)
            opt_layout.addWidget(banner)
        # make description
        if self.description != None:
            descr = QtWidgets.QLabel(options_widget)
            descr.setText(self.description)
            opt_layout.addWidget(descr)

        # bundle id changing
        if self.change_bundle_id:
            # textbox input
            bx_widget = QtWidgets.QWidget(options_widget)
            bx_layout = QtWidgets.QVBoxLayout(options_widget)
            bx_layout.setContentsMargins(0, 2, 0, 2)
            bx_lbl = QtWidgets.QLabel(bx_widget)
            bx_lbl.setText("App bundle id:")
            bx_layout.addWidget(bx_lbl)
            textbox = QtWidgets.QLineEdit(bx_widget)
            textbox.setPlaceholderText(QtCore.QCoreApplication.tr("Bundle id (default: {0})").format(self.domain.removeprefix("AppDomain-")))
            textbox.setText(self.bundle_id)
            textbox.textEdited.connect(self.update_bundle_id)
            bx_layout.addWidget(textbox)
            bx_widget.setLayout(bx_layout)
            opt_layout.addWidget(bx_widget)

        for option in self.options:
            # provide the window
            if option.type == TemplateOptionTypePB.replace and option.window == None:
                option.window = window#.set_window(self.window)
            option.create_interface(options_widget=options_widget, options_layout=opt_layout)
            # add the previews and update it
            option.add_potential_preview_lbls(prevs)
            option.update_preview()

        options_widget.setLayout(opt_layout)

        # finish the main layout
        layout.addWidget(options_widget)
        # Add the widget to the mainLayout
        widget.setLayout(layout)
        templateLayout.addWidget(widget)
        self.loaded = True