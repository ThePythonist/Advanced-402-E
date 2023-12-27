import random


def irancell():
    pn = ""
    code = random.choice(["0930", "0939", "0938", "0936"])

    for i in range(7):
        pn += str(random.randint(0, 9))
        # pn += str(random.choice(range(0,10)))

    phonenumber = f"{code}{pn}"
    return phonenumber


def hamrahaval():
    pn = ""
    code = random.choice(["0993", "0912", "0990", "0919"])

    for i in range(7):
        pn += str(random.randint(0, 9))

    phonenumber = f"{code}{pn}"
    return phonenumber


def rightell():
    pn = ""
    code = random.choice(["0921", "0922", "0923"])

    for i in range(7):
        pn += str(random.randint(0, 9))

    phonenumber = f"{code}{pn}"
    return phonenumber


if __name__ == "__main__":
    print(irancell())
    print(hamrahaval())
    print(rightell())
