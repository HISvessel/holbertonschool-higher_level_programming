#!/usr/bin/python3
"""This module contains the function called class to JSON"""

def class_to_json(obj):
    """this function returns a string representation of a dictionary
    that can be serialized into a JSON string"""

    return obj.__dict__
