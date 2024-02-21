import json

f = open("states.json")
data = json.load(f)

for i in data["states"]:
    if i["name"].lower() in ["alaska", "florida", "new york"]:
        print(i)
