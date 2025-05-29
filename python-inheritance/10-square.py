#!/usr/bin/python3
"""this module contains a class that is created by
inheriting attributes from other parent classes"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a new subclass called Square that inhertis from
    rectangle, which itself inherits from BaseGeometry
    To obtain attributes and rewrite them to make attributes with
    custom properties, such as making 1 attribute of square(size)
    perform as two atributes of rectangle(height, width)
    we use super() method to override"""

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        self.__str__()
        self.integer_validator("size", size)
        self.integer_validator("size", size)
        self.area()
