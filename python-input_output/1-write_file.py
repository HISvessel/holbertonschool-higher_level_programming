#!/usr/bin/python3
"""this module contains the function called write_file
which uses the input and output methods to create and write
to a test file"""


def write_file(filename="", text=""):
    """this function writes text on a file. if the file does
    not exist, it creates it by mean of the 'w' write argument"""
    with open(filename, "w") as f:
        f.write(text)
