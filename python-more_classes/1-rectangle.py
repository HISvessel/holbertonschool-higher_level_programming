#!/usr/bin/python3
"""a new class called rectangle which will be given some data"""


class Rectangle:
    """we will now create data for length and width"""
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width

    """We will now use getter and setter method
    to obtain public instance of height and store as private"""
    @property
    def height(self):
        return self.__height

    height.setter

    def height(self, value):

        """This function stores the attribute with a value

        Arguments: a value to be taken when creating a new object

        Conditions:
        TypeError if the value obtained is not an integer
        ValueError if the value obtained is less than zero"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """We will now use the getter and setter
    method to make private instance of width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        """We will set the value of width

        Arguments: a value given to a width attribute

        Conditions:
        TypeError if the value obtained is not an integer
        ValueError if the value obtained is less than 0"""
        if type(value) is not int:
            raise TypeError("width must be an intger")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
