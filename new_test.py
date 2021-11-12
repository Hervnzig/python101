import xml.etree.ElementTree as Et

dict_data = 'data.json'


def dict_to_xml(root, tag, dict_data):
    root_element = Et.Element(root)
    for info in dict_data:
        elements = ''
        for key, value in info.items():
            if key == 'id':
                elements = Et.Element(tag, attrib={key: value})
            else:
                child = Et.Element(key)
                child.text = str(value)
                elements.append(child)

        root_element.append(elements)
        print(root_element)
    return root_element
