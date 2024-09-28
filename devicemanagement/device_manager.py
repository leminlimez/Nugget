import traceback
import plistlib
from pathlib import Path

from PySide6.QtWidgets import QMessageBox

from pymobiledevice3 import usbmux
from pymobiledevice3.lockdown import create_using_usbmux

from devicemanagement.constants import Device, Version
from devicemanagement.data_singleton import DataSingleton

from tweaks.tweaks import tweaks, FeatureFlagTweak, EligibilityTweak, AITweak, BasicPlistTweak
from tweaks.basic_plist_locations import FileLocation
from Sparserestore.restore import restore_files, FileToRestore

def show_error_msg(txt: str):
    detailsBox = QMessageBox()
    detailsBox.setIcon(QMessageBox.Critical)
    detailsBox.setWindowTitle("Error!")
    detailsBox.setText(txt)
    detailsBox.setDetailedText(str(traceback.format_exc()))
    detailsBox.exec()

class DeviceManager:
    ## Class Functions
    def __init__(self):
        self.devices: list[Device] = []
        self.data_singleton = DataSingleton()
        self.current_device_index = 0
        self.apply_over_wifi = True
    
    def get_devices(self):
        self.devices.clear()
        connected_devices = usbmux.list_devices()
        # Connect via usbmuxd
        for device in connected_devices:
            if self.apply_over_wifi or device.is_usb:
                try:
                    ld = create_using_usbmux(serial=device.serial)
                    vals = ld.all_values
                    dev = Device(
                            uuid=device.serial,
                            name=vals['DeviceName'],
                            version=vals['ProductVersion'],
                            build=vals['BuildVersion'],
                            model=vals['ProductType'],
                            locale=ld.locale,
                            ld=ld
                        )
                    self.devices.append(dev)
                except Exception as e:
                    print(f"ERROR with lockdown device with UUID {device.serial}")
                    show_error_msg(type(e).__name__)
        
        if len(connected_devices) > 0:
            self.set_current_device(index=0)
        else:
            self.set_current_device(index=None)

    ## CURRENT DEVICE
    def set_current_device(self, index: int = None):
        if index == None:
            self.data_singleton.current_device = None
            self.data_singleton.device_available = False
            self.data_singleton.gestalt_path = None
            self.current_device_index = 0
        else:
            self.data_singleton.current_device = self.devices[index]
            if Version(self.devices[index].version) < Version("17.0"):
                self.data_singleton.device_available = False
                self.data_singleton.gestalt_path = None
            else:
                self.data_singleton.device_available = True
            self.current_device_index = index
        
    def get_current_device_name(self) -> str:
        if self.data_singleton.current_device == None:
            return "No Device"
        else:
            return self.data_singleton.current_device.name
        
    def get_current_device_version(self) -> str:
        if self.data_singleton.current_device == None:
            return ""
        else:
            return self.data_singleton.current_device.version
    
    def get_current_device_uuid(self) -> str:
        if self.data_singleton.current_device == None:
            return ""
        else:
            return self.data_singleton.current_device.uuid
        
    def get_current_device_supported(self) -> bool:
        if self.data_singleton.current_device == None:
            return False
        else:
            return self.data_singleton.current_device.supported()

    
    ## APPLYING OR REMOVING TWEAKS AND RESTORING
    def apply_changes(self, resetting: bool = False, update_label=lambda x: None):
        # set the tweaks and apply
        # first open the file in read mode
        update_label("Applying changes to files...")
        gestalt_plist = None
        if self.data_singleton.gestalt_path != None:
            with open(self.data_singleton.gestalt_path, 'rb') as in_fp:
                gestalt_plist = plistlib.load(in_fp)
        # create the other plists
        flag_plist: dict = {}
        eligibility_files = None
        ai_file = None
        basic_plists: dict = {}

        # set the plist keys
        if not resetting:
            for tweak_name in tweaks:
                tweak = tweaks[tweak_name]
                if isinstance(tweak, FeatureFlagTweak):
                    flag_plist = tweak.apply_tweak(flag_plist)
                elif isinstance(tweak, EligibilityTweak):
                    eligibility_files = tweak.apply_tweak()
                elif isinstance(tweak, AITweak):
                    ai_file = tweak.apply_tweak()
                elif isinstance(tweak, BasicPlistTweak):
                    basic_plists = tweak.apply_tweak(basic_plists)
                else:
                    if gestalt_plist != None:
                        gestalt_plist = tweak.apply_tweak(gestalt_plist)
        
        gestalt_data = None
        if resetting:
            gestalt_data = b""
        elif gestalt_plist != None:
            gestalt_data = plistlib.dumps(gestalt_plist)
        
        # Generate backup
        update_label("Generating backup...")
        # create the restore file list
        files_to_restore = [
            FileToRestore(
                contents=plistlib.dumps(flag_plist),
                restore_path="/var/preferences/FeatureFlags/",
                restore_name="Global.plist"
            )
        ]
        if gestalt_data != None:
            files_to_restore.append(FileToRestore(
                contents=gestalt_data,
                restore_path="/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/",
                restore_name="com.apple.MobileGestalt.plist"
            ))
        if eligibility_files:
            files_to_restore += eligibility_files
        if ai_file != None:
            files_to_restore.append(ai_file)
        for location, plist in basic_plists:
            files_to_restore.append(FileToRestore(
                contents=plistlib.dumps(plist),
                restore_path=location.value
            ))
        # reset basic tweaks
        if resetting:
            empty_data = plistlib.dumps({})
            for location in FileLocation:
                files_to_restore.append(FileToRestore(
                    contents=empty_data,
                    restore_path=location.value
                ))

        # restore to the device
        update_label("Restoring to device...")
        try:
            restore_files(files=files_to_restore, reboot=True, lockdown_client=self.data_singleton.current_device.ld)
            QMessageBox.information(None, "Success!", "All done! Your device will now restart.")
            update_label("Success!")
        except Exception as e:
            if "Find My" in str(e):
                detailsBox = QMessageBox()
                detailsBox.setIcon(QMessageBox.Critical)
                detailsBox.setWindowTitle("Error!")
                detailsBox.setText("Find My must be disabled in order to use this tool.")
                detailsBox.setDetailedText("Disable Find My from Settings (Settings -> [Your Name] -> Find My) and then try again.")
                detailsBox.exec()
            else:
                print(traceback.format_exc())
                update_label("Failed to restore")
                show_error_msg(type(e).__name__)

    ## RESETTING MOBILE GESTALT
    def reset_mobilegestalt(self, update_label=lambda x: None):
        # restore to the device
        update_label("Restoring to device...")
        try:
            restore_files(files=[FileToRestore(
                    contents=b"",
                    restore_path="/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/",
                    restore_name="com.apple.MobileGestalt.plist"
                )], reboot=True, lockdown_client=self.data_singleton.current_device.ld)
            QMessageBox.information(None, "Success!", "All done! Your device will now restart.")
            update_label("Success!")
        except Exception as e:
            if "Find My" in str(e):
                detailsBox = QMessageBox()
                detailsBox.setIcon(QMessageBox.Critical)
                detailsBox.setWindowTitle("Error!")
                detailsBox.setText("Find My must be disabled in order to use this tool.")
                detailsBox.setDetailedText("Disable Find My from Settings (Settings -> [Your Name] -> Find My) and then try again.")
                detailsBox.exec()
            else:
                print(traceback.format_exc())
                update_label("Failed to restore")
                show_error_msg(type(e).__name__)
