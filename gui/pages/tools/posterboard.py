from PySide6 import QtCore, QtWidgets, QtGui
import webbrowser

from ..page import Page
from qt.ui_mainwindow import Ui_Nugget
from gui.dialogs import PBHelpDialog
from gui.custom_qt_elements.multicombobox import MultiComboBox
from gui.custom_qt_elements.resizable_image_label import ResizableImageLabel

from tweaks.tweaks import tweaks
from tweaks.posterboard.template_options import OptionType as TemplateOptionTypePB

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
                file.clean_files(),
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

            # main layout
            layout = QtWidgets.QVBoxLayout(widget)
            layout.setContentsMargins(4, 2, 4, 2)
            layout.addWidget(left_widget)
            line = QtWidgets.QFrame()
            line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
            line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
            line.setStyleSheet("QFrame {\n	color: #414141;\n}")
            layout.addWidget(line)

            # create previews
            prevs: dict[str, QtWidgets.QLabel] = {}
            if len(template.previews) > 0:
                prev_widget = QtWidgets.QWidget(widget)
                prev_widget.setMinimumHeight(0)
                prev_widget.setMaximumHeight(250)
                prev_widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                if template.preview_layout == "stacked":
                    prev_layout = QtWidgets.QStackedLayout(widget)
                    prev_layout.setStackingMode(QtWidgets.QStackedLayout.StackAll)
                else:
                    prev_layout = QtWidgets.QHBoxLayout(widget)
                prev_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
                for prev in template.previews.keys():
                    new_prev = ResizableImageLabel(prev_widget)
                    new_prev.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                    pixmap = QtGui.QPixmap(template.previews[prev])
                    new_prev.setPixmap(pixmap)
                    # new_prev.setScaledContents(True)
                    prev_layout.addWidget(new_prev)
                    prevs[prev] = new_prev
                prev_widget.setLayout(prev_layout)
                layout.addWidget(prev_widget)

            # create options
            # options_widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
            opt_layout = QtWidgets.QVBoxLayout()
            opt_layout.setContentsMargins(3, 0, 0, 0)

            # make banner
            if template.banner_text != None:
                banner = QtWidgets.QLabel(options_widget)
                banner.setText(template.banner_text)
                banner.setAlignment(QtCore.Qt.AlignCenter)
                if template.banner_stylesheet != None:
                    banner.setStyleSheet(template.banner_stylesheet)
                opt_layout.addWidget(banner)
            # make description
            if template.description != None:
                descr = QtWidgets.QLabel(options_widget)
                descr.setText(template.description)
                opt_layout.addWidget(descr)

            for option in template.options:
                # provide the window
                if option.type == TemplateOptionTypePB.replace and option.window == None:
                    option.window = self.window#.set_window(self.window)
                option.create_interface(options_widget=options_widget, options_layout=opt_layout)
                # add the previews and update it
                option.add_potential_preview_lbls(prevs)
                option.update_preview()

            options_widget.setLayout(opt_layout)

            # finish the main layout
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