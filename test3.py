# from xml.etree.ElementTree import tostring
from xml.etree.ElementTree import tostring
import xml.etree.cElementTree as ET
import json

json_file = 'data.json'

with open(json_file) as json_file:
    data = json.load(json_file)

# print(data)


root = ET.Element('root')

result = ET.SubElement(root, json_file)

for i in [data]:
    ET.SubElement(result, 'subject').text = str(i)

    # print(str(i))

tree = ET.Element(result)
# tree.write('students.xml')
print(tostring(tree))
