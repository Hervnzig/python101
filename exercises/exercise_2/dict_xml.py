# Python program to convert

import xml.etree.ElementTree as Et
import json


# Opening JSON file and loading the data
# into the variable data
with open('exercises/exercise_2/data.json') as json_file:
    data = json.load(json_file)

student_data = data


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

    data = student_data

    root = 'Students'
    tag = 'Student'

    xml_data = dict_to_xml(root, tag, data)
    print(Et.tostring(xml_data, encoding='unicode'))


print_result()
