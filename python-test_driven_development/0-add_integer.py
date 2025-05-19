#!/usr/bin/python3
"""
This module contains a function that returns two integers
"""


def add_integer(a, b=98):
    """
    This function returns the addition of a and b

    a = an integer or float parameter
    b = an integer or float parameter

    Return type: the addition of a and b

    Error types: raises TypeError if not an intgeer or a float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
