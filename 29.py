import xmltodict

xml_data = open("payments.xml").read()
data = xmltodict.parse(xml_data)

root = data["employees"]
employees = root["employee"]
python_salaries = []

for i in employees:
    if "python" in i["job_title"].lower():
        for j in i["monthly_payment"].values():
            python_salaries.append(int(j))

avg = sum(python_salaries) / len(python_salaries)
print(avg)
