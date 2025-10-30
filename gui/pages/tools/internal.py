from ..page import Page
from qt.ui_mainwindow import Ui_Nugget

from PySide6.QtWidgets import QRadioButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import QCoreApplication

from tweaks.tweak_loader import load_internal
from tweaks.tweaks import tweaks

class InternalPage(Page):
    def __init__(self, ui: Ui_Nugget):
        super().__init__()
        self.ui = ui

    def createRadioBtns(self, key: str, container: QHBoxLayout):
        defaultBtn = QRadioButton(QCoreApplication.tr("Default"))
        defaultBtn.setChecked(True)
        defaultBtn.clicked.connect(lambda _, k=key: tweaks[k].set_enabled(False))
        enabledBtn = QRadioButton(QCoreApplication.tr("Enabled"))
        enabledBtn.clicked.connect(lambda _, k=key: tweaks[k].set_value(True))
        disabledBtn = QRadioButton(QCoreApplication.tr("Disabled"))
        disabledBtn.clicked.connect(lambda _, k=key: tweaks[k].set_value(False))
        container.addWidget(defaultBtn)
        container.addWidget(enabledBtn)
        container.addWidget(disabledBtn)
        # spacer to left-align it
        spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        container.addItem(spacer)

    def load_page(self):
        # Create the radio buttons where needed
        self.createRadioBtns(key="DisableSolarium", container=self.ui.disableSolariumBtns)
        self.createRadioBtns(key="IgnoreSolariumLinkedOnCheck", container=self.ui.ignoreSolariumAppBuildBtns)

        self.createRadioBtns(key="SBBuildNumber", container=self.ui.buildVersionBtns)
        self.createRadioBtns(key="RTL", container=self.ui.RTLBtns)
        self.createRadioBtns(key="LTR", container=self.ui.LTRBtns)
        self.createRadioBtns(key="SBIconVisibility", container=self.ui.sbIconVisibilityBtns)
        self.createRadioBtns(key="KeyFlick", container=self.ui.keyFlickBtns)

        self.createRadioBtns(key="MetalForceHudEnabled", container=self.ui.metalHUDBtns)
        self.createRadioBtns(key="iMessageDiagnosticsEnabled", container=self.ui.iMessageBtns)
        self.createRadioBtns(key="IDSDiagnosticsEnabled", container=self.ui.IDSBtns)
        self.createRadioBtns(key="VCDiagnosticsEnabled", container=self.ui.VCBtns)
        self.createRadioBtns(key="AccessoryDeveloperEnabled", container=self.ui.accessoryDevBtns)

        self.createRadioBtns(key="AppStoreDebug", container=self.ui.appStoreBtns)
        self.createRadioBtns(key="NotesDebugMode", container=self.ui.notesBtns)

        self.createRadioBtns(key="BKDigitizerVisualizeTouches", container=self.ui.showTouchesBtns)
        self.createRadioBtns(key="BKHideAppleLogoOnLaunch", container=self.ui.hideRespringBtns)
        self.createRadioBtns(key="EnableWakeGestureHaptic", container=self.ui.wakeVibrateBtns)
        self.createRadioBtns(key="PlaySoundOnPaste", container=self.ui.pasteSoundBtns)
        self.createRadioBtns(key="AnnounceAllPastes", container=self.ui.notifyPastesBtns)

        load_internal()
