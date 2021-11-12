
import json as j
from xml.etree.ElementTree import Element, tostring


def dict_to_xml(tag, d):

    elem = Element(tag)
    for key, val in d.items():

        child = Element(key)
        child.text = str(val)
        elem.append(child)

    return elem


# Driver Program
s = {'name': 'geeksforgeeks',
     'city': 'noida', 'stock': 920}

# e stores the element instance
e = dict_to_xml('company', s)


# print(e)

# converting into a byte string
print(tostring(e))

e.set('_id', '1000')

print(tostring(e))
