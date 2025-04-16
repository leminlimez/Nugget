import xml.etree.ElementTree as tree

tree.register_namespace('', "http://www.apple.com/CoreAnimation/1.0")

def parse_equation(eq: str, val: str):
    eqns = eq.split(',')
    value = [val]
    if ' ' in val:
        # convert to array
        value = val.split(' ')
    # map the value to floats
    value = list(map(lambda x: float(x), value))
    keys = ['x', 'y', 'z', 'a']
    results = []
    mapped = dict(zip(keys, value))
    for eqn in eqns:
        results.append(str(eval(eqn, {}, mapped)))
    # map back to string
    return ' '.join(results)

def set_xml_value(file: str, id: str, key: str, val: any, use_ca_id: bool = False):
    set_xml_values(file=file, id=id, keys=[key], values=[val], use_ca_id=use_ca_id)

def set_xml_values(file: str, id: str, keys: list[str], values: list[any], use_ca_id: bool = False):
    xml = tree.parse(file)
    root = xml.getroot()

    # convert bool to integer
    for i in range(len(values)):
        if isinstance(values[i], bool):
            values[i] = int(values[i])
        # convert value to string
        if not isinstance(values[i], str):
            values[i] = str(values[i])

    # set all values with the nugget id passed by param
    if use_ca_id:
        idKey = "id"
    else:
        idKey = "nuggetId"
    for to_change in root.findall(f".//*[@{idKey}='{id}']"):
        eqn = to_change.get("nuggetOffset")
        # TODO: Allow offsets for more than just the first value
        for i in range(len(keys)):
            offsetVal = values[i]
            if i == 0 and eqn != None:
                offsetVal = parse_equation(eqn, offsetVal)
            to_change.set(keys[i], offsetVal)
    if use_ca_id:
        # also look for target id
        for to_change in root.findall(f".//*[@targetId='{id}']"):
            for i in range(len(keys)):
                to_change.set(keys[i], values[i])

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