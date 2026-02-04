import os
import sys
if os.name == 'nt':
    # only needed for windows
    import tempfile
    import subprocess

from enum import Enum

from .status_bar_c.status_setter import ffi
from src.exceptions.nugget_exception import NuggetException

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
    PhonePickupStatusBarItem = 31
    # 32
    # 33
    # 34
    # 35
    # 36
    # 37
    # 38
    # 39
    LiquidDetectionStatusBarItem = 40
    VoiceControlStatusBarItem = 41
    # 42
    # 43
    Extra1StatusBarItem = 44
    # 45

class Setter:
    def __init__(self):
        self.current_overrides = ffi.new("StatusBarOverrideData *")
        self.silly_mode = False

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
        overrides = self.current_overrides
        if self.silly_mode:
            # create a copy so that it doesn't change the original data
            overrides = ffi.new("StatusBarOverrideData *")
            # since it doesn't contain pointers, can just copy directly
            ffi.memmove(overrides, self.current_overrides, ffi.sizeof(self.current_overrides))
            # now turn on everything funny
            for i in range(46):
                if overrides.overrideItemIsEnabled[i] == 1:
                    # don't change setting
                    continue
                overrides.overrideItemIsEnabled[i] = 1
                overrides.values.itemIsEnabled[i] = 1
        if os.name != 'nt':
            return ffi.buffer(self.current_overrides)
        
        # --- PATH DETECTION START ---
        if getattr(sys, 'frozen', False):
            if hasattr(sys, '_MEIPASS'):
                base_path = sys._MEIPASS
            else:
                base_path = os.path.dirname(sys.executable)
                if not os.path.exists(os.path.join(base_path, "status_setter_windows.exe")):
                    if os.path.exists(os.path.join(base_path, "_internal", "status_setter_windows.exe")):
                        base_path = os.path.join(base_path, "_internal")
        else:
            base_path = os.getcwd()

        exe_path = os.path.join(base_path, "status_setter_windows.exe")
        # --- PATH DETECTION END ---

        # need to run the C++ cli tool because of differing bitfield standards
        tmpdir = tempfile.mkdtemp()
        tmpin = os.path.join(tmpdir, "sbin")
        tmpout = os.path.join(tmpdir, "status_bar_overrides")
        
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
            
            # --- FIX: Inject PATH env variable ---
            env = os.environ.copy()
            # Prepend our base_path to the PATH so the exe finds its DLLs first
            env["PATH"] = base_path + os.pathsep + env["PATH"]

            result = subprocess.run(
                [exe_path, tmpin, tmpout],
                encoding="utf-8", 
                check=True, 
                cwd=base_path,
                env=env  # <--- Critical for finding DLLs
            )
            print(f"returned {result}")
            
        except subprocess.CalledProcessError as e:
            # Enhanced Error Logging
            file_list = "Unable to list files"
            try:
                file_list = os.listdir(base_path)
            except:
                pass
            raise NuggetException(f"Failed to run status bar process.\nPath used: {base_path}\nFiles in path: {file_list}\nError: {e}")
            
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