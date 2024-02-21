import json

f = open("states.json")
data = json.load(f)

# print(len(data["states"]))

for i in data["states"]:
    print(i["name"])
