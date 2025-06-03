#!/usr/bin/python3
"""this module contains a function that converts
a python object into its json representation"""


from json import dumps


def to_json_string(my_obj):
    """this function takes an object and converts it
    to its json representation by use of the imported function
    dumps"""

    return dumps(my_obj)
