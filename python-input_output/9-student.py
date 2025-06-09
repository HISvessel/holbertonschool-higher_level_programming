#!/usr/bin/python3
"""this module contains the class of a student that will recieve various
methods to initialize the class and to represent as an item to translate
into a JSON string"""


class Student:
    """we initialize methods to adhere to the class
    and we have a public method that returns the data
    into a JSON file by use of the dict dunder method
    which prints a dictionary string"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
