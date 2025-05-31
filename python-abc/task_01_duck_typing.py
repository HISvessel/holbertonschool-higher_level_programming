#!/us/bin/python3
"""This module contains
an abstract class called shape
two concrete classes called rectangle and circle
and a function called shape_info"""


from abc import ABC, abstractmethod
from math import pi


"""this is our abstract class, from which
our other classes will be created.
It passes two empty abstract methods that will be
implemented into our other classes"""


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


"""We create a new class called circle
the abstract methods will now be implemented
as well as its own attribute called radius"""


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return pi * (self.radius * 2)


"""A new class called rectangle is also created
the abstract methods are also implemented, as well
as its own attributes called height and width"""


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


"""The final piece of the module: the shape_info function
which prints the information contained within the abstract methods
of their respective class, showing that both classes
despite being different instances of the class shape,
contain the methods as described"""


def shape_info(obj):
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")

