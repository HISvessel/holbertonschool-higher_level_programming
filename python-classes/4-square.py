#!/usr/bin/python3
"""this is a new class with a few more modifications"""


class Square:
    """this new class has a few private instances
    but also public instances of the class,
      so that we may use and retrieve private data"""
    def __init__(self, size=0):
        """this function creates a private instance of a class"""

        self.__size = size

    @property
    def size(self):
        """this function is created for the purpose of storing the
        private size data for a public usage of that attribute"""
        return self.__size

    """this function uses the getter and setter method to
    make an private instance be declared public"""
    @size.setter
    def size(self, value):
        """raises errors if not the correct type
        of if value is less than 0"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        return value

    """this returns the area of a square's size"""
    def area(self):
        return self.__size ** 2
