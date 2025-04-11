import xml.etree.ElementTree as tree

tree.register_namespace('', "http://www.apple.com/CoreAnimation/1.0")

def set_xml_value(file: str, id: str, key: str, val: any, use_ca_id: bool = False):
    xml = tree.parse(file)
    root = xml.getroot()

    # convert bool to integer
    value = val
    if isinstance(val, bool):
        value = int(val)
    # convert value to string
    if not isinstance(val, str):
        value = str(value)

    # set all values with the nugget id passed by param
    if use_ca_id:
        idKey = "id"
    else:
        idKey = "nuggetId"
    for to_change in root.findall(f".//*[@{idKey}='{id}']"):
        to_change.set(key, value)
    if use_ca_id:
        # also look for target id
        for to_change in root.findall(f".//*[@targetId='{id}']"):
            to_change.set(key, value)

    # write back to file
    xml.write(file, encoding="UTF-8", xml_declaration=True)

def remove_from_root(root, search):
    for parent in root.findall(search + "/.."):
        for prop in parent.findall(search):
            parent.remove(prop)

def delete_xml_value(file: str, id: str, use_ca_id: bool = False):
    xml = tree.parse(file)
    root = xml.getroot()

    # delete all elements with the nugget id passed by param
    if use_ca_id:
        idKey = "id"
    else:
        idKey = "nuggetId"
    remove_from_root(root, search=f".//*[@{idKey}='{id}']")
    if use_ca_id:
        # also remove the target ids
        remove_from_root(root, search=f".//*[@targetId='{id}']")
    
    # write back to file
    xml.write(file, encoding="UTF-8", xml_declaration=True)