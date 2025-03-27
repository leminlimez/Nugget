import traceback
import plistlib
from tempfile import TemporaryDirectory

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QSettings, QThread

from pymobiledevice3 import usbmux
from pymobiledevice3.lockdown import create_using_usbmux
from pymobiledevice3.exceptions import MuxException, PasswordRequiredError

from devicemanagement.constants import Device, Version
from devicemanagement.data_singleton import DataSingleton

from gui.apply_worker import ApplyAlertMessage
from tweaks.tweaks import tweaks, FeatureFlagTweak, EligibilityTweak, AITweak, BasicPlistTweak, AdvancedPlistTweak, RdarFixTweak, NullifyFileTweak
from tweaks.custom_gestalt_tweaks import CustomGestaltTweaks
from tweaks.posterboard_tweak import PosterboardTweak
from tweaks.basic_plist_locations import FileLocationsList, RiskyFileLocationsList
from Sparserestore.restore import restore_files, FileToRestore

def show_error_msg(txt: str, title: str = "Error!", icon = QMessageBox.Critical, detailed_txt: str = None):
    detailsBox = QMessageBox()
    detailsBox.setIcon(icon)
    detailsBox.setWindowTitle(title)
    detailsBox.setText(txt)
    if detailed_txt != None:
        detailsBox.setDetailedText(detailed_txt)
    detailsBox.exec()

def show_apply_error(e: Exception, update_label=lambda x: None):
    print(traceback.format_exc())
    update_label("Failed to restore")
    if "Find My" in str(e):
        return ApplyAlertMessage("Find My must be disabled in order to use this tool.",
                       detailed_txt="Disable Find My from Settings (Settings -> [Your Name] -> Find My) and then try again.")
    elif "Encrypted Backup MDM" in str(e):
        return ApplyAlertMessage("Nugget cannot be used on this device. Click Show Details for more info.",
                       detailed_txt="Your device is managed and MDM backup encryption is on. This must be turned off in order for Nugget to work. Please do not use Nugget on your school/work device!")
    elif "SessionInactive" in str(e):
        return ApplyAlertMessage("The session was terminated. Refresh the device list and try again.")
    elif "PasswordRequiredError" in str(e):
        return ApplyAlertMessage("Device is password protected! You must trust the computer on your device.",
                       detailed_txt="Unlock your device. On the popup, click \"Trust\", enter your password, then try again.")
    else:
        return ApplyAlertMessage(type(e).__name__ + ": " + repr(e), detailed_txt=str(traceback.format_exc()))

