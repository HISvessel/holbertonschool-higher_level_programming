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

    """setting a public instance of private size"""
    @size.setter
    def size(self, value):
        """raises value errors and type errors
        if size is not a positive number or an integer"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """this new private instance position is now to be obtained"""
    @property
    def position(self):
        """this returns the privae instance position"""
        return self.__position

    """this function uses the getter and setter method to
    make a position instance public"""
    @position.setter
    def position(self, value):
        check = 0
        while 1:
            if type(value) is not tuple or len(value) != 2:
                check += 1
                break
            if value[0] < 0 or value[1] < 0:
                check += 1
                break
            if type(value[0]) is not int or type(value[1]) is not int:
                check += 1
                break
        if check is 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
