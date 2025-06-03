#!/usr/bin/python3
"""this module contains a function that stores
the data as given by the JSON interpretation of 
a string and converts it into a Python object"""
from json import loads


def from_json_string(my_str):
    """a function that utilizes the loads builtin
    from the JSON module and converts it into a python
    object. This can be used to better manipulate control 
    and output objects that will then be passed into JSON"""

    return loads(my_str)
