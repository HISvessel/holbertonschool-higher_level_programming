#!/usr/bin/python3
"""creating a class that prints a sorted list"""


class MyList(list):
    def print_sorted(self):
        self.sort()
        print(self)
