import plistlib

def recursive_set(plist: dict, key: str, value: any):
    new_plist: dict = plist
    for curr_key in plist.keys:
        if curr_key == key:
            new_plist[curr_key] = value
        elif isinstance(plist[curr_key], dict):
            new_plist[curr_key] = recursive_set(plist[key], key, value)
    return new_plist

def set_plist_value(file: str, key: str, value: any):
    with open(file, 'rb') as in_fp:
        plist = plistlib.load(in_fp)
    new_plist = recursive_set(plist, key, value)
    return plistlib.dumps(new_plist)