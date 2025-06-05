#!/usr/bin/python3
"""this module contains the function load from json file
which loads an object contained within a JSON file"""
import json


def load_from_json_file(filename):

    """the function is designed to read from a JSON
    file and convert the returned string into an
    object
    
    changing particular output"""

    with open(filename, encoding="utf-8") as file:
        return json.load(file)
