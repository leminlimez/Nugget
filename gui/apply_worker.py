from PySide6.QtCore import Signal, QThread
from PySide6.QtWidgets import QMessageBox

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
    
    def __init__(self, manager, resetting: bool = False):
        super().__init__()
        self.manager = manager
        self.resetting = resetting

    def do_work(self):
        self.manager.apply_changes(self.resetting, self.update_label, self.alert_window)

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