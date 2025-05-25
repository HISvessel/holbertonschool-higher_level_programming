#!/usr/bin/python3
"""a new class called rectangle which will be given some data"""


class Rectangle:
    """we will now create data for length and width"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """We will now use getter and setter method
    to obtain public instance of height and store as private"""
    @property
    def height(self):
        return self.__height

    @height.setter
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
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """A new function that returns the area of the class Rectangle"""
    def area(self):
        """returning the height times the width"""
        return self.__height * self.__width

    """A new function that returns the perimeter of the class"""
    def perimeter(self):
        """returning two times the area"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    """This new function serves to represent our rectangle
    as a readable object"""
    def __str__(self):
        """this function returns the value stored as an object and
        the __str__ prints it"""
        if self.__width == 0 or self.__height == 0:
            return ""
        lines = []
        for _ in range(self.__height):
            lines.append("#" * self.__width)
        return "\n".join(lines)

    """This function prints a string representation of our rectangle"""
    def __repr__(self):
        """this function returns a string with the
        initialization of our object of class Rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"
