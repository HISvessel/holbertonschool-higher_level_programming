#!/usr/bin/python3
"""this module contains the function inherits from,
which returns true when the inheritance of a class is found"""


def inherits_from(obj, a_class):
    """returning true for all subclasses but not its own class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
