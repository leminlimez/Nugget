import zipfile
import os

from .tweak_classes import Tweak
from restore.restore import FileToRestore

class PasscodeThemeTweak(Tweak):
    def __init__(self):
        super().__init__(key=None, value=None)

    def import_passthm(self, path: str) -> bool:
        # returns whether or not it was valid
        if path == None or path == "":
            self.value = None
            self.enabled = False
            return False
        final_path = None
        success = False
        try:
            with zipfile.ZipFile(path, mode="r") as archive:
                if any('TelephonyUI-' in folder for folder in archive.namelist()):
                    final_path = path
                    success = True
        except:
            pass
        finally:
            self.value = final_path
            self.enabled = success
            return success

    def apply_tweak(self) -> list[FileToRestore]:
        if not self.enabled or self.value == None or self.value == "":
            return None
        files: list[FileToRestore] = []
        with zipfile.ZipFile(self.value, mode='r') as archive:
            for path in archive.namelist():
                if path.startswith('.') or "__MACOSX" in path:
                    continue
                if path.lower().endswith('.png'):
                    # add it (assume it is a passcode key for now)
                    files.append(FileToRestore(
                        contents=archive.read(path),
                        restore_path=f"/var/mobile/Library/Caches/TelephonyUI-10/{os.path.basename(path)}",
                        domain=None
                    ))
        return files