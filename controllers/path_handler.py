import os

def fix_windows_path(dos_path: str, encoding=None):
    if os.name == 'nt':
        if (not isinstance(dos_path, str) and encoding is not None): 
            dos_path = dos_path.decode(encoding)
        path = os.path.abspath(dos_path)
        if path.startswith(u"\\\\"):
            return u"\\\\?\\UNC\\" + path[2:]
        return u"\\\\?\\" + path
    else:
        return dos_path