#!/usr/bin/python3
"""this module contains a function that opens a file and reads it"""


def read_file(filename=""):
    """this function opens a document and reads it
    we use this method to safely close and secure documents
    after the read builtin has been executed"""

    with open(filename) as f:
        print(f.read(), end="")
