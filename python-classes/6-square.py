#!/usr/bin/python3
"""this is a new class with a few more modifications"""


class Square:
    """this new class has a few private instances
    but also public instances of the class,
      so that we may use and retrieve private data"""
    def __init__(self, size=0, position=(0, 0)):
        """this function creates a private instance of a class
        a new instance is given by the name of position"""

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """this obtains the private instance called size"""
        return self.__size

    """this new private instance position is now to be obtained"""
    @property
    def position(self):
        """this returns the privae instance position"""
        return self.__position

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

    @position.setter
    def position(self, value):
        self.__position = value
        if not isinstance(value, tuple()):
            raise TypeError("position must be a tuple of 2 positive integers")
        return value

    """this returns the area of a square's size"""
    def area(self):
        return self.__size ** 2

    """this new function prints a set of
    astersik up to the size of our square"""
    def my_print(self):
        """this should print out a new line
        if size equals to 0, otherwise prints a square"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print("_" * self.position[0] + "#" * self.size)
