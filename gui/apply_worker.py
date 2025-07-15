from PySide6.QtCore import Signal, QThread, QSettings
from PySide6.QtWidgets import QMessageBox
from typing import Optional

from gui.pages.pages_list import Page

class ApplyAlertMessage:
    def __init__(self, txt: str, title: str = "Error!", icon = QMessageBox.Critical, detailed_txt: str = None):
        self.txt = txt
        self.title = title
        self.icon = icon
        self.detailed_txt = detailed_txt

class ApplyThread(QThread):
    progress = Signal(str)
    alert = Signal(ApplyAlertMessage)

    def update_label(self, txt: str):
        self.progress.emit(txt)
    def alert_window(self, msg: ApplyAlertMessage):
        self.alert.emit(msg)
    
    def __init__(self, manager, settings: QSettings, reset_pages: Optional[list[Page]] = None):
        super().__init__()
        self.manager = manager
        self.settings = settings
        self.reset_pages = reset_pages

    def do_work(self):
        if self.reset_pages == None:
            # applying tweaks
            self.manager.apply_changes(self.update_label, self.alert_window)
        else:
            # resetting tweaks
            self.manager.reset_tweaks(self.reset_pages, self.settings, self.update_label, self.alert_window)

    def run(self):
        self.do_work()

class RefreshDevicesThread(QThread):
    alert = Signal(ApplyAlertMessage)

    def alert_window(self, msg: ApplyAlertMessage):
        self.alert.emit(msg)

    def __init__(self, manager, settings):
        super().__init__()
        self.manager = manager
        self.settings = settings

    def do_work(self):
        self.manager.get_devices(self.settings, self.alert_window)

    def run(self):
        self.do_work()