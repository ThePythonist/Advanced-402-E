import json

f = open("states.json")
data = json.load(f)
names = []
# print(len(data["states"]))

for i in data["states"]:
    names.append(i["name"])

# with open("state_names.json", "w") as f2:
#     json.dump(names, f2, indent=2)

f2 = open("state_names.json", "w")
json.dump(names, f2, indent=2)
