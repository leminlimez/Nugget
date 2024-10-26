import traceback
import plistlib
from pathlib import Path

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QSettings

from pymobiledevice3 import usbmux
from pymobiledevice3.lockdown import create_using_usbmux

from devicemanagement.constants import Device, Version
from devicemanagement.data_singleton import DataSingleton

from tweaks.tweaks import tweaks, FeatureFlagTweak, EligibilityTweak, AITweak, BasicPlistTweak, RdarFixTweak
from tweaks.custom_gestalt_tweaks import CustomGestaltTweaks
from tweaks.basic_plist_locations import FileLocationsList
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

        # preferences
        self.apply_over_wifi = True
        self.skip_setup = True
        self.auto_reboot = True
    
    def get_devices(self, settings: QSettings):
        self.devices.clear()
        # handle errors when failing to get connected devices
        try:
            connected_devices = usbmux.list_devices()
        except:
            show_error_msg(
                """
                Failed to get device list. Click \"Show Details\" for the traceback.

                If you are on Windows, make sure you have the \"Apple Devices\" app from the Microsoft Store or iTunes from Apple's website.
                If you are on Linux, make sure you have usbmuxd and libimobiledevice installed.
                """
            )
        # Connect via usbmuxd
        for device in connected_devices:
            if self.apply_over_wifi or device.is_usb:
                try:
                    ld = create_using_usbmux(serial=device.serial)
                    vals = ld.all_values
                    model = vals['ProductType']
                    try:
                        product_type = settings.value(device.serial + "_model", "", type=str)
                        if product_type == "":
                            # save the new product type
                            settings.setValue(device.serial + "_model", model)
                        else:
                            model = product_type
                    except:
                        pass
                    dev = Device(
                            uuid=device.serial,
                            name=vals['DeviceName'],
                            version=vals['ProductVersion'],
                            build=vals['BuildVersion'],
                            model=model,
                            locale=ld.locale,
                            ld=ld
                        )
                    tweaks["RdarFix"].get_rdar_mode(model)
                    self.devices.append(dev)
                except Exception as e:
                    print(f"ERROR with lockdown device with UUID {device.serial}")
                    show_error_msg(type(e).__name__ + ": " + repr(e))
        
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
            tweaks["SpoofModel"].value[0] = "Placeholder"
        else:
            self.data_singleton.current_device = self.devices[index]
            if Version(self.devices[index].version) < Version("17.0"):
                self.data_singleton.device_available = False
                self.data_singleton.gestalt_path = None
            else:
                self.data_singleton.device_available = True
                tweaks["SpoofModel"].value[0] = self.data_singleton.current_device.model
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
    
    def get_current_device_build(self) -> str:
        if self.data_singleton.current_device == None:
            return ""
        else:
            return self.data_singleton.current_device.build
    
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
        

    def reset_device_pairing(self):
        # first, unpair it
        if self.data_singleton.current_device == None:
            return
        self.data_singleton.current_device.ld.unpair()
        # next, pair it again
        self.data_singleton.current_device.ld.pair()
        QMessageBox.information(None, "Pairing Reset", "Your device's pairing was successfully reset. Refresh the device list before applying.")
        

    def add_skip_setup(self, files_to_restore: list[FileToRestore]):
        if self.skip_setup and not self.get_current_device_supported():
            # add the 2 skip setup files
            cloud_config_plist: dict = {
                "SkipSetup": ["WiFi", "Location", "Restore", "SIMSetup", "Android", "AppleID", "IntendedUser", "TOS", "Siri", "ScreenTime", "Diagnostics", "SoftwareUpdate", "Passcode", "Biometric", "Payment", "Zoom", "DisplayTone", "MessagingActivationUsingPhoneNumber", "HomeButtonSensitivity", "CloudStorage", "ScreenSaver", "TapToSetup", "Keyboard", "PreferredLanguage", "SpokenLanguage", "WatchMigration", "OnBoarding", "TVProviderSignIn", "TVHomeScreenSync", "Privacy", "TVRoom", "iMessageAndFaceTime", "AppStore", "Safety", "Multitasking", "ActionButton", "TermsOfAddress", "AccessibilityAppearance", "Welcome", "Appearance", "RestoreCompleted", "UpdateCompleted"],
                "CloudConfigurationUIComplete": True,
                "IsSupervised": False
            }
            files_to_restore.append(FileToRestore(
                contents=plistlib.dumps(cloud_config_plist),
                restore_path="systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/CloudConfigurationDetails.plist",
                domain="SysSharedContainerDomain-."
            ))
            purplebuddy_plist: dict = {
                "SetupDone": True,
                "SetupFinishedAllSteps": True,
                "UserChoseLanguage": True
            }
            files_to_restore.append(FileToRestore(
                contents=plistlib.dumps(purplebuddy_plist),
                restore_path="mobile/com.apple.purplebuddy.plist",
                domain="ManagedPreferencesDomain"
            ))

    def get_domain_for_path(self, path: str) -> str:
        mappings: dict = {
            "/var/Managed Preferences/": "ManagedPreferencesDomain",
            "/var/root/": "RootDomain",
            "/var/preferences/": "SystemPreferencesDomain",
            "/var/MobileDevice/": "MobileDeviceDomain",
            "/var/mobile/": "HomeDomain",
            "/var/db/": "DatabaseDomain",
            "/var/containers/Shared/SystemGroup/": "SysSharedContainerDomain-.",
            "/var/containers/Data/SystemGroup/": "SysContainerDomain-."
        }
        for mapping in mappings.keys():
            if path.startswith(mapping):
                new_path = path.replace(mapping, "")
                return mappings[mapping], new_path
        return None, path
    
    def concat_file(self, contents: str, path: str, files_to_restore: list[FileToRestore]):
        if self.get_current_device_supported():
            files_to_restore.append(FileToRestore(
                contents=contents,
                restore_path=path
            ))
        else:
            domain, file_path = self.get_domain_for_path(path)
            files_to_restore.append(FileToRestore(
                contents=contents,
                restore_path=file_path,
                domain=domain
            ))
    
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
                elif isinstance(tweak, BasicPlistTweak) or isinstance(tweak, RdarFixTweak):
                    basic_plists = tweak.apply_tweak(basic_plists)
                else:
                    if gestalt_plist != None:
                        gestalt_plist = tweak.apply_tweak(gestalt_plist)
            # set the custom gestalt keys
            if gestalt_plist != None:
                gestalt_plist = CustomGestaltTweaks.apply_tweaks(gestalt_plist)
        
        gestalt_data = None
        if resetting:
            gestalt_data = b""
        elif gestalt_plist != None:
            gestalt_data = plistlib.dumps(gestalt_plist)
        
        # Generate backup
        update_label("Generating backup...")
        # create the restore file list
        files_to_restore: dict[FileToRestore] = [
        ]
        self.concat_file(
            contents=plistlib.dumps(flag_plist),
            path="/var/preferences/FeatureFlags/Global.plist",
            files_to_restore=files_to_restore
        )
        self.add_skip_setup(files_to_restore)
        if gestalt_data != None:
            self.concat_file(
                contents=gestalt_data,
                path="/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist",
                files_to_restore=files_to_restore
            )
        if eligibility_files:
            new_eligibility_files: dict[FileToRestore] = []
            if not self.get_current_device_supported():
                # update the files
                for file in eligibility_files:
                    self.concat_file(
                        contents=file.contents,
                        path=file.restore_path,
                        files_to_restore=new_eligibility_files
                    )
            else:
                new_eligibility_files = eligibility_files
            files_to_restore += new_eligibility_files
        if ai_file != None:
            self.concat_file(
                contents=ai_file.contents,
                path=ai_file.restore_path,
                files_to_restore=files_to_restore
            )
        for location, plist in basic_plists.items():
            self.concat_file(
                contents=plistlib.dumps(plist),
                path=location.value,
                files_to_restore=files_to_restore
            )
        # reset basic tweaks
        if resetting:
            empty_data = plistlib.dumps({})
            for location in FileLocationsList:
                self.concat_file(
                    contents=empty_data,
                    path=location.value,
                    files_to_restore=files_to_restore
                )

        # restore to the device
        update_label("Restoring to device...")
        try:
            restore_files(files=files_to_restore, reboot=self.auto_reboot, lockdown_client=self.data_singleton.current_device.ld)
            msg = "Your device will now restart."
            if not self.auto_reboot:
                msg = "Please restart your device to see changes."
            QMessageBox.information(None, "Success!", "All done! " + msg)
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
                show_error_msg(type(e).__name__ + ": " + repr(e))

    ## RESETTING MOBILE GESTALT
    def reset_mobilegestalt(self, settings: QSettings, update_label=lambda x: None):
        # restore to the device
        update_label("Restoring to device...")
        try:
            # remove the saved device model
            settings.setValue(self.data_singleton.current_device.uuid + "_model", "")
            domain, file_path = self.get_domain_for_path("/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")
            restore_files(files=[FileToRestore(
                    contents=b"",
                    restore_path=file_path,
                    domain=domain
                )], reboot=self.auto_reboot, lockdown_client=self.data_singleton.current_device.ld)
            msg = "Your device will now restart."
            if not self.auto_reboot:
                msg = "Please restart your device to see changes."
            QMessageBox.information(None, "Success!", "All done! " + msg)
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
                show_error_msg(type(e).__name__ + ": " + repr(e))
