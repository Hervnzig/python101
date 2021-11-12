import xml.etree.ElementTree as Et


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


def print_result():

    data = [
        {
            "id": "001",
            "firstname": "Eric",
            "lastname": "Smith",
            "password": "Her#001ksc"
        },
        {
            "id": "002",
            "firstname": "Alice",
            "lastname": "Brown",
            "password": "H4rv#87902749#"
        },
        {
            "id": "003",
            "firstname": "Robert",
            "lastname": "Rock",
            "password": "ryAn978#582"
        }
    ]

    root = 'Students'
    tag = 'Student'

    xml_data = dict_to_xml(root, tag, data)
    print(Et.tostring(xml_data, encoding='unicode'))


print_result()
