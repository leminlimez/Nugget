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

def windows_join_path(og_path: str, join: str):
    if os.name == 'nt':
        final_path = og_path
        for dir in join.split('/'):
            final_path = os.path.join(final_path, dir)
        return final_path
    else:
        return os.path.join(og_path, join)