import json

f = open("payments.json")
data = json.load(f)

for i in data["employees"]:
    print(f'{i["name"]} : {i["job_title"]}')
