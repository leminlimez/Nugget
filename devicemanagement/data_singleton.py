from pathlib import Path

from devicemanagement.constants import Device, Tweak

class DataSingleton:
    def __init__(self):
        self.current_device: Device
        self.device_available: bool = False
        self.gestalt_path = None