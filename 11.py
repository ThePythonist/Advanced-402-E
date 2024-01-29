from random import randint


def account_number():
    id = ""
    for i in range(10):
        id += str(randint(0, 9))
    return id


class BankAccount:
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type
        self.balance = 0

    def withdraw(self,value):
        if self.balance > 0 :
            if self.balance >= value:
                self.balance -= value
                print(f"Withdraw : {value}")
                print(f"Current account balance : {self.balance}")
            else :
                print("Your balance is not enough")


    def deposit(self,value):
        self.balance += value
        print(f"Deposit : {value}")
        print(f"Current account balance : {self.balance}")


    def info(self):
        print(self.id)
        print(self.name)
        print(self.type)

customer1 = BankAccount(account_number(),"Hamid Afshar","Seporde Kootah Modat")
customer2 = BankAccount(account_number(),"Kiarash Mohseni","Seporde Boland Modat")

customer1.deposit(50000)
customer1.withdraw(55000)
