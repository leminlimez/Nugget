from PySide6.QtCore import Signal, QThread
from .apply_worker import ApplyAlertMessage

class PBDBThread(QThread):
    progress = Signal(float)
    infoLbl = Signal(str)
    # TODO: Error messages
    # alert = Signal(ApplyAlertMessage)

    def update_label(self, txt: str):
        self.infoLbl.emit(txt)
    def update_progress(self, amt: float):
        self.progress.emit(amt)
    # def alert_window(self, msg: ApplyAlertMessage):
    #     self.alert.emit(msg)
    
    def __init__(self, backup_function):
        super().__init__()
        self.backup_function = backup_function

    def do_work(self):
        self.backup_function(self.update_label, self.update_progress)

    def run(self):
        self.do_work()