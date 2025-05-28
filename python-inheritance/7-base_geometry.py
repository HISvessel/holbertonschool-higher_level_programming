#!/usr/bin/python3
"""A module that creates a class of name BaseGeometry"""


class BaseGeometry:
    """this non empty class contains a public instance attribute"""
    def area(self):
        """passng a public class with an implementation exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.name = value
