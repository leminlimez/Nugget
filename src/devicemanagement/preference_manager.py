import plistlib

from PySide6.QtCore import QSettings
from src.restore.bookrestore import BookRestoreFileTransferMethod, BookRestoreApplyMethod

class PreferenceManager:
    def __init__(self, settings: QSettings):
        self.settings = settings
        self.apply_over_wifi = False
        self.auto_reboot = True
        self.allow_risky_tweaks = False
        self.show_all_spoofable_models = False
        self.disable_tendies_limit = False
        self.restore_truststore = False
        self.bookrestore_apply_mode = BookRestoreApplyMethod.AFC
        self.bookrestore_transfer_mode = BookRestoreFileTransferMethod.LocalHost
        self.skip_setup = True
        self.supervised = False
        self.organization_name = ""

    def get_mga_prefs(self) -> QSettings:
        return QSettings("Nugget", "MGA Data")

    def save_mga_file(self, filepath: str, udid: str):
        mga_settings = self.get_mga_prefs()
        with open(filepath, 'rb') as mga_file:
            mga_settings.setValue(udid, mga_file.read())

    def remove_mga_data(self, udid: str):
        mga_settings = self.get_mga_prefs()
        if mga_settings.contains(udid):
            mga_settings.remove(udid)

    def has_mga_data(self, udid: str) -> bool:
        return self.get_mga_prefs().contains(udid)
    def has_valid_mga_data(self, udid: str, build: str, model: str) -> bool:
        # makes sure that it matches the build/model as well as existing
        # also removes it if the build/model don't match
        data = self.get_mga_data(udid)
        if data == None:
            return False
        if not self.is_valid_mga_plist(data, build, model):
            self.remove_mga_data(udid)
            return False
        return True
    
    def get_mga_data(self, udid: str) -> dict:
        mga_settings = self.get_mga_prefs()
        if not mga_settings.contains(udid):
            return None
        data = mga_settings.value(udid)
        return plistlib.loads(data)
    
    def is_valid_mga_plist(self, plist: dict, device_build: str, device_model: str) -> bool:
        return ("CacheVersion" in plist
                and "0+nc/Udy4WNG8S+Q7a/s1A" in plist["CacheExtra"]
                and plist["CacheVersion"] == device_build
                and plist["CacheExtra"]["0+nc/Udy4WNG8S+Q7a/s1A"] == device_model)