#!/usr/bin/python3
"""this module contains a function called save_to_json_file
which takes a json object and converts it a to readable text
that can be written into a Python text file"""
from json import dumps


def save_to_json_file(my_obj, filename):
    """this function converts the object to string
    by the use of dumps and then is written into a
    file given by the parameter filename"""

    with open(filename, 'w') as f:
        f.write(dumps(my_obj))
