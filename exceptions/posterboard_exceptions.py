from .nugget_exception import NuggetException

class VideoLengthException(NuggetException):
    def __init__(self, frame_limit: int):
        super().__init__(f"Videos must be under {frame_limit} frames to loop. Either reduce the frame rate or make it shorter.")

class PBTemplateException(Exception):
    def __init__(self, file: str, message: str):
        self.message = message
        super().__init__(self.message)
        self.filename = file
    def __str__(self):
        return self.message