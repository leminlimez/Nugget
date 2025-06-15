from .status_setter import Setter, StatusBarItem
from ..tweak_classes import Tweak
from restore.restore import FileToRestore

from cffi import FFI
ffi = FFI()

class StatusBarTweak(Tweak):
    def __init__(self):
        super().__init__(key=None)
        self.setter = Setter()

    def apply_tweak(self, files_to_restore: list[FileToRestore]):
        if self.enabled:
            files_to_restore.append(FileToRestore(
                contents=self.setter.get_data(),
                restore_path="/Library/SpringBoard/statusBarOverrides",
                domain="HomeDomain"
            ))

        
    ### PRIMARY CARRIER
    # CELLULAR SERVICE
    def is_cellular_service_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[StatusBarItem.CellularServiceStatusBarItem.value] == 1
    def get_cellular_service_override(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.values.itemIsEnabled[StatusBarItem.CellularServiceStatusBarItem.value] == 1
    def set_cellular_service(self, shown: bool) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[StatusBarItem.CellularServiceStatusBarItem.value] = 1
        overrides.values.itemIsEnabled[StatusBarItem.CellularServiceStatusBarItem.value] = 1 if shown else 0
        self.setter.apply_changes(overrides)
    def unset_cellular_service(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[StatusBarItem.CellularServiceStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
            
    # SERVICE STRING
    def is_carrier_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideServiceString == 1
    def get_carrier_override(self) -> str:
        overrides = self.setter.get_overrides()
        return ffi.string(overrides.values.serviceString).decode()
    def set_carrier_override(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideServiceString = 1
        truncated = text[:100]
        overrides.values.serviceString = truncated.encode()
        overrides.values.serviceCrossfadeString = truncated.encode()
        self.setter.apply_changes(overrides)
    def unset_carrier_override(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideServiceString = 0
        self.setter.apply_changes(overrides)

    # SERVICE BADGE
    def is_primary_service_badge_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overridePrimaryServiceBadgeString == 1
    def get_primary_service_badge_override(self) -> str:
        overrides = self.setter.get_overrides()
        return ffi.string(overrides.values.primaryServiceBadgeString).decode()
    def set_primary_service_badge(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overridePrimaryServiceBadgeString = 1
        overrides.values.primaryServiceBadgeString = text[:100].encode()
        self.setter.apply_changes(overrides)
    def unset_primary_service_badge(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overridePrimaryServiceBadgeString = 0
        self.setter.apply_changes(overrides)

    # DATA NETWORK TYPE
    def is_data_network_type_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideDataNetworkType == 1
    def get_data_network_type_override(self) -> int:
        overrides = self.setter.get_overrides()
        return overrides.values.dataNetworkType
    def set_data_network_type(self, id: int) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideDataNetworkType = 1
        overrides.values.dataNetworkType = id
        self.setter.apply_changes(overrides)
    def unset_data_network_type(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideDataNetworkType = 0
        self.setter.apply_changes(overrides)

    # GSM SIGNAL BARS
    def is_gsm_signal_strength_bars_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideGSMSignalStrengthBars == 1
    def get_gsm_signal_strength_bars_override(self) -> int:
        overrides = self.setter.get_overrides()
        return overrides.values.GSMSignalStrengthBars
    def set_gsm_signal_strength_bars(self, id: int) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[StatusBarItem.CellularSignalStrengthStatusBarItem.value] = 1
        overrides.values.itemIsEnabled[StatusBarItem.CellularSignalStrengthStatusBarItem.value] = 1
        overrides.overrideGSMSignalStrengthBars = 1
        overrides.values.GSMSignalStrengthBars = id
        self.setter.apply_changes(overrides)
    def unset_gsm_signal_strength_bars(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[StatusBarItem.CellularSignalStrengthStatusBarItem.value] = 0
        overrides.overrideGSMSignalStrengthBars = 0
        self.setter.apply_changes(overrides)


    ### SECONDARY CARRIER
    # CELLULAR SERVICE
    def is_secondary_cellular_service_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[StatusBarItem.SecondaryCellularServiceStatusBarItem.value] == 1
    def get_secondary_cellular_service_override(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.values.itemIsEnabled[StatusBarItem.SecondaryCellularServiceStatusBarItem.value] == 1
    def set_secondary_cellular_service(self, shown: bool) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[StatusBarItem.SecondaryCellularServiceStatusBarItem.value] = 1
        overrides.values.itemIsEnabled[StatusBarItem.SecondaryCellularServiceStatusBarItem.value] = 1 if shown else 0
        overrides.overrideSecondaryCellularConfigured = 1
        overrides.values.secondaryCellularConfigured = 1 if shown else 0
        self.setter.apply_changes(overrides)
    def unset_secondary_cellular_service(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[StatusBarItem.SecondaryCellularServiceStatusBarItem.value] = 0
        overrides.overrideSecondaryCellularConfigured = 0
        self.setter.apply_changes(overrides)
            
    # SERVICE STRING
    def is_secondary_carrier_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideSecondaryServiceString == 1
    def get_secondary_carrier_override(self) -> str:
        overrides = self.setter.get_overrides()
        return ffi.string(overrides.values.secondaryServiceString).decode()
    def set_secondary_carrier_override(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideSecondaryServiceString = 1
        truncated = text[:100]
        overrides.values.secondaryServiceString = truncated.encode()
        overrides.values.secondaryServiceCrossfadeString = truncated.encode()
        self.setter.apply_changes(overrides)
    def unset_secondary_carrier_override(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideSecondaryServiceString = 0
        self.setter.apply_changes(overrides)

    # SERVICE BADGE
    def is_secondary_service_badge_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideSecondaryServiceBadgeString == 1
    def get_secondary_service_badge_override(self) -> str:
        overrides = self.setter.get_overrides()
        return ffi.string(overrides.values.secondaryServiceBadgeString).decode()
    def set_secondary_service_badge(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideSecondaryServiceBadgeString = 1
        overrides.values.secondaryServiceBadgeString = text[:100].encode()
        self.setter.apply_changes(overrides)
    def unset_secondary_service_badge(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideSecondaryServiceBadgeString = 0
        self.setter.apply_changes(overrides)

    # DATA NETWORK TYPE
    def is_secondary_data_network_type_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideSecondaryDataNetworkType == 1
    def get_secondary_data_network_type_override(self) -> int:
        overrides = self.setter.get_overrides()
        return overrides.values.secondaryDataNetworkType
    def set_secondary_data_network_type(self, id: int) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideSecondaryDataNetworkType = 1
        overrides.values.secondaryDataNetworkType = id
        self.setter.apply_changes(overrides)
    def unset_secondary_data_network_type(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideSecondaryDataNetworkType = 0
        self.setter.apply_changes(overrides)

    # GSM SIGNAL BARS
    def is_secondary_gsm_signal_strength_bars_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideSecondaryGSMSignalStrengthBars == 1
    def get_secondary_gsm_signal_strength_bars_override(self) -> int:
        overrides = self.setter.get_overrides()
        return overrides.values.secondaryGSMSignalStrengthBars
    def set_secondary_gsm_signal_strength_bars(self, id: int) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[StatusBarItem.SecondaryCellularSignalStrengthStatusBarItem.value] = 1
        overrides.values.itemIsEnabled[StatusBarItem.SecondaryCellularSignalStrengthStatusBarItem.value] = 1
        overrides.overrideSecondaryGSMSignalStrengthBars = 1
        overrides.values.secondaryGSMSignalStrengthBars = id
        self.setter.apply_changes(overrides)
    def unset_secondary_gsm_signal_strength_bars(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[StatusBarItem.SecondaryCellularSignalStrengthStatusBarItem.value] = 0
        overrides.overrideSecondaryGSMSignalStrengthBars = 0
        self.setter.apply_changes(overrides)


    ### MISC TEXT INPUTS
    # DATE STRING (Unused)
    def is_date_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideDateString == 1
    def get_date_override(self) -> str:
        overrides = self.setter.get_overrides()
        return ffi.string(overrides.values.dateString).decode()
    def set_date(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideDateString = 1
        overrides.values.dateString = text[:256].encode()
        self.setter.apply_changes(overrides)
    def unset_date(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideDateString = 0
        self.setter.apply_changes(overrides)

    # TIME STRING
    def is_time_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideTimeString == 1
    def get_time_override(self) -> str:
        overrides = self.setter.get_overrides()
        return ffi.string(overrides.values.timeString).decode()
    def set_time(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideTimeString = 1
        overrides.values.timeString = text[:64].encode()
        self.setter.apply_changes(overrides)
    def unset_time(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideTimeString = 0
        self.setter.apply_changes(overrides)

    # BREADCRUMB STRING
    def is_crumb_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideBreadcrumb == 1
    def get_crumb_override(self) -> str:
        overrides = self.setter.get_overrides()
        text: str = ffi.string(overrides.values.breadcrumbTitle).decode()
        if len(text) > 1:
            return text[:len(text) - 4]
        return ""
    def set_crumb(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideBreadcrumb = 1
        new_crumb = ""
        if text != "":
            new_crumb: str = text[:254] + " ▶"
        overrides.values.breadcrumbTitle = new_crumb.encode()
        self.setter.apply_changes(overrides)
    def unset_crumb(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideBreadcrumb = 0
        overrides.values.breadcrumbTitle = "".encode()
        self.setter.apply_changes(overrides)

    # BATTERY DETAIL STRING
    def is_battery_detail_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideBatteryDetailString == 1
    def get_battery_detail_override(self) -> str:
        overrides = self.setter.get_overrides()
        return ffi.string(overrides.values.batteryDetailString).decode()
    def set_battery_detail(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideBatteryDetailString = 1
        overrides.values.batteryDetailString = text[:150].encode()
        self.setter.apply_changes(overrides)
    def unset_battery_detail(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideBatteryDetailString = 0
        self.setter.apply_changes(overrides)


    ## MISC SLIDER INPUTS
    # BATTERY CAPACITY
    def is_battery_capacity_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideBatteryCapacity == 1
    def get_battery_capacity_override(self) -> int:
        overrides = self.setter.get_overrides()
        return overrides.values.batteryCapacity
    def set_battery_capacity(self, id: int) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideBatteryCapacity = 1
        overrides.values.batteryCapacity = id
        self.setter.apply_changes(overrides)
    def unset_battery_capacity(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideBatteryCapacity = 0
        self.setter.apply_changes(overrides)

    # WIFI SIGNAL STRENGTH
    def is_wifi_signal_strength_bars_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideWifiSignalStrengthBars == 1
    def get_wifi_signal_strength_bars_override(self) -> int:
        overrides = self.setter.get_overrides()
        return overrides.values.wifiSignalStrengthBars
    def set_wifi_signal_strength_bars(self, id: int) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideWifiSignalStrengthBars = 1
        overrides.values.wifiSignalStrengthBars = id
        self.setter.apply_changes(overrides)
    def unset_wifi_signal_strength_bars(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideWifiSignalStrengthBars = 0
        self.setter.apply_changes(overrides)


    ## RAW SIGNAL STRENGTH TOGGLES
    # WIFI
    def is_raw_wifi_signal_shown(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideDisplayRawWifiSignal == 1
    def show_raw_wifi_signal(self, shown: bool) -> None:
        overrides = self.setter.get_overrides()
        if shown:
            overrides.overrideDisplayRawWifiSignal = 1
            overrides.values.displayRawWifiSignal = 1
        else:
            overrides.overrideDisplayRawWifiSignal = 0
        self.setter.apply_changes(overrides)
    # GSM
    def is_raw_gsm_signal_shown(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideDisplayRawGSMSignal == 1
    def show_raw_gsm_signal(self, shown: bool) -> None:
        overrides = self.setter.get_overrides()
        if shown:
            overrides.overrideDisplayRawGSMSignal = 1
            overrides.values.displayRawGSMSignal = 1
        else:
            overrides.overrideDisplayRawGSMSignal = 0
        self.setter.apply_changes(overrides)

    ## RADIO BUTTONS
    def is_item_overridden(self, item: StatusBarItem) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[item.value] == 1
    def get_item_override(self, item: StatusBarItem) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.values.itemIsEnabled[item.value] == 1
    def set_item_override(self, item: StatusBarItem, shown: bool) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[item.value] = 1
        overrides.values.itemIsEnabled[item.value] = 1 if shown else 0
        self.setter.apply_changes(overrides)
    def unset_item_override(self, item: StatusBarItem) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[item.value] = 0
        self.setter.apply_changes(overrides)


    ## HIDE OPTION TOGGLES
    # DND
    def is_dnd_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[StatusBarItem.QuietModeStatusBarItem.value] == 1
    def hide_dnd(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[StatusBarItem.QuietModeStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[StatusBarItem.QuietModeStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[StatusBarItem.QuietModeStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # AIRPLANE
    def is_airplane_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[StatusBarItem.AirplaneModeStatusBarItem.value] == 1
    def hide_airplane(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[StatusBarItem.AirplaneModeStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[StatusBarItem.AirplaneModeStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[StatusBarItem.AirplaneModeStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # CELL
    def is_cell_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[StatusBarItem.CellularServiceStatusBarItem.value] == 1
    def hide_cell(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[StatusBarItem.CellularServiceStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[StatusBarItem.CellularServiceStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[StatusBarItem.CellularServiceStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # WIFI
    def is_wifi_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[StatusBarItem.CellularDataNetworkStatusBarItem.value] == 1
    def hide_wifi(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[StatusBarItem.CellularDataNetworkStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[StatusBarItem.CellularDataNetworkStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[StatusBarItem.CellularDataNetworkStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # BATTERY
    def is_battery_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[StatusBarItem.MainBatteryStatusBarItem.value] == 1
    def hide_battery(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[StatusBarItem.MainBatteryStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[StatusBarItem.MainBatteryStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[StatusBarItem.MainBatteryStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # BLUETOOTH
    def is_bluetooth_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[StatusBarItem.BluetoothStatusBarItem.value] == 1
    def hide_bluetooth(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[StatusBarItem.BluetoothStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[StatusBarItem.BluetoothStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[StatusBarItem.BluetoothStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # ALARM
    def is_alarm_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[StatusBarItem.AlarmStatusBarItem.value] == 1
    def hide_alarm(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[StatusBarItem.AlarmStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[StatusBarItem.AlarmStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[StatusBarItem.AlarmStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # LOCATION
    def is_location_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[StatusBarItem.LocationStatusBarItem.value] == 1
    def hide_location(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[StatusBarItem.LocationStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[StatusBarItem.LocationStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[StatusBarItem.LocationStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # ROTATION LOCK
    def is_rotation_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[StatusBarItem.RotationLockStatusBarItem.value] == 1
    def hide_rotation(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[StatusBarItem.RotationLockStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[StatusBarItem.RotationLockStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[StatusBarItem.RotationLockStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # AIRPLAY
    def is_airplay_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[StatusBarItem.AirPlayStatusBarItem.value] == 1
    def hide_airplay(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[StatusBarItem.AirPlayStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[StatusBarItem.AirPlayStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[StatusBarItem.AirPlayStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # CARPLAY
    def is_carplay_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[StatusBarItem.CarPlayStatusBarItem.value] == 1
    def hide_carplay(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[StatusBarItem.CarPlayStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[StatusBarItem.CarPlayStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[StatusBarItem.CarPlayStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # VPN
    def is_vpn_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[StatusBarItem.VPNStatusBarItem.value] == 1
    def hide_vpn(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[StatusBarItem.VPNStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[StatusBarItem.VPNStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[StatusBarItem.VPNStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)

    def is_silly_mode_enabled(self) -> bool:
        return self.setter.silly_mode
    def toggle_silly_mode(self, value: bool) -> None:
        self.setter.silly_mode = value
