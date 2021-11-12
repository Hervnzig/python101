import xml.etree.cElementTree as e
import json as j

with open("data.json") as json_format_file:
    d = j.load(json_format_file)

# print(d)

r = e.Element(d)
# print("\n ===== test==== ", r, "\n")

# stud_list = e.SubElement(r, [])

for z in d:
    e.SubElement(r, "id").text = z["id"]
    e.SubElement(r, "firstname").text = z["firstname"]
    e.SubElement(r, "lastname").text = z["lastname"]
    e.SubElement(r, "password").text = z["password"]

    print("tessssssst \n", z)

a = e.Element(r)

a.write('xml_data.xml')

# print("\n Let's see ======", d)
