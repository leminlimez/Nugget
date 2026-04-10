from os import path, makedirs, remove, listdir
import shutil
import sqlite3
import time
from PySide6.QtCore import QStandardPaths
from typing import Optional

from src.exceptions.nugget_exception import NuggetException
from src.controllers.files_handler import get_bundle_files
from src.devicemanagement.preference_manager import PreferenceManager
from .pb_config_item import PBConfigItem

DB_FILE_NAME = "PBFPosterExtensionDataStoreSQLiteDatabase.sqlite3"

class PBConfigManager:
    def __init__(self):
        self.staging = False
        self.saved_items: list[PBConfigItem] = []
        self.staged_items: list[PBConfigItem] = []
        self.database = None
        self.staged_database = None
        self.config_files: list[str] = []
        self.config_files_folder: Optional[str] = None

    def start_staging(self):
        self.staged_items.clear()
        if self.staged_database != None and path.exists(self.staged_database):
            try:
                remove(self.staged_database)
            except Exception:
                pass
        self.staged_database = None
        self.staging = True
    def cleanup(self):
        self.staged_items.clear()
        self.staging = False
    def add_config(self, uuid: str, ext: str):
        new_conf = PBConfigItem(uuid, ext)
        self.staged_items.append(new_conf)

    def cache_config_files(self):
        # cache the files for config conversion
        if len(self.config_files) == 0:
            self.config_files_folder = get_bundle_files("files/posterboard/configconversion")
            for item in listdir(self.config_files_folder):
                self.config_files.append(path.basename(item))
    def file_needs_updated(self, filename: str) -> bool:
        if not filename.endswith(".plist"):
            return False
        self.cache_config_files()
        if filename in self.config_files:
            return True
        return False
    
    def save_staged_ids(self, udid: str):
        if self.staging:
            PreferenceManager.save_pbconfig_ids(self.staged_items, udid)
            self.saved_items = self.staged_items
            self.cleanup()
    
    def update_for_saved_database(self, udid: str) -> bool:
        db_data = PreferenceManager.get_pbconfig_data(udid)
        if db_data is None:
            self.database = None
            self.staged_database = None
            return False
        app_data_path = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        if not path.exists(app_data_path):
            makedirs(app_data_path)
        dbpath = path.join(app_data_path, DB_FILE_NAME)
        with open(dbpath, 'wb') as outfile:
            outfile.write(db_data)
        del db_data
        # get the list of saved ids
        self.saved_items = PreferenceManager.get_pbconfig_ids(udid)
        return True

    def update_database_file(self, new_db: str, udid: str) -> bool:
        # make sure it has the tables: "poster", "posterAttributes", "posterRoleMembership", and "sqlite_sequence"
        # copy to a writeable path
        app_data_path = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        if not path.exists(app_data_path):
            makedirs(app_data_path)
        dbpath = path.join(app_data_path, DB_FILE_NAME)
        shutil.copyfile(new_db, dbpath)
        # make sure it has the tables
        db_connection = sqlite3.connect(dbpath)
        db_cursor = db_connection.cursor()
        tables_to_check = ["poster", "posterAttributes", "posterRoleMembership", "sqlite_sequence"]
        for tab in tables_to_check:
            db_cursor.execute(f"PRAGMA table_info({tab})")
            if db_cursor.fetchone() is None:
                db_connection.close()
                return False
        # check the saved ids
        final_saved_items: list[PBConfigItem] = []
        for item in self.saved_items:
            db_cursor.execute("SELECT FROM poster WHERE UUID = ?", (item.uuid,))
            sort_keys = db_cursor.fetchall()
            if sort_keys is None or len(sort_keys) == 0:
                final_saved_items.append(item)
        self.saved_items = final_saved_items
        # it is correct format, update database
        db_connection.close()
        self.database = dbpath
        if udid is not None:
            # save the database
            PreferenceManager.save_pbconfig_file(dbpath, udid)
        return True

    def update_sqlite(self) -> str:
        # use "sqlite_sequence" table "seq" entry for # of posters (add 1 to it for each wallpaper)
        # in "poster" table, add new entry:
        #   posterId = seq+1
        #   UUID = uuid of wallpaper
        #   providerId = extension string
        # in "posterAttributes" table, add new entry:
        #   posterUUID = uuid of wallpaper
        #   roleId = "PRPosterRoleLockScreen"
        #   attributeIdentifier = "PRPosterRoleAttributeTypeUsageMetadata"
        #   attributePayload = {"creationDate":1771975981.427938,"extensionAvailable":true,"attributeType":"PRPosterRoleAttributeTypeUsageMetadata"}
        # in "posterRoleMembership" table, add new entry:
        #   posterUUID = uuid of wallpaper
        #   roleId = "PRPosterRoleLockScreen"
        #   roleSortKey = # of highest sort key + 1
        if self.database is None:
            raise NuggetException("PosterBoard database file not selected!")
        # copy and open database file
        self.staged_database = path.join(QStandardPaths.writableLocation(QStandardPaths.AppDataLocation), f'STAGED-{DB_FILE_NAME}')
        shutil.copyfile(self.database, self.staged_database)
        conn = sqlite3.connect(self.staged_database)
        cursor = conn.cursor()
        # read number sequence
        cursor.execute("SELECT seq FROM sqlite_sequence WHERE name = ?", ("poster",))
        seq = cursor.fetchone()
        if seq is None:
            conn.close()
            raise NuggetException("Could not find \"seq\" in PosterBoard database!")
        seq = int(seq[0])
        # get the poster role sort key (falls back to seq)
        cursor.execute("SELECT roleSortKey FROM posterRoleMembership WHERE roleId = ?", ("PRPosterRoleLockScreen",))
        sort_keys = cursor.fetchall()
        if sort_keys is None or len(sort_keys) == 0:
            curr_role_sort_key = seq
        else:
            try:
                curr_role_sort_key = max(key[0] for key in sort_keys)
            except Exception:
                curr_role_sort_key = seq
        # remove the currently selected wallpaper
        cursor.execute("DELETE FROM posterAttributes WHERE roleId = ? AND attributeIdentifier = ? AND attributePayload = ?",
                       ("PRPosterRoleLockScreen", "SELECTED", 1))
        # combine the saved items
        self.staged_items = self.saved_items + self.staged_items
        for i in range(len(self.staged_items)):
            wallpaper = self.staged_items[i]
            seq += 1
            wallpaper.posterId = seq
            cursor.execute("INSERT INTO poster (posterId, UUID, providerId) VALUES (?, ?, ?)",
                           (wallpaper.posterId, wallpaper.uuid, wallpaper.extension))
            # TODO: Figure out when you need to add PRPosterRoleAmbient
            wallpaper_payload = ('{"creationDate":' + str(time.time())
                                 + ',"extensionAvailable":true,"attributeType":"PRPosterRoleAttributeTypeUsageMetadata","lastActivatedDate":'
                                 + str(time.time()+0.0001) + ',"lastSelectedDate":' + str(time.time()+0.00001) + '}')
            cursor.execute("INSERT INTO posterAttributes (posterUUID, roleId, attributeIdentifier, attributePayload) VALUES (?, ?, ?, ?)",
                        (wallpaper.uuid, "PRPosterRoleLockScreen", "SELECTED", 1))
            cursor.execute("INSERT INTO posterAttributes (posterUUID, roleId, attributeIdentifier, attributePayload) VALUES (?, ?, ?, ?)",
                           (wallpaper.uuid, "PRPosterRoleLockScreen", "PRPosterRoleAttributeTypeUsageMetadata",
                            wallpaper_payload))
            curr_role_sort_key += 1
            cursor.execute("INSERT INTO posterRoleMembership (posterUUID, roleId, roleSortKey) VALUES (?, ?, ?)",
                           (wallpaper.uuid, "PRPosterRoleLockScreen", curr_role_sort_key))
        cursor.execute("UPDATE sqlite_sequence SET seq = ? WHERE name = ?",
                       (seq, "poster"))
        conn.commit()
        conn.close()
        return self.staged_database