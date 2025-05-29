#!/usr/bin/python3
"""creating a class that prints a sorted list"""


class MyList(list):
    """sorting a list when elements are appended
    remains to be fixed"""
    def print_sorted(self):
        """this function prints a list in an ascending sorted fashion"""
        print(sorted(self))
