#!/usr/bin/python3
"""this module works with the inheritance of our previously created module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this new subclass inherits from the basegeometry superclass"""
    def __init__(self, width, height):
        """privatizing both of our instance attributes
        inheriting the class function integer validator"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """updating the inherited area function
        so that it now returns the area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """returning a string containing the contents of the class"""
        return (f"[Rectangle] {self.__width}/{self.__height}")
