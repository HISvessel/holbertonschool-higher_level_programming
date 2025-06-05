#!/usr/bin/python3
"""this module contains the function called write_file
which uses the input and output methods to create and write
to a test file"""


def write_file(filename="", text=""):
    """this function writes text on a file. if the file does
    not exist, it creates it by mean of the 'w' write argument

    since the requirement of the task is to see that the write
    builtin is writing the data in the document, the best way to
    test it is by returning the value given at the end of the
    function as stored data"""

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
