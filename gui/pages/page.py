from tweaks.tweaks import tweaks, TweakID
from PySide6.QtWidgets import QRadioButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import QCoreApplication

class Page:
    def __init__(self):
        self.loaded = False

    def createRadioBtns(self, key: TweakID, container: QHBoxLayout, invert_values: bool = False):
        defaultBtn = QRadioButton(QCoreApplication.tr("Default"))
        defaultBtn.setChecked(True)
        defaultBtn.clicked.connect(lambda _, k=key: tweaks[k].set_enabled(False))
        enabledBtn = QRadioButton(QCoreApplication.tr("Enabled"))
        enabledBtn.clicked.connect(lambda _, k=key: tweaks[k].set_value(not invert_values))
        disabledBtn = QRadioButton(QCoreApplication.tr("Disabled"))
        disabledBtn.clicked.connect(lambda _, k=key: tweaks[k].set_value(invert_values))
        container.addWidget(defaultBtn)
        container.addWidget(enabledBtn)
        container.addWidget(disabledBtn)
        # spacer to left-align it
        spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        container.addItem(spacer)

    def load(self):
        if not self.loaded:
            self.load_page()
            self.loaded = True

    def load_page(self):
        raise NotImplementedError