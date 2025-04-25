from PySide6 import QtCore, QtWidgets, QtGui
import webbrowser
import subprocess
import os
import uuid

from ..page import Page
from qt.ui_mainwindow import Ui_Nugget

from tweaks.tweaks import tweaks

class TemplatesPage(Page):
    def __init__(self, window, ui: Ui_Nugget):
        super().__init__()
        self.window = window
        self.ui = ui
        self.templateLayout = None

    def load_page(self):
        self.ui.importTemplatesBtn.clicked.connect(self.on_importTemplatesBtn_clicked)

    def on_importTemplatesBtn_clicked(self):
        selected_files, _ = QtWidgets.QFileDialog.getOpenFileNames(self.window, "Select Nugget Template Files", "", "Zip Files (*.batter)", options=QtWidgets.QFileDialog.ReadOnly)
        if selected_files != None and len(selected_files) > 0:
            # user selected files, add them
            for file in selected_files:
                tweaks["Templates"].add_template(file)
            self.load_templates_list()

    def load_templates_list(self):
        if len(tweaks["Templates"].templates) == 0:
            return
        if self.templateLayout == None:
            # Create scroll layout
            self.templateLayout = QtWidgets.QVBoxLayout()
            self.templateLayout.setContentsMargins(0, 0, 0, 0)
            self.templateLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
            # Create a QWidget to act as the container for the scroll area
            scrollWidget = QtWidgets.QWidget()

            # Set the main layout (containing all the widgets) on the scroll widget
            scrollWidget.setLayout(self.templateLayout)

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
            self.ui.templatesList.setLayout(scrollLayout)
        
        widgets = {}
        # Iterate through the templates
        for template in tweaks["Templates"].templates:
            template.create_ui(self.window, tweaks["Templates"], widgets, self.templateLayout)