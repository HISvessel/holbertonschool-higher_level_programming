#!/usr/bin/python3
"""rhis module introduces us to the concept of 
serialization and deserialization, shows us the differnece"""


import json

"""serializing is the process by which we convert a Python
object as a JSON string"""

def serialize_and_save_to_file(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        """
        Serialize and ssave data to the specified file

        args: 
            data - a pyton dictionary with a data
            filename: a filename that is taken as a string
        """
        
        json.dump(data, filename)

"""this function deserializes an existing string inside of a file
by loading it as an object, which is to recreate the object as it was"""

def load_and_deserialize(filename):
    """
    deserializing the string inside of a JSON file as an object

    args:
        filename: a string of the filename from which the
        data is extracted and deserialized
    """

    with open(filename, encoding='uts-8') as file:
        return json.load(file)