from .nugget_exception import NuggetException
from PySide6.QtCore import QCoreApplication

class VideoLengthException(NuggetException):
    def __init__(self, frame_limit: int):
        super().__init__(QCoreApplication.tr("Videos must be under {0} frames to loop. Either reduce the frame rate or make it shorter.").format(frame_limit))

class PBTemplateException(Exception):
    def __init__(self, file: str, message: str):
        self.message = message
        super().__init__(self.message)
        self.filename = file
    def __str__(self):
        return self.message