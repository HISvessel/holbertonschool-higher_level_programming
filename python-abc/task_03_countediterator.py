#!/usr/bin/python3
"""This module contains a class called CountedIterator
in which, given a list, we iterate through every item in that list
without using loops; instead, we utilize the dunder methods
__iter__ and __next__"""


class CountedIterator:
    """a non empty class which has the following arguments:
    init, which takes a list, for which we will iterate through
    iter, which is the iterable builtin that returns self
    count, which holds a count of all the iterable objects
    next, which moves to the next iterable object"""

    def __init__(self, iterator):
        self.iterator = iter(iterator)
        self.count = 0

    def __iter__(self):
        """function that stores the iterable data inside of itself"""

        return self

    def __next__(self):
        """Returns an item, which is the iterable of all the list"""

        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Returns a count of all items obtained through ter and next"""

        return self.count
