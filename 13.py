class Calculator:
    def __init__(self, n1, op, n2):
        self.num1 = n1
        self.operator = op
        self.num2 = n2

    def add(self):
        print(self.num1 + self.num2)

    def substract(self):
        print(self.num1 - self.num2)

    def multiply(self):
        print(self.num1 * self.num2)

    def divide(self):
        print(self.num1 / self.num2)


def main():
    number1 = int(input("Enter number : "))
    operator = input("Enter operator : ")
    number2 = int(input("Enter number : "))

    result = Calculator(number1, operator, number2)

    print("Result : ", end="")

    if operator == "+":
        result.add()
    elif operator == "-":
        result.substract()
    elif operator == "*":
        result.multiply()
    elif operator == "/":
        result.divide()
    else:
        print("Invalid Operator. Try again")
        main()


main()
