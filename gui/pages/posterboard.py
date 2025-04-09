from PySide6 import QtCore, QtWidgets, QtGui
import webbrowser

from .page import Page
from qt.ui_mainwindow import Ui_Nugget
from gui.dialogs import PBHelpDialog

from tweaks.tweaks import tweaks
from tweaks.posterboard.template_options import OptionType as TemplateOptionTypePB

class PosterboardPage(Page):
    def __init__(self, window, ui: Ui_Nugget):
        super().__init__()
        self.window = window
        self.ui = ui
        self.pb_mainLayout = None
        self.pb_templateLayout = None

    def load_page(self):
        self.ui.modifyPosterboardsChk.toggled.connect(self.on_modifyPosterboardsChk_clicked)
        self.ui.tendiesPageBtn.clicked.connect(self.on_tendiesPageBtn_clicked)
        self.ui.templatePageBtn.clicked.connect(self.on_templatePageBtn_clicked)
        self.ui.videoPageBtn.clicked.connect(self.on_videoPageBtn_clicked)

        self.ui.importTendiesBtn.clicked.connect(self.on_importTendiesBtn_clicked)
        self.ui.resetPRBExtBtn.clicked.connect(self.on_resetPRBExtBtn_clicked)
        self.ui.deleteAllDescriptorsBtn.clicked.connect(self.on_deleteAllDescriptorsBtn_clicked)

        self.ui.importTemplateBtn.clicked.connect(self.on_importTemplatesBtn_clicked)

        self.ui.chooseThumbBtn.clicked.connect(self.on_chooseThumbBtn_clicked)
        self.ui.chooseVideoBtn.clicked.connect(self.on_chooseVideoBtn_clicked)
        self.ui.clearSuggestedBtn.clicked.connect(self.on_clearSuggestedBtn_clicked)
        self.ui.caVideoChk.toggled.connect(self.on_caVideoChk_toggled)
        self.ui.reverseLoopChk.toggled.connect(self.on_reverseLoopChk_toggled)
        self.ui.useForegroundChk.toggled.connect(self.on_useForegroundChk_toggled)
        self.ui.clearSuggestedBtn.hide()
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

            # create the icon/label + delete button
            left_widget = QtWidgets.QWidget(widget)
            titleBtn = self.create_title_widget(tendie=template, widget=widget)
            delBtn = QtWidgets.QToolButton(widget)
            delBtn.setIcon(QtGui.QIcon(":/icon/trash.svg"))
            delBtn.clicked.connect(lambda _, file=template: (widgets[file].deleteLater(), tweaks["PosterBoard"].templates.remove(file)))
            # align to left layout
            left_layout = QtWidgets.QVBoxLayout(widget)
            left_layout.setContentsMargins(0, 0, 4, 0)
            left_layout.addWidget(titleBtn)
            left_layout.addWidget(delBtn)
            left_widget.setLayout(left_layout)

            # create options
            options_widget = QtWidgets.QWidget(widget)
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
                    repl_btn.setText(f"  {btn_lbl}")
                    repl_btn.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
                    repl_btn.clicked.connect(lambda _, opt=option: (self.on_importReplaceBtn_clicked(opt)))
                    repl_layout.addWidget(repl_btn)
                    repl_widget.setLayout(repl_layout)
                    opt_layout.addWidget(repl_widget)
                elif option.type == TemplateOptionTypePB.remove:
                    # remove object
                    remove_chk = QtWidgets.QCheckBox(options_widget)
                    remove_chk.setText(option.label)
                    remove_chk.setChecked(option.default_value)
                    remove_chk.toggled.connect(option.set_option)
            options_widget.setLayout(opt_layout)

            # main layout
            layout = QtWidgets.QHBoxLayout(widget)
            layout.setContentsMargins(4, 2, 4, 2)
            layout.addWidget(left_widget)
            line = QtWidgets.QFrame()
            line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
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
        tweaks["PosterBoard"].resetting = False
        self.ui.pbActionLbl.hide()
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
    def on_deleteAllDescriptorsBtn_clicked(self):
        if tweaks["PosterBoard"].resetting and tweaks["PosterBoard"].resetType == 0:
            tweaks["PosterBoard"].resetting = False
            self.ui.pbActionLbl.hide()
        else:
            tweaks["PosterBoard"].resetting = True
            tweaks["PosterBoard"].resetType = 0
            self.ui.pbActionLbl.setText("! Set to Clear Collections Wallpapers")
            self.ui.pbActionLbl.show()
    def on_resetPRBExtBtn_clicked(self):
        if tweaks["PosterBoard"].resetting and tweaks["PosterBoard"].resetType == 1:
            tweaks["PosterBoard"].resetting = False
            self.ui.pbActionLbl.hide()
        else:
            tweaks["PosterBoard"].resetting = True
            tweaks["PosterBoard"].resetType = 1
            self.ui.pbActionLbl.setText("! Set to Reset PRB Extension")
            self.ui.pbActionLbl.show()

    # Templates Page
    def on_importTemplatesBtn_clicked(self):
        selected_files, _ = QtWidgets.QFileDialog.getOpenFileNames(self.window, "Select PosterBoard Template Files", "", "Zip Files (*.batter)", options=QtWidgets.QFileDialog.ReadOnly)
        tweaks["PosterBoard"].resetting = False
        self.ui.pbActionLbl.hide()
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
        tweaks["PosterBoard"].resetting = False
        if selected_file != None and selected_file != "":
            tweaks["PosterBoard"].videoThumbnail = selected_file
            self.ui.pbVideoThumbLbl.setText(f"Current Thumbnail: {selected_file}")
        else:
            tweaks["PosterBoard"].videoThumbnail = None
            self.ui.pbVideoThumbLbl.setText("Current Thumbnail: None")
    def on_chooseVideoBtn_clicked(self):
        selected_file, _ = QtWidgets.QFileDialog.getOpenFileName(self.window, "Select Video File", "", "Video Files (*.mov *.mp4 *.mkv)", options=QtWidgets.QFileDialog.ReadOnly)
        tweaks["PosterBoard"].resetting = False
        if selected_file != None and selected_file != "":
            tweaks["PosterBoard"].videoFile = selected_file
            self.ui.pbVideoLbl.setText(f"Current Video: {selected_file}")
        else:
            tweaks["PosterBoard"].videoFile = None
            self.ui.pbVideoLbl.setText("Current Video: None")
    def on_clearSuggestedBtn_clicked(self):
        if tweaks["PosterBoard"].resetting and tweaks["PosterBoard"].resetType == 2:
            tweaks["PosterBoard"].resetting = False
            self.ui.pbActionLbl.hide()
        else:
            tweaks["PosterBoard"].resetting = True
            tweaks["PosterBoard"].resetType = 2
            self.ui.pbActionLbl.setText("! Set to Clear Suggested Photos")
            self.ui.pbActionLbl.show()
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