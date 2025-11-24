import traceback
import plistlib
from tempfile import TemporaryDirectory
from typing import Optional
import os.path
from pathlib import Path

from cryptography import x509
from cryptography.hazmat.primitives.serialization import Encoding
from uuid import uuid4

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QSettings, QCoreApplication

from pymobiledevice3 import usbmux
from pymobiledevice3.ca import create_keybag_file
from pymobiledevice3.services.mobile_config import MobileConfigService
from pymobiledevice3.lockdown import create_using_usbmux
from pymobiledevice3.exceptions import MuxException, PasswordRequiredError, ConnectionTerminatedError, AccessDeniedError
from pymobiledevice3.services.installation_proxy import InstallationProxyService
from pymobiledevice3.services.house_arrest import HouseArrestService

from devicemanagement.constants import Device, Version
from devicemanagement.data_singleton import DataSingleton

from gui.apply_worker import ApplyAlertMessage
from gui.pages.pages_list import Page
from controllers.path_handler import fix_windows_path
from controllers.files_handler import get_bundle_files

from exceptions.nugget_exception import NuggetException

from tweaks.tweaks import tweaks, TweakID, FeatureFlagTweak, EligibilityTweak, AITweak, BasicPlistTweak, AdvancedPlistTweak, RdarFixTweak, NullifyFileTweak, StatusBarTweak
from tweaks.custom_gestalt_tweaks import CustomGestaltTweaks
from tweaks.posterboard.posterboard_tweak import PosterboardTweak
from tweaks.posterboard.template_options.templates_tweak import TemplatesTweak
from tweaks.basic_plist_locations import FileLocation

from restore.restore import restore_files, FileToRestore
from restore.bookrestore import perform_bookrestore
from restore.mbdb import _FileMode

def show_error_msg(txt: str, title: str = "Error!", icon = QMessageBox.Critical, detailed_txt: str = None):
    detailsBox = QMessageBox()
    detailsBox.setIcon(icon)
    detailsBox.setWindowTitle(title)
    detailsBox.setText(txt)
    if detailed_txt != None:
        detailsBox.setDetailedText(detailed_txt)
    detailsBox.exec()

def get_files_list_str(files_list: list[FileToRestore] = None) -> str:
    files_str: str = ""
    if files_list != None:
        files_str = "FILES LIST:"
        print("\nFile List:\n")
        for file in files_list:
            file_info = f"\n    Domain: {file.domain}\n    Path: {file.restore_path}"
            files_str += file_info
            print(file_info)
        files_list += "\n\n"
    return files_str

def show_apply_error(e: Exception, update_label=lambda x: None, files_list: list[FileToRestore] = None):
    print(traceback.format_exc())
    update_label("Failed to restore")
    if "Find My" in str(e):
        return ApplyAlertMessage(QCoreApplication.tr("Find My must be disabled in order to use this tool."),
                       detailed_txt=QCoreApplication.tr("Disable Find My from Settings (Settings -> [Your Name] -> Find My) and then try again."))
    elif "Encrypted Backup MDM" in str(e):
        return ApplyAlertMessage(QCoreApplication.tr("Nugget cannot be used on this device. Click Show Details for more info."),
                       detailed_txt=QCoreApplication.tr("Your device is managed and MDM backup encryption is on. This must be turned off in order for Nugget to work. Please do not use Nugget on your school/work device!"))
    elif "SessionInactive" in str(e) or "ConnectionAbortedError" in str(e):
        return ApplyAlertMessage(QCoreApplication.tr("The session was terminated. Refresh the device list and try again."))
    elif "PasswordRequiredError" in str(e):
        return ApplyAlertMessage(QCoreApplication.tr("Device is password protected! You must trust the computer on your device."),
                       detailed_txt=QCoreApplication.tr("Unlock your device. On the popup, click \"Trust\", enter your password, then try again."))
    elif isinstance(e, ConnectionTerminatedError):
        files_str: str = get_files_list_str(files_list)
        return ApplyAlertMessage(QCoreApplication.tr("Device failed in sending files. The file list is possibly corrupted or has duplicates. Click Show Details for more info."),
                                 detailed_txt=files_str + "TRACEBACK:\n\n" + str(traceback.format_exc()))
    elif isinstance(e, AccessDeniedError):
        return ApplyAlertMessage(QCoreApplication.tr("You must run the application as an administer to use BookRestore tweaks."), detailed_txt="Try running the program with sudo.")
    elif isinstance(e, NuggetException):
        return ApplyAlertMessage(str(e))
    else:
        files_str: str = get_files_list_str(files_list)
        return ApplyAlertMessage(type(e).__name__ + ": " + repr(e), detailed_txt=files_str + "TRACEBACK:\n\n" + str(traceback.format_exc()))

