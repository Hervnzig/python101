from xml.etree.ElementTree import Element, tostring


def dict_to_xml(tag, d):

    elem = Element(tag)
    for key, val in d.items():
        # create an Element
        # class object
        child = Element(key)
        child.text = str(val)
        elem.append(child)

    return elem


json_file = 'data.json'


for i in json_file:
    e = dict_to_xml('company', json_file)
    # print(tostring(e))
    # print(i)


e = dict_to_xml('company', json_file)
print(tostring(e))
