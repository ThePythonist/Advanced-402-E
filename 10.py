class BankAccount:
    def __init__(self, name, type, code):
        self.name = name
        self.accountype = type
        self.nationalcode = code
        self.balance = 0

    def show_balance(self):
        print("Current Account Balanace :", self.balance)

    def withdraw(self, value):
        if self.balance >= 0:
            if not self.balance < value:
                self.balance -= value
                print("-", value)
            else:
                print("Account Balance is not Enough")

        self.show_balance()

    def deposit(self, value):
        self.balance += value
        print("+", value)

        self.show_balance()


customer1 = BankAccount("ahora", "seporde kootah modat", "0130067141")
customer2 = BankAccount("akbar", "seporde boland modat", "0070062331")

customer1.deposit(50000)
customer1.withdraw(60000)
