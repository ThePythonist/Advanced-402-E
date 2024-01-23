import time


class Car:
    def __init__(self, color, gb, hp, a): # Khod be khod ejra mishe
        self.color = color
        self.gearbox = gb
        self.horsepower = hp
        self.engine_mode = False
        self.rpm = 0
        self.acceleration = a

    def start_engine(self):
        self.engine_mode = True

    def horn(self):
        print("Horn")

    def accelerate(self, value):
        if self.engine_mode == True:
            for i in range(value):
                time.sleep(self.acceleration)
                self.rpm += 1000
                print(self.rpm)

    def stop(self):
        print("Decreasing")

    def info(self):
        print(self.color)
        print(self.gearbox)
        print(self.horsepower)


# Creating Instance or Object : Shey
persia = Car("White", "Manual", 153, 2)
dena = Car("Black", "Automatic", 160, 3)
samand = Car("White", "Manual", 140, 4)

# Calling Methods
samand.start_engine()
samand.accelerate(4)
