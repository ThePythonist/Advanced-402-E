import xml.etree.ElementTree as ET

xml_data = open("flights.xml").read()
root = ET.fromstring(xml_data)

flights = root.findall("flight")
for i in flights:
    origin = i.find('origin').text
    print(origin)
