from enum import Enum
from .status_bar_c.status_setter import ffi

class Setter:
    class StatusBarItem(Enum):
        TimeStatusBarItem = 0
        DateStatusBarItem = 1
        QuietModeStatusBarItem = 2
        AirplaneModeStatusBarItem = 3
        CellularSignalStrengthStatusBarItem = 4
        SecondaryCellularSignalStrengthStatusBarItem = 5
        CellularServiceStatusBarItem = 6
        SecondaryCellularServiceStatusBarItem = 7
        # 8
        CellularDataNetworkStatusBarItem = 9
        SecondaryCellularDataNetworkStatusBarItem = 10
        # 11
        MainBatteryStatusBarItem = 12
        ProminentlyShowBatteryDetailStatusBarItem = 13
        # 14
        # 15
        BluetoothStatusBarItem = 16
        TTYStatusBarItem = 17
        AlarmStatusBarItem = 18
        # 19
        # 20
        LocationStatusBarItem = 21
        RotationLockStatusBarItem = 22
        CameraUseStatusBarItem = 23
        AirPlayStatusBarItem = 24
        AssistantStatusBarItem = 25
        CarPlayStatusBarItem = 26
        StudentStatusBarItem = 27
        MicrophoneUseStatusBarItem = 28
        VPNStatusBarItem = 29
        # 30
        # 31
        # 32
        # 33
        # 34
        # 35
        # 36
        # 37
        LiquidDetectionStatusBarItem = 38
        VoiceControlStatusBarItem = 39
        # 40
        # 41
        # 42
        # 43
        Extra1StatusBarItem = 44
    
    def __init__(self):
        self.current_overrides = ffi.new("StatusBarOverrideData *")

    def apply_changes(self, new_overrides):
        self.current_overrides = new_overrides
    def get_overrides(self):
        return self.current_overrides
    def get_data(self) -> bytes:
        return ffi.buffer(self.current_overrides)