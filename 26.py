import json

f = open("payments.json")
data = json.load(f)
employees = {}

for emp in data["employees"]:
    emp_salary = [i for i in emp["monthly_payment"].values()]
    avg = sum(emp_salary) / len(emp_salary)
    employees.setdefault(emp["name"], avg)

most_payed = max(employees.items())
print(most_payed)
