from pathlib import Path

from devicemanagement.constants import Device, Tweak

class DataSingleton:
    def __init__(self):
        self.current_device: Device
        self.device_available: bool = False
        self.gestalt_path = None
        self.SAVED_GESTALT_STRING = "Nugget Saved MobileGestalt File" # string for when the data is saved by Nugget