from PySide6 import QtCore, QtWidgets, QtGui

from ..page import Page
from qt.ui_mainwindow import Ui_Nugget

from tweaks.tweak_loader import load_mobilegestalt
from tweaks.tweaks import tweaks
from tweaks.custom_gestalt_tweaks import CustomGestaltTweaks, ValueTypeStrings

class GestaltPage(Page):
    def __init__(self, window, ui: Ui_Nugget):
        super().__init__()
        self.window = window
        self.ui = ui

    def load_page(self):
        self.ui.dynamicIslandDrp.activated.connect(self.on_dynamicIslandDrp_activated)
        self.ui.rdarFixChk.clicked.connect(self.on_rdarFixChk_clicked)
        self.ui.modelNameChk.toggled.connect(self.on_modelNameChk_clicked)
        self.ui.modelNameTxt.textEdited.connect(self.on_modelNameTxt_textEdited)

        self.ui.bootChimeChk.clicked.connect(self.on_bootChimeChk_clicked)
        self.ui.chargeLimitChk.clicked.connect(self.on_chargeLimitChk_clicked)
        self.ui.tapToWakeChk.clicked.connect(self.on_tapToWakeChk_clicked)
        self.ui.iphone16SettingsChk.clicked.connect(self.on_iphone16SettingsChk_clicked)
        self.ui.parallaxChk.clicked.connect(self.on_parallaxChk_clicked)
        self.ui.stageManagerChk.clicked.connect(self.on_stageManagerChk_clicked)
        self.ui.enableMedusaChk.clicked.connect(self.on_enableMedusaChk_clicked)
        self.ui.ipadAppsChk.clicked.connect(self.on_ipadAppsChk_clicked)
        self.ui.shutterChk.clicked.connect(self.on_shutterChk_clicked)
        self.ui.findMyFriendsChk.clicked.connect(self.on_findMyFriendsChk_clicked)
        self.ui.pencilChk.clicked.connect(self.on_pencilChk_clicked)
        self.ui.actionButtonChk.clicked.connect(self.on_actionButtonChk_clicked)

        self.ui.internalInstallChk.clicked.connect(self.on_internalInstallChk_clicked)
        self.ui.internalStorageChk.clicked.connect(self.on_internalStorageChk_clicked)
        self.ui.collisionSOSChk.clicked.connect(self.on_collisionSOSChk_clicked)
        self.ui.aodChk.clicked.connect(self.on_aodChk_clicked)
        self.ui.aodVibrancyChk.clicked.connect(self.on_aodVibrancyChk_clicked)

        self.ui.addGestaltKeyBtn.clicked.connect(self.on_addGestaltKeyBtn_clicked)

        # load tweaks
        load_mobilegestalt(self.window.device_manager.data_singleton.current_device)
        self.set_rdar_fix_label()
        self.ui.dynamicIslandDrp.setItemText(0, self.window.noneText)

    def setup_spoofedModelDrp_models(self):
        # hide all the models first
        for i in range(1, self.ui.spoofedModelDrp.count()):
            try:
                self.ui.spoofedModelDrp.removeItem(1)
            except:
                pass
        # indexes 1-6 for iPhones, 7-(len(values) - 1) for iPads
        # TODO: Make this get fetched from the gui on app startup
        spoof_drp_options = ["iPhone 15 Pro (iPhone16,1)", "iPhone 15 Pro Max (iPhone16,2)", "iPhone 16 (iPhone17,3)", "iPhone 16 Plus (iPhone17,4)", "iPhone 16 Pro (iPhone17,1)", "iPhone 16 Pro Max (iPhone17,2)", "iPad Mini (A17 Pro) (W) (iPad16,1)", "iPad Mini (A17 Pro) (C) (iPad16,2)", "iPad Pro (13-inch) (M4) (W) (iPad16,5)", "iPad Pro (13-inch) (M4) (C) (iPad16,6)", "iPad Pro (11-inch) (M4) (W) (iPad16,3)", "iPad Pro (11-inch) (M4) (C) (iPad16,4)", "iPad Pro (12.9-inch) (M2) (W) (iPad14,5)", "iPad Pro (12.9-inch) (M2) (C) (iPad14,6)", "iPad Pro (11-inch) (M2) (W) (iPad14,3)", "iPad Pro (11-inch) (M2) (C) (iPad14,4)", "iPad Air (13-inch) (M2) (W) (iPad14,10)", "iPad Air (13-inch) (M2) (C) (iPad14,11)", "iPad Air (11-inch) (M2) (W) (iPad14,8)", "iPad Air (11-inch) (M2) (C) (iPad14,9)", "iPad Pro (11-inch) (M1) (W) (iPad13,4)", "iPad Pro (11-inch) (M1) (C) (iPad13,5)", "iPad Pro (12.9-inch) (M1) (W) (iPad13,8)", "iPad Pro (12.9-inch) (M1) (C) (iPad13,9)", "iPad Air (M1) (W) (iPad13,16)", "iPad Air (M1) (C) (iPad13,17)"]
        if self.window.device_manager.show_all_spoofable_models or self.window.device_manager.get_current_device_model().startswith("iPhone"):
            # re-enable iPhone spoof models
            self.ui.spoofedModelDrp.addItems(spoof_drp_options[:6])
        if self.window.device_manager.show_all_spoofable_models or self.window.device_manager.get_current_device_model().startswith("iPad"):
            # re-enable iPad spoof models
            self.ui.spoofedModelDrp.addItems(spoof_drp_options[6:])

    ## ACTIONS
    def set_rdar_fix_label(self):
        rdar_title = tweaks["RdarFix"].get_rdar_title()
        if rdar_title == "hide":
            self.ui.rdarFixChk.hide()
        else:
            self.ui.rdarFixChk.show()
            res_title = QtCore.QCoreApplication.tr("modifies resolution")
            self.ui.rdarFixChk.setText(f"{rdar_title} ({res_title})")
    
    def on_dynamicIslandDrp_activated(self, index: int):
        if index == 0:
            tweaks["DynamicIsland"].set_enabled(False)
            tweaks["RdarFix"].set_di_type(-1)
        else:
            # disable X gestures on devices other than iPhone SEs
            # the lazy way, better option would be to remove it from the menu but I didn't want to rework all that
            model = self.window.device_manager.get_current_device_model()
            if index != 1 or (model == "iPhone12,8" or model == "iPhone14,6"):
                tweaks["DynamicIsland"].set_selected_option(index - 1)
            else:
                tweaks["DynamicIsland"].set_enabled(False)
            tweaks["RdarFix"].set_di_type(tweaks["DynamicIsland"].value[tweaks["DynamicIsland"].get_selected_option()])
        self.set_rdar_fix_label()
    def on_rdarFixChk_clicked(self, checked: bool):
        tweaks["RdarFix"].set_enabled(checked)

    def on_modelNameChk_clicked(self, checked: bool):
        tweaks["ModelName"].set_enabled(checked)
    def on_modelNameTxt_textEdited(self, text: str):
        tweaks["ModelName"].set_value(text, toggle_enabled=False)

    def on_bootChimeChk_clicked(self, checked: bool):
        tweaks["BootChime"].set_enabled(checked)
    def on_chargeLimitChk_clicked(self, checked: bool):
        tweaks["ChargeLimit"].set_enabled(checked)
    def on_tapToWakeChk_clicked(self, checked: bool):
        tweaks["TapToWake"].set_enabled(checked)
    def on_iphone16SettingsChk_clicked(self, checked: bool):
        tweaks["CameraButton"].set_enabled(checked)
    def on_parallaxChk_clicked(self, checked: bool):
        tweaks["Parallax"].set_enabled(checked)

    def on_stageManagerChk_clicked(self, checked: bool):
        tweaks["StageManager"].set_enabled(checked)
    def on_enableMedusaChk_clicked(self, checked: bool):
        tweaks["Medusa"].set_enabled(checked)
    def on_ipadAppsChk_clicked(self, checked: bool):
        tweaks["iPadApps"].set_enabled(checked)
    def on_shutterChk_clicked(self, checked: bool):
        # TODO: allow the user to select the region
        tweaks["Shutter"].set_enabled(checked)
    def on_findMyFriendsChk_clicked(self, checked: bool):
        tweaks["FindMyFriends"].set_enabled(checked)
    def on_pencilChk_clicked(self, checked: bool):
        tweaks["Pencil"].set_enabled(checked)
    def on_actionButtonChk_clicked(self, checked: bool):
        tweaks["ActionButton"].set_enabled(checked)

    def on_internalInstallChk_clicked(self, checked: bool):
        tweaks["InternalInstall"].set_enabled(checked)
    def on_internalStorageChk_clicked(self, checked: bool):
        tweaks["InternalStorage"].set_enabled(checked)

    def on_collisionSOSChk_clicked(self, checked: bool):
        tweaks["CollisionSOS"].set_enabled(checked)
    def on_aodChk_clicked(self, checked: bool):
        tweaks["AOD"].set_enabled(checked)
    def on_aodVibrancyChk_clicked(self, checked: bool):
        tweaks["AODVibrancy"].set_enabled(checked)

    def update_custom_gestalt_value_type(self, id, idx, valueField: QtWidgets.QLineEdit):
        new_str = CustomGestaltTweaks.set_tweak_value_type(id, idx)
        # update the value
        valueField.setText(new_str)

    def delete_custom_gestalt_key(self, id: int, widget: QtWidgets.QWidget):
        CustomGestaltTweaks.deactivate_tweak(id)
        self.ui.customKeysLayout.removeWidget(widget)
        widget.setParent(None)

    def on_addGestaltKeyBtn_clicked(self):
        # create a blank gestalt value with default value of 1
        key_identifier = CustomGestaltTweaks.create_tweak()

        widget = QtWidgets.QWidget()
        widget.setFixedHeight(35)
        widget.setStyleSheet("QWidget { background: none; border: 1px solid #3b3b3b; border-radius: 8px; }")
        hlayout = QtWidgets.QHBoxLayout(widget)
        hlayout.setContentsMargins(9, 2, 9, 2)

        # create the key field
        keyField = QtWidgets.QLineEdit(widget)
        # keyField.setMaximumWidth(200)
        keyField.setPlaceholderText("Key")
        keyField.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        keyField.setTextMargins(5, 0, 5, 0)
        keyField.textEdited.connect(lambda txt, id=key_identifier: CustomGestaltTweaks.set_tweak_key(id, txt))
        hlayout.addWidget(keyField)

        # create the delete button
        delBtn = QtWidgets.QToolButton(widget)
        delBtn.setIcon(QtGui.QIcon(":/icon/trash.svg"))
        delBtn.setStyleSheet("QToolButton { margin-right: 8px; background: none; border: none; }\nQToolButton:pressed { background: none; color: #FFFFFF; }")
        delBtn.clicked.connect(lambda _, id=key_identifier, w=widget: self.delete_custom_gestalt_key(id, w))
        hlayout.addWidget(delBtn)

        # create the type dropdown
        valueTypeDrp = QtWidgets.QComboBox(widget)
        valueTypeDrp.setStyleSheet("QComboBox {\n	background-color: #3b3b3b;\n    border: none;\n    color: #e8e8e8;\n    font-size: 14px;\n	padding-left: 8px;\n	border-radius: 8px;\n}\n\nQComboBox::drop-down {\n    image: url(:/icon/caret-down-fill.svg);\n	icon-size: 16px;\n    subcontrol-position: right center;\n	margin-right: 8px;\n}\n\nQComboBox QAbstractItemView {\n	background-color: #3b3b3b;\n    outline: none;\n	margin-top: 1px;\n}\n\nQComboBox QAbstractItemView::item {\n	background-color: #3b3b3b;\n	color: #e8e8e8;\n    padding-left: 8px;\n}\n\nQComboBox QAbstractItemView::item:hover {\n    background-color: #535353;\n    color: #ffffff;\n}")
        valueTypeDrp.setFixedWidth(120)
        valueTypeDrp.addItems(ValueTypeStrings)
        valueTypeDrp.setCurrentIndex(0)

        # create the value edit field
        valueField = QtWidgets.QLineEdit(widget)
        valueField.setMaximumWidth(175)
        valueField.setPlaceholderText("Value")
        valueField.setText("1")
        valueField.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        valueField.setTextMargins(5, 0, 5, 0)
        valueField.textEdited.connect(lambda txt, id=key_identifier: CustomGestaltTweaks.set_tweak_value(id, txt))

        valueTypeDrp.activated.connect(lambda idx, id=key_identifier, vf=valueField: self.update_custom_gestalt_value_type(id, idx, vf))
        hlayout.addWidget(valueTypeDrp)
        hlayout.addWidget(valueField)
        
        # add it to the main widget
        widget.setDisabled(False)
        self.ui.customKeysLayout.addWidget(widget)