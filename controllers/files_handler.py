import sys
from os import path, getcwd

def get_bundle_files(name: str):
    try:
        return path.join(sys._MEIPASS, name)
    except:
        return path.join(getcwd(), name)