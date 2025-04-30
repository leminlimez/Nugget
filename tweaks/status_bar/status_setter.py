import os
if os.name == 'nt':
    # only needed for windows
    import tempfile
    import subprocess

from enum import Enum

from .status_bar_c.status_setter import ffi
from exceptions.nugget_exception import NuggetException

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
    
    def bool_array_to_str(self, arr: list[bool]) -> str:
        final_str = ""
        for a in arr:
            if a:
                final_str += "1"
            else:
                final_str += "0"
        return final_str
    def get_data(self) -> bytes:
        if os.name != 'nt':
            return ffi.buffer(self.current_overrides)
        # need to run the C++ cli tool because of differing bitfield standards
        tmpdir = tempfile.mkdtemp()
        tmp = os.path.join(tmpdir, "status_bar_overrides")
        #os.fsync(tmp) # sync so external program can see it
        overrides = self.current_overrides
        try:
            result = subprocess.run([
                "status_setter_windows.exe", tmp,
                "--overrideItemIsEnabled", self.bool_array_to_str(overrides.overrideItemIsEnabled),
                "--itemIsEnabled", self.bool_array_to_str(overrides.values.itemIsEnabled),
                "--timeString", ffi.string(overrides.values.timeString).decode(),
                "--shortTimeString", ffi.string(overrides.values.shortTimeString).decode(),
                "--dateString", ffi.string(overrides.values.dateString).decode(),
                "--serviceString", ffi.string(overrides.values.serviceString).decode(),
                "--secondaryServiceString", ffi.string(overrides.values.secondaryServiceString).decode(),
                "--serviceCrossfadeString", ffi.string(overrides.values.serviceCrossfadeString).decode(),
                "--secondaryServiceCrossfadeString", ffi.string(overrides.values.secondaryServiceCrossfadeString).decode(),
                "--batteryDetailString", ffi.string(overrides.values.batteryDetailString).decode(),
                "--primaryServiceBadgeString", ffi.string(overrides.values.primaryServiceBadgeString).decode(),
                "--secondaryServiceBadgeString", ffi.string(overrides.values.secondaryServiceBadgeString).decode(),
                "--breadcrumbTitle", ffi.string(overrides.values.breadcrumbTitle),
                "--overrideTimeString", str(overrides.overrideTimeString),
                "--overrideDateString", str(overrides.overrideDateString),
                "--overrideServiceString", str(overrides.overrideServiceString),
                "--overrideSecondaryServiceString", str(overrides.overrideSecondaryServiceString),
                "--overrideBatteryDetailString", str(overrides.overrideBatteryDetailString),
                "--overridePrimaryServiceBadgeString", str(overrides.overridePrimaryServiceBadgeString),
                "--overrideSecondaryServiceBadgeString", str(overrides.overrideSecondaryServiceBadgeString),
                "--overrideBreadcrumb", str(overrides.overrideBreadcrumb),
                "--overrideDisplayRawWifiSignal", str(overrides.overrideDisplayRawWifiSignal),
                "--overrideDisplayRawGSMSignal", str(overrides.overrideDisplayRawGSMSignal),
                "--displayRawWifiSignal", str(overrides.values.displayRawWifiSignal),
                "--displayRawGSMSignal", str(overrides.values.displayRawGSMSignal)
            ], encoding="utf-8", check=True)
        except subprocess.CalledProcessError as e:
            raise NuggetException(f"Failed to run status bar process:\n\n{e}")
        with open(tmp, "rb") as in_file:
            contents = in_file.read()
        try:
            # clean up temporary files
            os.remove(tmp)
            os.rmdir(tmpdir)
        except:
            pass
        return contents