#!/usr/bin/python3
"""this is the creation of a class called Square"""


class Square:
    """ a new Square was created"""
    def __init__(self, size=0):
        """this function creates a private instance called size
        is size is not an integer, a TyeError is raised"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

    """this is the function of an area"""
    def area(self):
        """this functon creates a public instance called area
        where area is the current area of the Square size"""
        return self.__size ** 2
