#!/usr/bin/python3
"""this module contains a function that writes
data to an existing file by appending it to the EoF"""


def append_write(filename="", text=""):
    """this function writes to a file in the
    aooend selector: by aoending the text to the file
    we can add it to the end of an already existing file"""
    
    with open(filename, 'a') as f:
        return f.write(text)