class DeviceManager:
    ## Class Functions
    def __init__(self):
        self.devices: list[Device] = []
        self.data_singleton = DataSingleton()
        self.current_device_index = 0

        # preferences
        # TODO: Move to its own class
        self.apply_over_wifi = False
        self.auto_reboot = True
        self.allow_risky_tweaks = False
        self.windows_path_fix = True
        self.show_all_spoofable_models = False
        self.skip_setup = True
        self.supervised = False
        self.organization_name = ""
    
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
                """, detailed_txt=str(traceback.format_exc())
            )
            self.set_current_device(index=None)
            return
        # Connect via usbmuxd
        for device in connected_devices:
            if self.apply_over_wifi or device.is_usb:
                try:
                    ld = create_using_usbmux(serial=device.serial)
                    vals = ld.all_values
                    model = vals['ProductType']
                    hardware = vals['HardwareModel']
                    cpu = vals['HardwarePlatform']
                    try:
                        product_type = settings.value(device.serial + "_model", "", type=str)
                        hardware_type = settings.value(device.serial + "_hardware", "", type=str)
                        cpu_type = settings.value(device.serial + "_cpu", "", type=str)
                        if product_type == "":
                            # save the new product type
                            settings.setValue(device.serial + "_model", model)
                        else:
                            model = product_type
                        if hardware_type == "":
                            # save the new hardware model
                            settings.setValue(device.serial + "_hardware", hardware)
                        else:
                            hardware = hardware_type
                        if cpu_type == "":
                            # save the new cpu model
                            settings.setValue(device.serial + "_cpu", cpu)
                        else:
                            cpu = cpu_type
                    except:
                        pass
                    dev = Device(
                            uuid=device.serial,
                            usb=device.is_usb,
                            name=vals['DeviceName'],
                            version=vals['ProductVersion'],
                            build=vals['BuildVersion'],
                            model=model,
                            hardware=hardware,
                            cpu=cpu,
                            locale=ld.locale,
                            ld=ld
                        )
                    tweaks["RdarFix"].get_rdar_mode(model)
                    self.devices.append(dev)
                except MuxException as e:
                    # there is probably a cable issue
                    print(f"MUX ERROR with lockdown device with UUID {device.serial}")
                    show_error_msg("MuxException: " + repr(e) + "\n\nIf you keep receiving this error, try using a different cable or port.",
                                   detailed_txt=str(traceback.format_exc()))
                except Exception as e:
                    print(f"ERROR with lockdown device with UUID {device.serial}")
                    show_error_msg(type(e).__name__ + ": " + repr(e), detailed_txt=str(traceback.format_exc()))
        
        if len(self.devices) > 0:
            self.set_current_device(index=0)
        else:
            self.set_current_device(index=None)

    ## CURRENT DEVICE
    def set_current_device(self, index: int = None):
        if index == None or len(self.devices) == 0:
            self.data_singleton.current_device = None
            self.data_singleton.device_available = False
            self.data_singleton.gestalt_path = None
            self.current_device_index = 0
            tweaks["SpoofModel"].value[0] = "Placeholder"
            tweaks["SpoofHardware"].value[0] = "Placeholder"
            tweaks["SpoofCPU"].value[0] = "Placeholder"
        else:
            self.data_singleton.current_device = self.devices[index]
            if Version(self.devices[index].version) < Version("17.0"):
                self.data_singleton.device_available = False
                self.data_singleton.gestalt_path = None
            else:
                self.data_singleton.device_available = True
                tweaks["SpoofModel"].value[0] = self.data_singleton.current_device.model
                tweaks["SpoofHardware"].value[0] = self.data_singleton.current_device.hardware
                tweaks["SpoofCPU"].value[0] = self.data_singleton.current_device.cpu
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
        
    def get_current_device_model(self) -> str:
        if self.data_singleton.current_device == None:
            return ""
        else:
            return self.data_singleton.current_device.model
        
    def get_current_device_supported(self) -> bool:
        if self.data_singleton.current_device == None:
            return False
        else:
            return self.data_singleton.current_device.supported()
    
    def get_current_device_patched(self) -> bool:
        if self.data_singleton.current_device == None:
            return True
        else:
            return self.data_singleton.current_device.is_exploit_fully_patched()
        

    def reset_device_pairing(self):
        # first, unpair it
        if self.data_singleton.current_device == None:
            return
        self.data_singleton.current_device.ld.unpair()
        # next, pair it again
        self.data_singleton.current_device.ld.pair()
        QMessageBox.information(None, "Pairing Reset", "Your device's pairing was successfully reset. Refresh the device list before applying.")
        

    def add_skip_setup(self, files_to_restore: list[FileToRestore], restoring_domains: bool):
        if self.skip_setup and (not self.get_current_device_supported() or restoring_domains):
            # add the 2 skip setup files
            cloud_config_plist: dict = {
                "SkipSetup": ["WiFi", "Location", "Restore", "SIMSetup", "Android", "AppleID", "IntendedUser", "TOS", "Siri", "ScreenTime", "Diagnostics", "SoftwareUpdate", "Passcode", "Biometric", "Payment", "Zoom", "DisplayTone", "MessagingActivationUsingPhoneNumber", "HomeButtonSensitivity", "CloudStorage", "ScreenSaver", "TapToSetup", "Keyboard", "PreferredLanguage", "SpokenLanguage", "WatchMigration", "OnBoarding", "TVProviderSignIn", "TVHomeScreenSync", "Privacy", "TVRoom", "iMessageAndFaceTime", "AppStore", "Safety", "Multitasking", "ActionButton", "TermsOfAddress", "AccessibilityAppearance", "Welcome", "Appearance", "RestoreCompleted", "UpdateCompleted"],
                "AllowPairing": True,
                "ConfigurationWasApplied": True,
                "CloudConfigurationUIComplete": True,
                "ConfigurationSource": 0,
                "PostSetupProfileWasInstalled": True,
                "IsSupervised": False,
            }
            if self.supervised == True:
                cloud_config_plist["IsSupervised"] = True
                cloud_config_plist["OrganizationName"] = self.organization_name
            files_to_restore.append(FileToRestore(
                contents=plistlib.dumps(cloud_config_plist),
                restore_path="Library/ConfigurationProfiles/CloudConfigurationDetails.plist",
                domain="SysSharedContainerDomain-systemgroup.com.apple.configurationprofiles"
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

    def get_domain_for_path(self, path: str, owner: int = 501) -> str:
        # returns Domain: str?, Path: str
        if self.get_current_device_supported() and not path.startswith("/var/mobile/") and not owner == 0:
            # don't do anything on sparserestore versions
            return path, None
        fully_patched = self.get_current_device_patched()
        # just make the Sys Containers to use the regular way (won't work for mga)
        sysSharedContainer = "SysSharedContainerDomain-"
        sysContainer = "SysContainerDomain-"
        if not fully_patched:
            sysSharedContainer += "."
            sysContainer += "."
        mappings: dict = {
            "/var/Managed Preferences/": "ManagedPreferencesDomain",
            "/var/root/": "RootDomain",
            "/var/preferences/": "SystemPreferencesDomain",
            "/var/MobileDevice/": "MobileDeviceDomain",
            "/var/mobile/": "HomeDomain",
            "/var/db/": "DatabaseDomain",
            "/var/containers/Shared/SystemGroup/": sysSharedContainer,
            "/var/containers/Data/SystemGroup/": sysContainer
        }
        for mapping in mappings.keys():
            if path.startswith(mapping):
                new_path = path.replace(mapping, "")
                new_domain = mappings[mapping]
                # if patched, include the next part of the path in the domain
                if fully_patched and (new_domain == sysSharedContainer or new_domain == sysContainer):
                    parts = new_path.split("/")
                    new_domain += parts[0]
                    new_path = new_path.replace(parts[0] + "/", "")
                return new_path, new_domain
        return path, None
    
    def concat_file(self, contents: str, path: str, files_to_restore: list[FileToRestore], owner: int = 501, group: int = 501):
        # TODO: try using inodes here instead
        file_path, domain = self.get_domain_for_path(path, owner=owner)
        files_to_restore.append(FileToRestore(
            contents=contents,
            restore_path=file_path,
            domain=domain,
            owner=owner, group=group
        ))
    
    ## APPLYING OR REMOVING TWEAKS AND RESTORING
    def apply_changes(self, resetting: bool = False, update_label=lambda x: None, show_alert=lambda x: None):
        try:
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
            basic_plists_ownership: dict = {}
            files_data: dict = {}
            uses_domains: bool = False
            # create the restore file list
            files_to_restore: dict[FileToRestore] = [
            ]
            tmp_pb_dir = None # temporary directory for unzipping pb files

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
                    elif isinstance(tweak, BasicPlistTweak) or isinstance(tweak, RdarFixTweak) or isinstance(tweak, AdvancedPlistTweak):
                        basic_plists = tweak.apply_tweak(basic_plists, self.allow_risky_tweaks)
                        basic_plists_ownership[tweak.file_location] = tweak.owner
                        if tweak.enabled and tweak.owner == 0:
                            uses_domains = True
                    elif isinstance(tweak, NullifyFileTweak):
                        tweak.apply_tweak(files_data)
                        if tweak.enabled and tweak.file_location.value.startswith("/var/mobile/"):
                            uses_domains = True
                    elif isinstance(tweak, PosterboardTweak):
                        tmp_pb_dir = TemporaryDirectory()
                        tweak.apply_tweak(
                            files_to_restore=files_to_restore, output_dir=tmp_pb_dir.name,
                            windows_path_fix=self.windows_path_fix, update_label=update_label
                        )
                        if tweak.enabled:
                            uses_domains = True
                    else:
                        if gestalt_plist != None:
                            gestalt_plist = tweak.apply_tweak(gestalt_plist)
                        elif tweak.enabled:
                            # no mobilegestalt file provided but applying mga tweaks, give warning
                            show_alert(show_error_msg("No mobilegestalt file provided! Please select your file to apply mobilegestalt tweaks.", exec=False))
                            update_label("Failed.")
                            return
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
            self.concat_file(
                contents=plistlib.dumps(flag_plist),
                path="/var/preferences/FeatureFlags/Global.plist",
                files_to_restore=files_to_restore
            )
            self.add_skip_setup(files_to_restore, uses_domains)
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
                ownership = basic_plists_ownership[location]
                self.concat_file(
                    contents=plistlib.dumps(plist),
                    path=location.value,
                    files_to_restore=files_to_restore,
                    owner=ownership, group=ownership
                )
            for location, data in files_data.items():
                self.concat_file(
                    contents=data,
                    path=location.value,
                    files_to_restore=files_to_restore,
                    owner=ownership, group=ownership
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
                if self.allow_risky_tweaks:
                    for location in RiskyFileLocationsList:
                        self.concat_file(
                            contents=empty_data,
                            path=location.value,
                            files_to_restore=files_to_restore
                        )

            # restore to the device
            update_label("Restoring to device...")
            restore_files(files=files_to_restore, reboot=self.auto_reboot, lockdown_client=self.data_singleton.current_device.ld)
            if tmp_pb_dir != None:
                tmp_pb_dir.cleanup()
            msg = "Your device will now restart."
            if not self.auto_reboot:
                msg = "Please restart your device to see changes."
            show_alert(ApplyAlertMessage(txt="All done! " + msg, title="Success!", icon=QMessageBox.Information))
            update_label("Success!")
        except Exception as e:
            if tmp_pb_dir != None:
                tmp_pb_dir.cleanup()
            show_alert(show_apply_error(e, update_label))

    ## RESETTING MOBILE GESTALT
    def reset_mobilegestalt(self, settings: QSettings, update_label=lambda x: None):
        # restore to the device
        update_label("Restoring to device...")
        try:
            # remove the saved device model, hardware, and cpu
            settings.setValue(self.data_singleton.current_device.uuid + "_model", "")
            settings.setValue(self.data_singleton.current_device.uuid + "_hardware", "")
            settings.setValue(self.data_singleton.current_device.uuid + "_cpu", "")
            file_path, domain = self.get_domain_for_path(
                "/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist"
            )
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
            show_error_msg(str(e))
