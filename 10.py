import math


class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        print(self.length * self.width)

    def perimeter(self):
        print((self.length + self.width) * 2)


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        print(self.radius * self.radius * math.pi)

    def perimeter(self):
        print(self.radius * 2 * math.pi)


def area(shape):
    shape.area()


def perimeter(shape):
    shape.perimeter()


rec = Rectangle(5, 6)
crc = Circle(3)

area(rec)
perimeter(rec)
