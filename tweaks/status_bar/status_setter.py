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
            if a == 1:
                final_str += "1"
            else:
                final_str += "0"
        return final_str
    def get_data(self) -> bytes:
        if os.name != 'nt':
            return ffi.buffer(self.current_overrides)
        # need to run the C++ cli tool because of differing bitfield standards
        tmpdir = tempfile.mkdtemp()
        tmpin = os.path.join(tmpdir, "sbin")
        tmpout = os.path.join(tmpdir, "status_bar_overrides")
        #os.fsync(tmpin) # sync so external program can see it
        overrides = self.current_overrides
        try:
            # generate the input file
            with open(tmpin, "w", encoding="utf-8") as in_file:
                for item in ([
                    self.bool_array_to_str(overrides.overrideItemIsEnabled),
                    self.bool_array_to_str(overrides.values.itemIsEnabled),
                    ffi.string(overrides.values.timeString).decode(),
                    ffi.string(overrides.values.shortTimeString).decode(),
                    ffi.string(overrides.values.dateString).decode(),
                    ffi.string(overrides.values.serviceString).decode(),
                    ffi.string(overrides.values.secondaryServiceString).decode(),
                    ffi.string(overrides.values.serviceCrossfadeString).decode(),
                    ffi.string(overrides.values.secondaryServiceCrossfadeString).decode(),
                    ffi.string(overrides.values.batteryDetailString).decode(),
                    ffi.string(overrides.values.primaryServiceBadgeString).decode(),
                    ffi.string(overrides.values.secondaryServiceBadgeString).decode(),
                    ffi.string(overrides.values.breadcrumbTitle).decode(),
                    int(overrides.overrideTimeString),
                    int(overrides.overrideDateString),
                    int(overrides.overrideServiceString),
                    int(overrides.overrideSecondaryServiceString),
                    int(overrides.overrideBatteryDetailString),
                    int(overrides.overridePrimaryServiceBadgeString),
                    int(overrides.overrideSecondaryServiceBadgeString),
                    int(overrides.overrideBreadcrumb),
                    int(overrides.overrideDisplayRawWifiSignal),
                    int(overrides.overrideDisplayRawGSMSignal),
                    int(overrides.values.displayRawWifiSignal),
                    int(overrides.values.displayRawGSMSignal),
                    int(overrides.overrideDataNetworkType),
                    int(overrides.values.dataNetworkType),
                    int(overrides.overrideSecondaryDataNetworkType),
                    int(overrides.values.secondaryDataNetworkType),
                    int(overrides.overrideGSMSignalStrengthBars),
                    int(overrides.values.GSMSignalStrengthBars),
                    int(overrides.overrideSecondaryGSMSignalStrengthBars),
                    int(overrides.values.secondaryGSMSignalStrengthBars),
                    int(overrides.overrideBatteryCapacity),
                    int(overrides.values.batteryCapacity),
                    int(overrides.overrideWifiSignalStrengthBars),
                    int(overrides.values.wifiSignalStrengthBars)
                ]):
                    in_file.write(f"{item}\n")
            result = subprocess.run([
                "status_setter_windows.exe", tmpin, tmpout
            ], encoding="utf-8", check=True)
            print(f"returned {result}")
        except subprocess.CalledProcessError as e:
            raise NuggetException(f"Failed to run status bar process:\n\n{e}")
        with open(tmpin, "r", encoding='utf-8') as fi:
            conts = fi.read()
        with open("C:\\Users\\lemin\\Documents\\sb_out.txt", "w", encoding='utf-8') as fo:
            fo.write(conts)
        with open(tmpout, "rb") as in_file:
            contents = in_file.read()
        try:
            # clean up temporary files
            os.remove(tmpin)
            os.remove(tmpout)
            os.rmdir(tmpdir)
        except:
            pass
        return contents