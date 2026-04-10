import plistlib

from PySide6.QtCore import QSettings
from src.restore.bookrestore import BookRestoreFileTransferMethod, BookRestoreApplyMethod
from src.tweaks.posterboard.pb_config_item import PBConfigItem

class PreferenceManager:
    def __init__(self, settings: QSettings):
        self.settings = settings
        self.apply_over_wifi = False
        self.auto_reboot = True
        self.allow_risky_tweaks = False
        self.show_all_spoofable_models = False
        self.disable_tendies_limit = False
        self.auto_refresh_posterboard = True
        self.restore_truststore = False
        self.bookrestore_apply_mode = BookRestoreApplyMethod.AFC
        self.bookrestore_transfer_mode = BookRestoreFileTransferMethod.LocalHost
        self.skip_setup = True
        self.supervised = False
        self.organization_name = ""

    # Mobile Gestalt Saving
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
    
    # PosterBoard Configuration Database Saving
    def get_pbconfigs_prefs() -> QSettings:
        return QSettings("Nugget", "PB Configs")
    
    def save_pbconfig_file(filepath: str, udid: str):
        pbc_settings = PreferenceManager.get_pbconfigs_prefs()
        with open(filepath, 'rb') as pbdb_file:
            pbc_settings.setValue(udid, pbdb_file.read())
    def save_pbconfig_ids(ids: list[PBConfigItem], udid: str):
        pbc_settings = PreferenceManager.get_pbconfigs_prefs()
        # convert it to serializable data
        serialized_ids: list[dict] = []
        for id in ids:
            serialized_ids.append(id.to_dict())
        pbc_settings.setValue(f'{udid}-ids', serialized_ids)

    def remove_pbconfig_data(udid: str):
        pbc_settings = PreferenceManager.get_pbconfigs_prefs()
        if pbc_settings.contains(udid):
            pbc_settings.remove(udid)
            PreferenceManager.remove_pbconfig_ids(udid)
    def remove_pbconfig_ids(udid: str):
        pbc_settings = PreferenceManager.get_pbconfigs_prefs()
        ids_key = f'{udid}-ids'
        if pbc_settings.contains(ids_key):
            pbc_settings.remove(ids_key)

    def has_pbconfig_data(udid: str) -> bool:
        return PreferenceManager.get_pbconfigs_prefs().contains(udid)
    def has_pbconfig_ids(udid: str) -> bool:
        return PreferenceManager.get_pbconfigs_prefs().contains(f'{udid}-ids')
    
    def get_pbconfig_data(udid: str):
        pbc_settings = PreferenceManager.get_pbconfigs_prefs()
        if not pbc_settings.contains(udid):
            return None
        return pbc_settings.value(udid)
    def get_pbconfig_ids(udid: str) -> list[PBConfigItem]:
        pbc_settings = PreferenceManager.get_pbconfigs_prefs()
        ids_key = f'{udid}-ids'
        if not pbc_settings.contains(ids_key):
            return None
        serialized_ids = pbc_settings.value(ids_key)
        ids: list[PBConfigItem] = []
        for id in serialized_ids:
            ids.append(PBConfigItem.from_dict(id))
        return ids