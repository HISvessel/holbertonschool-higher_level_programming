#!/usr/bin/python3
"""this functon creates a new class called Square"""


class Square:
    def __init__(self, size=0):
        """
        two errors are raised for this function:
        ValueError if size is less than 0
        TypeError if size does not recieve an integer
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
