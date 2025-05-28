#!/usr/bin/python3
"""This module defines is_same_class,
a function that returns true for the objext instance"""


def is_same_class(obj, a_class):
    """returns true for a correct instance of object"""
    return True if a_class == type(obj) else False
