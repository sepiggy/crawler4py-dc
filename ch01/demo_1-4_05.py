# usr/bin/env python3
# -*- coding: utf-8 -*-

# Demos for lxml document aka http://lxml.de/4.1/lxmldoc-4.1.1.pdf

# 1. The Element class
from lxml import etree

# 1.1 Create an element
root = etree.Element("root")

# 1.2 Get the XML tag name
print(root.tag)

# 1.3 Create child elements
root.append(etree.Element("child1"))

# Another method to create child elements [recommended]
child2 = etree.SubElement(root, "child2")
child3 = etree.SubElement(root, "child3")

# 1.4 Serialise the XML tree
print(etree.tostring(root, pretty_print=True))

# 2. Elements are lists
# elements mimic the behaviour of normal Python lists as closely as possilbe
child = root[0]
print(child.tag)

print(len(root))

print(root.index(root[1]))
print(root.index(root[2]))
children = list(root)
print(children)
for child in children:
    print(child.tag)
for child in root:
    print(child.tag)

root.insert(0, etree.Element("child0"))
for child in root:
    print(child.tag)

start = root[:1]
print(type(root))
print(type(start))
for child in start:
    print(child.tag)

end = root[-1:]
for child in end:
    print(child.tag)

print(start[0].tag)
print(end[0].tag)

# test if it's some kind of Element
print(etree.iselement(root))

if len(root):
    print("The root element has children")
