import zipfile
import os
import io
from PIL import Image

from .tweak_classes import Tweak
from restore.restore import FileToRestore

def pil_image_to_png_data(pil_image: Image.Image):
    """
    Converts a PIL Image object to raw PNG image data (bytes).

    Args:
        pil_image: A PIL.Image.Image object.

    Returns:
        bytes: The raw PNG image data.
    """
    buffered = io.BytesIO()
    pil_image.save(buffered, format="PNG")
    return buffered.getvalue()

class PasscodeThemeTweak(Tweak):
    def __init__(self):
        super().__init__(key=None, value=None)
        self.language_code = 'en'
        self.big_keys = True
        self.current_size = 0 # 0 = nothing, 1 = small, 2 = big

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
                    if any(path.endswith('_small') for path in archive.namelist()):
                        self.current_size = 1
                    elif any(path.endswith('_big') for path in archive.namelist()):
                        self.current_size = 2
                    else:
                        self.current_size = 0
        except:
            pass
        finally:
            self.value = final_path
            self.enabled = success
            return success
        
    def get_name_for_file(self, path: str) -> str:
        # format: [language code]-[number]-[letters]--white.png
        components = os.path.basename(path).split('-')
        return f'{self.language_code}-{components[1]}-{components[2]}--white.png'

    def apply_tweak(self) -> list[FileToRestore]:
        if not self.enabled or self.value == None or self.value == "":
            return None
        files: list[FileToRestore] = []
        size_multiplier = 1
        if self.current_size == 1 and self.big_keys:
            # convert small to big
            size_multiplier = 287/202
        elif self.current_size == 2 and not self.big_keys:
            # convert big to small
            size_multiplier = 202/287
        with zipfile.ZipFile(self.value, mode='r') as archive:
            for path in archive.namelist():
                if path.startswith('.') or "__MACOSX" in path:
                    continue
                if path.lower().endswith('.png'):
                    # add it (assume it is a passcode key for now)
                    if size_multiplier == 1:
                        img_data = archive.read(path)
                    else:
                        # resize the img
                        img = Image.open(archive.open(path))
                        width, height = img.size
                        new_width = int(width * size_multiplier)
                        new_height = int(height * size_multiplier)
                        img = img.resize((new_width, new_height))
                        img_data = pil_image_to_png_data(img)
                        img.close()
                    files.append(FileToRestore(
                        contents=img_data,
                        restore_path=f"/var/mobile/Library/Caches/TelephonyUI-10/{self.get_name_for_file(path)}",
                        domain=None
                    ))
                    del img_data
        return files