class DeviceManager:
    ## Class Functions
    def __init__(self):
        self.devices: list[Device] = []
        self.data_singleton = DataSingleton()
        self.current_device_index = 0

        # preferences
        # TODO: Move to its own class
        self.settings = None
        self.apply_over_wifi = False
        self.auto_reboot = True
        self.allow_risky_tweaks = False
        self.show_all_spoofable_models = False
        self.disable_tendies_limit = False
        self.restore_truststore = False
        self.skip_setup = True
        self.supervised = False
        self.organization_name = ""
    
    def get_devices(self, settings: QSettings, show_alert=lambda x: None):
        self.devices.clear()
        if self.settings == None:
            self.settings = settings
        # handle errors when failing to get connected devices
        try:
            connected_devices = usbmux.list_devices()
        except:
            sysmsg = QCoreApplication.tr("If you are on Linux, make sure you have usbmuxd and libimobiledevice installed.")
            if os.name == 'nt':
                sysmsg = QCoreApplication.tr("Make sure you have the \"Apple Devices\" app from the Microsoft Store or iTunes from Apple's website.")
            show_alert(ApplyAlertMessage(
                txt=QCoreApplication.tr("Failed to get device list. Click \"Show Details\" for the traceback.") + f"\n\n{sysmsg}", detailed_txt=str(traceback.format_exc())
            ))
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
                        books_uuid = settings.value(device.serial + "_books_container_uuid", "", type=str)
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
                        show_alert(ApplyAlertMessage(txt=QCoreApplication.tr("Click \"Show Details\" for the traceback."), detailed_txt=str(traceback.format_exc())))
                    dev = Device(
                            udid=device.serial,
                            usb=device.is_usb,
                            name=vals['DeviceName'],
                            version=vals['ProductVersion'],
                            build=vals['BuildVersion'],
                            model=model,
                            hardware=hardware,
                            cpu=cpu,
                            locale=ld.locale,
                            books_container_uuid=books_uuid,
                            ld=ld
                        )
                    if TweakID.RdarFix in tweaks:
                        tweaks[TweakID.RdarFix].get_rdar_mode(model)
                    self.devices.append(dev)
                except PasswordRequiredError as e:
                    show_alert(ApplyAlertMessage(txt=QCoreApplication.tr("Device is password protected! You must trust the computer on your device.\n\nUnlock your device. On the popup, click \"Trust\", enter your password, then try again.")))
                except MuxException as e:
                    # there is probably a cable issue
                    print(f"MUX ERROR with lockdown device with UUID {device.serial}")
                    show_alert(ApplyAlertMessage(txt="MuxException: " + repr(e) + "\n\n" + QCoreApplication.tr("If you keep receiving this error, try using a different cable or port."),
                                   detailed_txt=str(traceback.format_exc())))
                except Exception as e:
                    print(f"ERROR with lockdown device with UUID {device.serial}")
                    show_alert(ApplyAlertMessage(txt=f"{type(e).__name__}: {repr(e)}", detailed_txt=str(traceback.format_exc())))
        
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
            if TweakID.SpoofModel in tweaks:
                tweaks[TweakID.SpoofModel].value[0] = "Placeholder"
                tweaks[TweakID.SpoofHardware].value[0] = "Placeholder"
                tweaks[TweakID.SpoofCPU].value[0] = "Placeholder"
        else:
            self.data_singleton.current_device = self.devices[index]
            if Version(self.devices[index].version) < Version("17.0"):
                self.data_singleton.device_available = False
                self.data_singleton.gestalt_path = None
            else:
                self.data_singleton.device_available = True
                if TweakID.SpoofModel in tweaks:
                    tweaks[TweakID.SpoofModel].value[0] = self.data_singleton.current_device.model
                    tweaks[TweakID.SpoofHardware].value[0] = self.data_singleton.current_device.hardware
                    tweaks[TweakID.SpoofCPU].value[0] = self.data_singleton.current_device.cpu
            self.current_device_index = index
        
    def get_current_device_name(self) -> str:
        if self.data_singleton.current_device == None:
            return QCoreApplication.tr("No Device")
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
            return self.data_singleton.current_device.udid
        
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
    
    def get_current_device_uses_bookrestore(self) -> bool:
        if self.data_singleton.current_device == None:
            return False
        else:
            return self.data_singleton.current_device.has_bookrestore()
    
    def get_current_device_patched(self) -> bool:
        if self.data_singleton.current_device == None:
            return True
        else:
            return self.data_singleton.current_device.is_exploit_fully_patched()
        
    def current_device_books_container_uuid_callback(self, uuid: Optional[str]=None) -> Optional[str | None]:
        # if there is no argument, return the existing uuid
        if uuid is None:
            return self.data_singleton.current_device.books_container_uuid
        self.data_singleton.current_device.books_container_uuid = uuid
        # save it to settings
        self.settings.setValue(self.data_singleton.current_device.udid + "_books_container_uuid", uuid)
        
    def get_app_hashes(self, bundle_ids: list[str]) -> dict:
        apps = InstallationProxyService(lockdown=self.data_singleton.current_device.ld).get_apps(application_type="Any", calculate_sizes=False)
        results = {}
        for bundle_id in bundle_ids:
            app_info = apps[bundle_id]
            results[bundle_id] = app_info["Container"].removeprefix("/private/var/mobile/Containers/Data/Application/")
        return results
    
    def send_app_hashes_afc(self, hashes: dict) -> str:
        # create a temporary file to send it as
        with TemporaryDirectory() as tmpdir:
            # get the bundle id of Pocket Poster
            bundle_id = "com.leemin.Pocket-Poster"
            apps = InstallationProxyService(lockdown=self.data_singleton.current_device.ld).get_apps(application_type="User", calculate_sizes=False)
            for app in apps.values():
                if app["CFBundleExecutable"] == "Pocket Poster":
                    bundle_id = app["CFBundleIdentifier"]
                    break
                elif app["CFBundleExecutable"] == "LiveContainer":
                    # fallback for live container
                    bundle_id = app["CFBundleIdentifier"]
            afc = HouseArrestService(lockdown=self.data_singleton.current_device.ld, bundle_id=bundle_id, documents_only=True)
            # send each hash over
            for key in hashes.keys():
                fname = "Nugget" + key.replace("com.apple.", "") + "Hash"
                tmpf = os.path.join(tmpdir, fname)
                with open(tmpf, "w", encoding='UTF-8') as in_file:
                    in_file.write(hashes[key])
                afc.push(tmpf, f"/Documents/{fname}")
        

    def reset_device_pairing(self):
        # first, unpair it
        if self.data_singleton.current_device == None:
            return
        self.data_singleton.current_device.ld.unpair()
        # next, pair it again
        self.data_singleton.current_device.ld.pair()
        QMessageBox.information(None, QCoreApplication.tr("Pairing Reset"), QCoreApplication.tr("Your device's pairing was successfully reset. Refresh the device list before applying."))
        

    def add_skip_setup(self, files_to_restore: list[FileToRestore], restoring_domains: bool):
        # TODO: Probably should move this to its own file
        if self.skip_setup and (not self.get_current_device_supported() or restoring_domains):
            # get the already existing cloud config info
            cloud_config_plist = MobileConfigService(lockdown=self.data_singleton.current_device.ld).get_cloud_configuration()
            # add the 2 skip setup files
            cloud_config_plist["SkipSetup"] = [
                    'Location',
                    'Restore',
                    'SIMSetup',
                    'Android',
                    'AppleID',
                    'IntendedUser',
                    'TOS',
                    'Siri',
                    'ScreenTime',
                    'Diagnostics',
                    'SoftwareUpdate',
                    'Passcode',
                    'Biometric',
                    'Payment',
                    'Zoom',
                    'DisplayTone',
                    'MessagingActivationUsingPhoneNumber',
                    'HomeButtonSensitivity',
                    'CloudStorage',
                    'ScreenSaver',
                    'TapToSetup',
                    'Keyboard',
                    'PreferredLanguage',
                    'SpokenLanguage',
                    'WatchMigration',
                    'OnBoarding',
                    'TVProviderSignIn',
                    'TVHomeScreenSync',
                    'Privacy',
                    'TVRoom',
                    'iMessageAndFaceTime',
                    'AppStore',
                    'Safety',
                    'Multitasking',
                    'ActionButton',
                    'TermsOfAddress',
                    'AccessibilityAppearance',
                    'Welcome',
                    'Appearance',
                    'RestoreCompleted',
                    'UpdateCompleted',
                    'WiFi',
                    'Display',
                    'Tone',
                    'LanguageAndLocale',
                    'TouchID',
                    'TrueToneDisplay',
                    'FileVault',
                    'iCloudStorage',
                    'iCloudDiagnostics',
                    'Registration',
                    'DeviceToDeviceMigration',
                    'UnlockWithWatch',
                    'Accessibility',
                    'All',
                    'ExpressLanguage',
                    'Language',
                    'N/A',
                    'Region',
                    'Avatar',
                    'DeviceProtection',
                    'Key',
                    'LockdownMode',
                    'Wallpaper',
                    'PrivacySubtitle',
                    'SecuritySubtitle',
                    'DataSubtitle',
                    'AppleIDSubtitle',
                    'AppearanceSubtitle',
                    'PreferredLang',
                    'OnboardingSubtitle',
                    'AppleTVSubtitle',
                    'Intelligence',
                    'WebContentFiltering',
                    'CameraButton',
                    'AdditionalPrivacySettings',
                    'EnableLockdownMode',
                    'OSShowcase',
                    'SafetyAndHandling',
                    'Tips',
                    "AgeBasedSafetySettings",
                ]
            cloud_config_plist["AllowPairing"] = True
            cloud_config_plist["ConfigurationWasApplied"] = True
            cloud_config_plist["CloudConfigurationUIComplete"] = True
            cloud_config_plist["IsSupervised"] = False
            cloud_config_plist["ConfigurationSource"] = 0
            cloud_config_plist["PostSetupProfileWasInstalled"] = True
            if self.supervised == True:
                cloud_config_plist["IsSupervised"] = True
                # create/add the keybag
                if self.organization_name != None and self.organization_name != "":
                    with TemporaryDirectory() as temp_dir:
                        keybag_file = Path(temp_dir) / 'keybag'
                        create_keybag_file(keybag_file, self.organization_name)
                        cer = x509.load_pem_x509_certificate(keybag_file.read_bytes())
                        public_key = cer.public_bytes(Encoding.DER)
                        # make sure the mdm is removable
                        cloud_config_plist["OrganizationName"] = self.organization_name
                        cloud_config_plist['OrganizationMagic'] = str(uuid4())
                        cloud_config_plist['IsMDMUnremovable'] = False
                        cloud_config_plist['SupervisorHostCertificates'] = [public_key]
                else:
                    # remove keybag info
                    if 'OrganizationMagic' in cloud_config_plist:
                        cloud_config_plist.pop('OrganizationMagic')
                    if 'SupervisorHostCertificates' in cloud_config_plist:
                        cloud_config_plist.pop('SupervisorHostCertificates')
                    if not 'OrganizatonName' in cloud_config_plist:
                        # need to add it anyway
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

    def get_domain_for_path(self, path: str, owner: int = 501, use_bookrestore: bool = False) -> str:
        # returns Domain: str?, Path: str
        if ((self.get_current_device_supported() and not path.startswith("/var/mobile/")) or (self.get_current_device_uses_bookrestore() and use_bookrestore)) and not owner == 0:# and not uses_domains:
            # don't do anything on sparserestore versions
            return path, ""
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
        return path, ""
    
    def concat_file(self, contents: str, path: str, files_to_restore: list[FileToRestore], owner: int = 501, group: int = 501, uses_domains: bool = False):
        # TODO: try using inodes here instead
        file_path, domain = self.get_domain_for_path(path, owner=owner, use_bookrestore=uses_domains)
        files_to_restore.append(FileToRestore(
            contents=contents,
            restore_path=file_path,
            domain=domain,
            owner=owner, group=group
        ))
    
    ## APPLYING OR REMOVING TWEAKS AND RESTORING
    def progress_callback(self, progress: int):
        if self.update_label == None:
            return
        prog = ""
        if progress != None:
            prog = f" ({progress:6.1f}% )"
        self.update_label(QCoreApplication.tr("Restoring to device...{0}{1}").format(prog, self.do_not_unplug))
    def apply_changes(self, update_label=lambda x: None, show_alert=lambda x: None):
        try:
            # set the tweaks and apply
            # first open the file in read mode
            update_label(QCoreApplication.tr("Applying changes to files..."))
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
            use_bookrestore: bool = False
            # create the restore file list
            files_to_restore: list[FileToRestore] = [
            ]
            tmp_dirs = [] # temporary directory for unzipping pb and template files

            # set the plist keys
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
                elif isinstance(tweak, PosterboardTweak) or isinstance(tweak, TemplatesTweak):
                    tmp_dirs.append(TemporaryDirectory())
                    tweak.apply_tweak(
                        files_to_restore=files_to_restore,
                        output_dir=fix_windows_path(tmp_dirs[len(tmp_dirs)-1].name),
                        templates=tweaks[TweakID.Templates].templates,
                        version=self.get_current_device_version(), update_label=update_label
                    )
                    if tweak.uses_domains():
                        uses_domains = True
                elif isinstance(tweak, StatusBarTweak):
                    tweak.apply_tweak(files_to_restore=files_to_restore)
                    if tweak.enabled:
                        uses_domains = True
                else:
                    if gestalt_plist != None:
                        gestalt_plist = tweak.apply_tweak(gestalt_plist)
                        if tweak.enabled:
                            use_bookrestore = True
                    elif tweak.enabled:
                        # no mobilegestalt file provided but applying mga tweaks, give warning
                        show_alert(ApplyAlertMessage(txt=QCoreApplication.tr("No mobilegestalt file provided! Please select your file to apply mobilegestalt tweaks.")))
                        update_label("Failed.")
                        return
            # set the custom gestalt keys
            if gestalt_plist != None:
                gestalt_plist = CustomGestaltTweaks.apply_tweaks(gestalt_plist)
            
            gestalt_data = None
            if gestalt_plist != None:
                gestalt_data = plistlib.dumps(gestalt_plist)
            
            # Generate backup
            update_label(QCoreApplication.tr("Generating backup..."))
            if len(flag_plist) > 0:
                self.concat_file(
                    contents=plistlib.dumps(flag_plist),
                    path="/var/preferences/FeatureFlags/Global.plist",
                    files_to_restore=files_to_restore
                )
            self.add_skip_setup(files_to_restore, uses_domains and not use_bookrestore)
            if gestalt_data != None and use_bookrestore:
                self.concat_file(
                    contents=gestalt_data,
                    path="/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist",
                    files_to_restore=files_to_restore, uses_domains=True
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
                if location in basic_plists_ownership:
                    ownership = basic_plists_ownership[location]
                else:
                    ownership = 501
                self.concat_file(
                    contents=plistlib.dumps(plist),
                    path=location.value,
                    files_to_restore=files_to_restore,
                    owner=ownership, group=ownership, uses_domains=use_bookrestore
                )
            for location, data in files_data.items():
                if isinstance(data, NullifyFileTweak):
                    ownership = data.owner
                else:
                    ownership = 501
                self.concat_file(
                    contents=data,
                    path=location.value,
                    files_to_restore=files_to_restore,
                    owner=ownership, group=ownership
                )

            # Restore Mobileconfig Profiles
            # Read multiple configuration files from a directory
            # config_files = glob.glob('path/to/configuration/files/*.stub')

            # for idx, config_file in enumerate(config_files):
            #     with open(config_file, 'rb') as f:
            #         content = f.read()

            #     original_file_name = config_file.split('/')[-1]
            #     files_to_restore.append(FileToRestore(
            #         contents=content,
            #         restore_path=f"Library/ConfigurationProfiles/{original_file_name}",
            #         domain="SysSharedContainerDomain-systemgroup.com.apple.configurationprofiles"
            #     ))

            # Restore SSL Configuration Profiles
            if uses_domains and self.restore_truststore:
                with open(get_bundle_files('files/SSLconf/TrustStore.sqlite3'), 'rb') as f:
                    certsDB = f.read()

                files_to_restore.append(FileToRestore(
                    contents=certsDB,
                    restore_path="trustd/private/TrustStore.sqlite3",
                    domain="ProtectedDomain",
                    owner=501, group=501,
                    mode=_FileMode.S_IRUSR | _FileMode.S_IWUSR  | _FileMode.S_IRGRP | _FileMode.S_IWGRP | _FileMode.S_IROTH | _FileMode.S_IWOTH
                ))

            # restore to the device
            self.update_label = update_label
            self.do_not_unplug = ""
            if self.data_singleton.current_device.connected_via_usb:
                self.do_not_unplug = "\n" + QCoreApplication.tr("DO NOT UNPLUG")
            if use_bookrestore and not self.data_singleton.current_device.has_partial_sparserestore():
                update_label(QCoreApplication.tr("Creating connection to device...") + self.do_not_unplug)
                perform_bookrestore(files=files_to_restore, lockdown_client=self.data_singleton.current_device.ld, current_device_books_uuid_callback=self.current_device_books_container_uuid_callback, progress_callback=self.update_label)
            else:
                update_label(QCoreApplication.tr("Preparing to restore...") + self.do_not_unplug)
                restore_files(
                    files=files_to_restore, reboot=self.auto_reboot,
                    lockdown_client=self.data_singleton.current_device.ld,
                    progress_callback=self.progress_callback
                )
            msg = ""#QCoreApplication.tr("Your device will now restart.\n\nRemember to turn Find My back on!")
            if not self.auto_reboot:
                msg = QCoreApplication.tr("Please restart your device to see changes.")
            final_alert = ApplyAlertMessage(txt=QCoreApplication.tr("All done! ") + msg, title=QCoreApplication.tr("Success!"), icon=QMessageBox.Information)
            update_label(QCoreApplication.tr("Success!"))
        except Exception as e:
            final_alert = show_apply_error(e, update_label, files_list=files_to_restore)
        finally:
            if len(tmp_dirs) > 0:
                for tmp_dir in tmp_dirs:
                    try:
                        tmp_dir.cleanup()
                    except Exception as e:
                        # ignore clean up errors
                        print(str(e))
            show_alert(final_alert)

    ## RESETTING TWEAKS
    def reset_tweaks(self, reset_pages: list[Page], settings: QSettings, update_label=lambda x: None, show_alert=lambda x: None):
        try:
            # create the restore file list
            files_to_restore: list[FileToRestore] = []
            # Generate backup
            update_label(QCoreApplication.tr("Generating backup..."))
            files_to_null: list[str] = []
            uses_domains = False

            # use if-statements instead of match (switch) statements for compatibility with Python 3.9
            for page in reset_pages:
                if page == Page.Gestalt:
                    ## MOBILE GESTALT
                    # remove the saved device model, hardware, and cpu
                    settings.setValue(self.data_singleton.current_device.udid + "_model", "")
                    settings.setValue(self.data_singleton.current_device.udid + "_hardware", "")
                    settings.setValue(self.data_singleton.current_device.udid + "_cpu", "")
                    files_to_null.append("/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")
                elif page == Page.FeatureFlags:
                    ## FEATURE FLAGS
                    files_to_null.append("/var/preferences/FeatureFlags/Global.plist")
                elif page == Page.StatusBar:
                    ## STATUS BAR
                    files_to_restore.append(FileToRestore(
                        contents=b"",
                        restore_path="/Library/SpringBoard/statusBarOverrides",
                        domain="HomeDomain"
                    ))
                    uses_domains = True
                elif page == Page.Daemons:
                    ## DAEMONS
                    default_daemons = {
                        "com.apple.magicswitchd.companion": True,
                        "com.apple.security.otpaird": True,
                        "com.apple.dhcp6d": True,
                        "com.apple.bootpd": True,
                        "com.apple.ftp-proxy-embedded": False,
                        "com.apple.relevanced": True
                    }
                    self.concat_file(
                        contents=plistlib.dumps(default_daemons),
                        path=FileLocation.disabledDaemons.value,
                        files_to_restore=files_to_restore,
                        owner=0, group=0
                    )
                    uses_domains = True
                elif page == Page.RiskyTweaks:
                    ## RESOLUTION MODIFICATIONS
                    files_to_null.append(FileLocation.resolution.value)
                elif page == Page.Springboard:
                    ## SPRINGBOARD
                    files_to_null.append(FileLocation.springboard.value)
                    files_to_null.append(FileLocation.uikit.value)
                elif page == Page.InternalOptions:
                    ## INTERNAL OPTIONS
                    files_to_null.append(FileLocation.globalPreferences.value)
                    files_to_null.append(FileLocation.appStore.value)
                    files_to_null.append(FileLocation.backboardd.value)
                    files_to_null.append(FileLocation.coreMotion.value)
                    files_to_null.append(FileLocation.pasteboard.value)
                    files_to_null.append(FileLocation.notes.value)
            
            # add the files to null from the list
            for file_path in files_to_null:
                self.concat_file(
                    contents=b"",
                    path=file_path,
                    files_to_restore=files_to_restore
                )
            
            self.add_skip_setup(files_to_restore, uses_domains)

            # restore to the device
            self.update_label = update_label
            self.do_not_unplug = ""
            if self.data_singleton.current_device.connected_via_usb:
                self.do_not_unplug = f"\n{QCoreApplication.tr('DO NOT UNPLUG')}"
            update_label(f"{QCoreApplication.tr('Preparing to restore...')}{self.do_not_unplug}")
            restore_files(
                files=files_to_restore, reboot=self.auto_reboot,
                lockdown_client=self.data_singleton.current_device.ld,
                progress_callback=self.progress_callback
            )
            msg = QCoreApplication.tr("Your device will now restart.\n\nRemember to turn Find My back on!")
            if not self.auto_reboot:
                msg = QCoreApplication.tr("Please restart your device to see changes.")
            final_alert = ApplyAlertMessage(txt=QCoreApplication.tr("All done! ") + msg, title=QCoreApplication.tr("Success!"), icon=QMessageBox.Information)
            update_label(QCoreApplication.tr("Success!"))
        except Exception as e:
            final_alert = show_apply_error(e, update_label, files_list=files_to_restore)
        finally:
            show_alert(final_alert)
