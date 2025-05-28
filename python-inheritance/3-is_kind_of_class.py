#!/usr/bin/python3
"""This module has the function is_kind_of_class,
that returns true for an instance of the object or the type"""


def is_kind_of_class(obj, a_class):
    """the function returns true for instance of the object"""
    return True if isinstance(obj, a_class) else False
