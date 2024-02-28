import xmltodict

xml_data = open("flights.xml").read()
data = xmltodict.parse(xml_data)

root = data["flights"]
flights = root["flight"]
paris_flights = []

for i in flights:
    if i["destination"].lower() == "paris":
        paris_flights.append(i)

for i in paris_flights:
    print(i)
