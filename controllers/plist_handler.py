import plistlib

def recursive_set(plist: dict, key: str, value: any):
    new_plist: dict = plist
    for k, v in plist.items():
        if k == key:
            new_plist[k] = value
        elif isinstance(v, dict):
            new_plist[k] = recursive_set(v, key, value)
    return new_plist

def set_plist_value(file: str, key: str, value: any):
    with open(file, 'rb') as in_fp:
        plist = plistlib.load(in_fp)
    new_plist = recursive_set(plist, key, value)
    return plistlib.dumps(new_plist)