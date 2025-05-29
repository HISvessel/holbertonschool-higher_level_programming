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
    we use super() method to override. The area method
    is now implemented"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    """obtaining the correct string to be stored with the class name"""
    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
