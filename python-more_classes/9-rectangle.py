#!/usr/bin/python3
"""a new class called rectangle which will be given some data"""


class Rectangle:
    """a new instance that keeps count of the classes created
    further updating with a new print_symbol attrbute"""

    number_of_instances = 0
    print_symbol = "#"

    """we will now create data for length and width"""
    def __init__(self, height=0, width=0):
        Rectangle.number_of_instances += 1
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
        symbol = str(self.print_symbol)
        lines = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    """This function prints a string representation of our rectangle"""
    def __repr__(self):
        """this function returns a string with the
        initialization of our object of class Rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """This function decrements the instances
        upon deletion and prints a farewell message
        when an object of Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    """creating a new statimethod function to find the bigger rectangle"""
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """this returns the bigger of the two rectangles
        if the inputs are not a rectangle class, then a typeerror
        is raised"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        elif rect_1.area() >= rect_2.area():
            return rect_1

    @classmethod
    def square(cls, size=0):
        """utilizing class methods to create a new shape
        this shape has the inheritance of rectangle, but is a square
        to adapt it, it returns the same rectangle class but
        size being the height and the with so that size takes both
        values but is the same unit
        because of inheritance, it also creates the area
        and the perimeter based on size"""
        return cls(size, size)
