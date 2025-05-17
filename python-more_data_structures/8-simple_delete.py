#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key for key in a_dictionary)
    return a_dictionary
