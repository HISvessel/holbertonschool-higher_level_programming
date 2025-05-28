#!/usr/bin/python3
"""this module works with the inheritance of our previously created module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """thi new subclass inherits from the basegeometry superclass"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)
