from PySide6 import QtCore, QtWidgets, QtGui
import webbrowser

from ..page import Page
from qt.ui_mainwindow import Ui_Nugget
from gui.dialogs import PBHelpDialog
from gui.multicombobox import MultiComboBox

from tweaks.tweaks import tweaks
from tweaks.posterboard.template_options import OptionType as TemplateOptionTypePB
from tweaks.posterboard.template_options import SetterType

class PosterboardPage(Page):
    def __init__(self, window, ui: Ui_Nugget):
        super().__init__()
        self.window = window
        self.ui = ui
        self.pb_mainLayout = None
        self.pb_templateLayout = None

        # set up the dropdown
        self.ui.resetPBDrp = MultiComboBox(self.ui.pbPagePicker, updateAction=self.on_update_picker)
        self.ui.resetPBDrp.setMinimumWidth(165)
        self.ui.resetPBDrp.setMinimumHeight(25)
        self.ui.resetPBDrp.setMaximumWidth(200)
        self.ui.resetPBDrp.setMaximumHeight(30)
        self.ui.resetPBDrp.addItems(["Collections", "Suggested Photos", "Gallery Cache"])
        self.ui.resetPBDrp.lineEdit().setText("  None")
        self.ui.resetPBDrp.setStyleSheet("QWidget { background-color: #3b3b3b; border: 2px solid #3b3b3b; border-radius: 5px; }")# QAbstractItemView::indicator:checked { background-color: rgba(0, 0, 255, 0.3); border-radius: 4px; }")
        self.ui.pbPagePicker.layout().addWidget(self.ui.resetPBDrp)

    def on_update_picker(self, selected_items: list[str]):
        tweaks["PosterBoard"].resetModes = selected_items

    def load_page(self):
        self.ui.modifyPosterboardsChk.toggled.connect(self.on_modifyPosterboardsChk_clicked)
        self.ui.tendiesPageBtn.clicked.connect(self.on_tendiesPageBtn_clicked)
        self.ui.templatePageBtn.clicked.connect(self.on_templatePageBtn_clicked)
        self.ui.videoPageBtn.clicked.connect(self.on_videoPageBtn_clicked)

        self.ui.importTendiesBtn.clicked.connect(self.on_importTendiesBtn_clicked)

        self.ui.importTemplateBtn.clicked.connect(self.on_importTemplatesBtn_clicked)

        self.ui.chooseThumbBtn.clicked.connect(self.on_chooseThumbBtn_clicked)
        self.ui.chooseVideoBtn.clicked.connect(self.on_chooseVideoBtn_clicked)
        self.ui.caVideoChk.toggled.connect(self.on_caVideoChk_toggled)
        self.ui.reverseLoopChk.toggled.connect(self.on_reverseLoopChk_toggled)
        self.ui.useForegroundChk.toggled.connect(self.on_useForegroundChk_toggled)
        self.ui.chooseThumbBtn.hide()
        self.ui.pbVideoThumbLbl.hide()
        
        self.ui.findPBBtn.clicked.connect(self.on_findPBBtn_clicked)
        self.ui.pbHelpBtn.clicked.connect(self.on_pbHelpBtn_clicked)

    ## ACTIONS
    def delete_pb_file(self, file, widget):
        if file in tweaks["PosterBoard"].tendies:
            tweaks["PosterBoard"].tendies.remove(file)
        widget.deleteLater()

    def create_title_widget(self, tendie, widget: QtWidgets.QWidget) -> QtWidgets.QToolButton:
        titleBtn = QtWidgets.QToolButton(widget)
        titleBtn.setIcon(QtGui.QIcon(tendie.get_icon()))
        titleBtn.setIconSize(QtCore.QSize(20, 20))
        titleBtn.setText(f"   {tendie.name}")
        titleBtn.setStyleSheet("QToolButton {\n    background-color: transparent;\n	icon-size: 20px;\n}")
        titleBtn.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        titleBtn.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        return titleBtn

    def load_pb_tendies(self):
        if len(tweaks["PosterBoard"].tendies) == 0:
            return
        
        if self.pb_mainLayout == None:
            # Create scroll layout
            self.pb_mainLayout = QtWidgets.QVBoxLayout()
            self.pb_mainLayout.setContentsMargins(0, 0, 0, 0)
            self.pb_mainLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
            # Create a QWidget to act as the container for the scroll area
            scrollWidget = QtWidgets.QWidget()

            # Set the main layout (containing all the widgets) on the scroll widget
            scrollWidget.setLayout(self.pb_mainLayout)

            # Create a QScrollArea to hold the content widget (scrollWidget)
            scrollArea = QtWidgets.QScrollArea()
            scrollArea.setWidgetResizable(True)  # Allow the content widget to resize within the scroll area
            scrollArea.setFrameStyle(QtWidgets.QScrollArea.NoFrame)  # Remove the outline from the scroll area

            # Set the scrollWidget as the content widget of the scroll area
            scrollArea.setWidget(scrollWidget)

            # Set the size policy of the scroll area to expand in both directions
            scrollArea.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

            # Set the scroll area as the central widget of the main window
            scrollLayout = QtWidgets.QVBoxLayout()
            scrollLayout.setContentsMargins(0, 0, 0, 0)
            scrollLayout.addWidget(scrollArea)
            self.ui.pbFilesList.setLayout(scrollLayout)

        widgets = {}
        # Iterate through the files
        for tendie in tweaks["PosterBoard"].tendies:
            if tendie.loaded:
                continue
            widget = QtWidgets.QWidget()
            widgets[tendie] = widget

            # create the icon/label
            titleBtn = self.create_title_widget(tendie=tendie, widget=widget)

            delBtn = QtWidgets.QToolButton(widget)
            delBtn.setIcon(QtGui.QIcon(":/icon/trash.svg"))
            delBtn.clicked.connect(lambda _, file=tendie: (widgets[file].deleteLater(), tweaks["PosterBoard"].tendies.remove(file)))

            spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            # main layout
            layout = QtWidgets.QHBoxLayout(widget)
            layout.setContentsMargins(0, 0, 0, 3)
            layout.addWidget(titleBtn)
            layout.addItem(spacer)
            layout.addWidget(delBtn)
            # Add the widget to the mainLayout
            widget.setLayout(layout)
            self.pb_mainLayout.addWidget(widget)
            tendie.loaded = True

    def get_chevron_icon(self, is_up: bool):
        if is_up:
            return QtGui.QIcon(":/icon/chevron.up.svg")
        return QtGui.QIcon(":/icon/chevron.down.svg")

    def load_pb_templates(self):
        if len(tweaks["PosterBoard"].templates) == 0:
            return
        if self.pb_templateLayout == None:
            # Create scroll layout
            self.pb_templateLayout = QtWidgets.QVBoxLayout()
            self.pb_templateLayout.setContentsMargins(0, 0, 0, 0)
            self.pb_templateLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
            # Create a QWidget to act as the container for the scroll area
            scrollWidget = QtWidgets.QWidget()

            # Set the main layout (containing all the widgets) on the scroll widget
            scrollWidget.setLayout(self.pb_templateLayout)

            # Create a QScrollArea to hold the content widget (scrollWidget)
            scrollArea = QtWidgets.QScrollArea()
            scrollArea.setWidgetResizable(True)  # Allow the content widget to resize within the scroll area
            scrollArea.setFrameStyle(QtWidgets.QScrollArea.NoFrame)  # Remove the outline from the scroll area

            # Set the scrollWidget as the content widget of the scroll area
            scrollArea.setWidget(scrollWidget)

            # Set the size policy of the scroll area to expand in both directions
            scrollArea.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

            # Set the scroll area as the central widget of the main window
            scrollLayout = QtWidgets.QVBoxLayout()
            scrollLayout.setContentsMargins(0, 0, 0, 0)
            scrollLayout.addWidget(scrollArea)
            self.ui.pbTemplatesList.setLayout(scrollLayout)
        
        widgets = {}
        # Iterate through the templates
        for template in tweaks["PosterBoard"].templates:
            if template.loaded:
                continue
            widget = QtWidgets.QWidget()
            widgets[template] = widget
            options_widget = QtWidgets.QWidget(widget)

            # create the icon/label + delete button
            left_widget = QtWidgets.QWidget(widget)
            titleBtn = self.create_title_widget(tendie=template, widget=widget)
            chevron = QtWidgets.QToolButton(widget)
            chevron.setIcon(self.get_chevron_icon(is_up=True)) # for opening/closing the options
            chevron.setStyleSheet("QToolButton {\n    background-color: transparent;\n	icon-size: 20px;\n}")
            chevron.clicked.connect(lambda _, get_chev=self.get_chevron_icon: (
                options_widget.setVisible(not options_widget.isVisible()),
                chevron.setIcon(get_chev(options_widget.isVisible()))
            ))
            spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            delBtn = QtWidgets.QToolButton(widget)
            delBtn.setIcon(QtGui.QIcon(":/icon/trash.svg"))
            delBtn.clicked.connect(lambda _, file=template: (
                widgets[file].deleteLater(),
                tweaks["PosterBoard"].templates.remove(file)
            ))
            # align to top layout
            left_layout = QtWidgets.QHBoxLayout(widget)
            left_layout.setContentsMargins(0, 0, 4, 0)
            left_layout.addWidget(titleBtn)
            left_layout.addItem(spacer)
            left_layout.addWidget(chevron)
            left_layout.addWidget(delBtn)
            left_widget.setLayout(left_layout)
            left_widget.setMinimumHeight(40)
            left_widget.setMaximumHeight(40)

            # create options
            # options_widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
            opt_layout = QtWidgets.QVBoxLayout()
            opt_layout.setContentsMargins(3, 0, 0, 0)
            for option in template.options:
                if option.type == TemplateOptionTypePB.replace:
                    # replacable object
                    repl_widget = QtWidgets.QWidget(options_widget)
                    repl_layout = QtWidgets.QHBoxLayout(options_widget)
                    repl_layout.setContentsMargins(0, 2, 0, 2)
                    repl_lbl = QtWidgets.QLabel(repl_widget)
                    req_label = ""
                    if option.required:
                        req_label = "* "
                    repl_lbl.setText(f"{req_label}{option.label}")
                    repl_layout.addWidget(repl_lbl)
                    # button for importing files
                    repl_btn = QtWidgets.QToolButton(options_widget)
                    repl_btn.setIcon(QtGui.QIcon(":/icon/import.svg"))
                    repl_btn.setIconSize(QtCore.QSize(20, 20))
                    btn_lbl = option.button_label
                    if btn_lbl == None:
                        btn_lbl = f"Import {option.allowed_files}"
                    repl_btn.setText(btn_lbl)
                    repl_btn.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
                    repl_btn.clicked.connect(lambda _, opt=option: (self.on_importReplaceBtn_clicked(opt)))
                    repl_layout.addWidget(repl_btn)
                    repl_widget.setLayout(repl_layout)
                    opt_layout.addWidget(repl_widget)
                elif option.type == TemplateOptionTypePB.remove or (option.type == TemplateOptionTypePB.set and option.setter_type == SetterType.toggle):
                    # remove object/setter toggle
                    remove_chk = QtWidgets.QCheckBox(options_widget)
                    remove_chk.setText(option.label)
                    remove_chk.setChecked(option.value)
                    remove_chk.toggled.connect(option.set_option)
                    opt_layout.addWidget(remove_chk)
                elif option.type == TemplateOptionTypePB.set and option.setter_type == SetterType.textbox:
                    # textbox input
                    bx_widget = QtWidgets.QWidget(options_widget)
                    bx_layout = QtWidgets.QVBoxLayout(options_widget)
                    bx_layout.setContentsMargins(0, 2, 0, 2)
                    bx_lbl = QtWidgets.QLabel(bx_widget)
                    bx_lbl.setText(option.label)
                    bx_layout.addWidget(bx_lbl)
                    textbox = QtWidgets.QLineEdit(bx_widget)
                    textbox.setPlaceholderText("Value")
                    textbox.setText(option.value)
                    textbox.textEdited.connect(option.update_value)
                    bx_layout.addWidget(textbox)
                    bx_widget.setLayout(bx_layout)
                    opt_layout.addWidget(bx_widget)
                elif option.type == TemplateOptionTypePB.set and option.setter_type == SetterType.slider:
                    vals = option.get_value()
                    option.label_objects = []
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
                        slid_lbl.setText(f"{option.label}: {vals[i]}")
                        slid_layout.addWidget(slid_lbl)
                        option.label_objects.append(slid_lbl)
                        # widget for min and max values with slider
                        val_widget = QtWidgets.QWidget(slid_widget)
                        val_layout = QtWidgets.QHBoxLayout(slid_widget)
                        min_lbl = QtWidgets.QLabel(val_widget)

                        min_val_fixed = option.get_min()
                        min_val = option.min_value
                        max_val_fixed = option.get_max()
                        max_val = option.max_value
                        step = option.step
                        val = option.value
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
                        slider.setSingleStep(step)
                        slider.setValue(val)
                        slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
                        slider.valueChanged.connect(lambda v, idx=i: option.update_value(v, idx))
                        val_layout.addWidget(slider)
                        max_lbl = QtWidgets.QLabel(val_widget)
                        max_lbl.setText(str(max_val_fixed))
                        val_layout.addWidget(max_lbl)
                        # add to layout and widget
                        val_widget.setLayout(val_layout)
                        slid_layout.addWidget(val_widget)
                        slid_widget.setLayout(slid_layout)
                        opt_layout.addWidget(slid_widget)
                elif option.type == TemplateOptionTypePB.set and option.setter_type == SetterType.color_picker:
                    # color picker input
                    col_widget = QtWidgets.QWidget(options_widget)
                    col_layout = QtWidgets.QHBoxLayout(options_widget)
                    col_layout.setContentsMargins(0, 2, 0, 2)
                    col_lbl = QtWidgets.QLabel(col_widget)
                    col_lbl.setText(option.label)
                    col_layout.addWidget(col_lbl)
                    col_picker_bg = QtWidgets.QWidget(col_widget)
                    col_picker_bg_layout = QtWidgets.QStackedLayout(col_widget)
                    col_picker_bg_layout.setStackingMode(QtWidgets.QStackedLayout.StackAll)
                    col_picker_img = QtWidgets.QToolButton(col_picker_bg)
                    col_picker_img.setText("")
                    col_picker_img.setStyleSheet("background-image: url(:/gui/transparent.png); border-radius: 10px;")
                    col_picker = QtWidgets.QToolButton(col_picker_bg)
                    col_picker.setText("")
                    option.label_objects = [col_picker]
                    col_picker.setStyleSheet(option.get_stylesheet(color=option.value))
                    col_picker.clicked.connect(option.update_color)
                    col_picker_bg_layout.addWidget(col_picker_img)
                    col_picker_bg_layout.addWidget(col_picker)
                    col_picker_bg.setLayout(col_picker_bg_layout)
                    col_picker_bg.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                    col_layout.addWidget(col_picker_bg)
                    col_widget.setLayout(col_layout)
                    opt_layout.addWidget(col_widget)

            options_widget.setLayout(opt_layout)

            # main layout
            layout = QtWidgets.QVBoxLayout(widget)
            layout.setContentsMargins(4, 2, 4, 2)
            layout.addWidget(left_widget)
            line = QtWidgets.QFrame()
            line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
            line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
            line.setStyleSheet("QFrame {\n	color: #414141;\n}")
            layout.addWidget(line)
            layout.addWidget(options_widget)
            # Add the widget to the mainLayout
            widget.setLayout(layout)
            self.pb_templateLayout.addWidget(widget)
            template.loaded = True

    def on_modifyPosterboardsChk_clicked(self, checked: bool):
        tweaks["PosterBoard"].set_enabled(checked)
        self.ui.pbPages.setDisabled(not checked)

    # PB Pages Selectors
    def on_tendiesPageBtn_clicked(self):
        self.ui.tendiesPageBtn.setChecked(True)
        self.ui.templatePageBtn.setChecked(False)
        self.ui.videoPageBtn.setChecked(False)
        self.ui.pbPages.setCurrentIndex(0)
    def on_templatePageBtn_clicked(self):
        self.ui.tendiesPageBtn.setChecked(False)
        self.ui.templatePageBtn.setChecked(True)
        self.ui.videoPageBtn.setChecked(False)
        self.ui.pbPages.setCurrentIndex(1)
    def on_videoPageBtn_clicked(self):
        self.ui.tendiesPageBtn.setChecked(False)
        self.ui.templatePageBtn.setChecked(False)
        self.ui.videoPageBtn.setChecked(True)
        self.ui.pbPages.setCurrentIndex(2)

    def on_importReplaceBtn_clicked(self, option):
        selected_file, _ = QtWidgets.QFileDialog.getOpenFileName(self.window, "Select Template File", "", option.allowed_files, options=QtWidgets.QFileDialog.ReadOnly)
        if selected_file != None and selected_file != "":
            option.value = selected_file
    
    # Tendies Page
    def on_importTendiesBtn_clicked(self):
        selected_files, _ = QtWidgets.QFileDialog.getOpenFileNames(self.window, "Select PosterBoard Files", "", "Zip Files (*.tendies)", options=QtWidgets.QFileDialog.ReadOnly)
        self.ui.resetPBDrp.deselectAll()
        if selected_files != None and len(selected_files) > 0:
            # user selected files, add them
            for file in selected_files:
                if not tweaks["PosterBoard"].add_tendie(file):
                    # alert that there are too many
                    detailsBox = QtWidgets.QMessageBox()
                    detailsBox.setIcon(QtWidgets.QMessageBox.Critical)
                    detailsBox.setWindowTitle("Error!")
                    detailsBox.setText("You selected too many descriptors! The limit is 10.")
                    detailsBox.exec()
                    break
            self.load_pb_tendies()

    # Templates Page
    def on_importTemplatesBtn_clicked(self):
        selected_files, _ = QtWidgets.QFileDialog.getOpenFileNames(self.window, "Select PosterBoard Template Files", "", "Zip Files (*.batter)", options=QtWidgets.QFileDialog.ReadOnly)
        self.ui.resetPBDrp.deselectAll()
        if selected_files != None and len(selected_files) > 0:
            # user selected files, add them
            for file in selected_files:
                if not tweaks["PosterBoard"].add_template(file):
                    # alert that there are too many
                    detailsBox = QtWidgets.QMessageBox()
                    detailsBox.setIcon(QtWidgets.QMessageBox.Critical)
                    detailsBox.setWindowTitle("Error!")
                    detailsBox.setText("You selected too many descriptors! The limit is 10.")
                    detailsBox.exec()
                    break
            self.load_pb_templates()
    
    # Video Page
    def on_chooseThumbBtn_clicked(self):
        selected_file, _ = QtWidgets.QFileDialog.getOpenFileName(self.window, "Select Image File", "", "Image Files (*.heic)", options=QtWidgets.QFileDialog.ReadOnly)
        self.ui.resetPBDrp.deselectAll()
        if selected_file != None and selected_file != "":
            tweaks["PosterBoard"].videoThumbnail = selected_file
            self.ui.pbVideoThumbLbl.setText(f"Current Thumbnail: {selected_file}")
        else:
            tweaks["PosterBoard"].videoThumbnail = None
            self.ui.pbVideoThumbLbl.setText("Current Thumbnail: None")
    def on_chooseVideoBtn_clicked(self):
        selected_file, _ = QtWidgets.QFileDialog.getOpenFileName(self.window, "Select Video File", "", "Video Files (*.mov *.mp4 *.mkv)", options=QtWidgets.QFileDialog.ReadOnly)
        self.ui.resetPBDrp.deselectAll()
        if selected_file != None and selected_file != "":
            tweaks["PosterBoard"].videoFile = selected_file
            self.ui.pbVideoLbl.setText(f"Current Video: {selected_file}")
        else:
            tweaks["PosterBoard"].videoFile = None
            self.ui.pbVideoLbl.setText("Current Video: None")
    def on_caVideoChk_toggled(self, checked: bool):
        tweaks["PosterBoard"].loop_video = checked
        # hide thumbnail button and label
        if checked:
            self.ui.chooseThumbBtn.hide()
            self.ui.pbVideoThumbLbl.hide()
            self.ui.clearSuggestedBtn.hide()
            self.ui.reverseLoopChk.show()
            self.ui.useForegroundChk.show()
        else:
            self.ui.chooseThumbBtn.show()
            self.ui.pbVideoThumbLbl.show()
            self.ui.clearSuggestedBtn.show()
            self.ui.reverseLoopChk.hide()
            self.ui.useForegroundChk.hide()
    def on_reverseLoopChk_toggled(self, checked: bool):
        tweaks["PosterBoard"].reverse_video = checked
    def on_useForegroundChk_toggled(self, checked: bool):
        tweaks["PosterBoard"].use_foreground = checked

    def on_findPBBtn_clicked(self):
        webbrowser.open_new_tab("https://cowabun.ga/wallpapers")

    def on_pbHelpBtn_clicked(self):
        dialog = PBHelpDialog()
        dialog.exec()