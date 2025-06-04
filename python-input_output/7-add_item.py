#!/usr/bin/python3
"""this module has a function called add_item
it imports the functions save to json an load from json so that a command
line argument is recieved, parsed and converted as objects, which
are then brought unto a JSON doc by the use of save to JSON"""

import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


"""the module operates as per the following sequence:
a filename called add_file.json is retrieved of its json contents
if the ile does not exist, it is created with load from json
we operate the script so that command arguments are given, retrived as objects
and simultaneously written u=into the json files as json objects

if the document is not properly opened and closed, even if the code executes
successfully, undefined behaviour will begin to perform. I guess that explains
as to why the filw would not properly write objects added to it"""


filename = "add_file.json"
try:
    argument_list = load_from_json_file(filename)
except Exception:
    argument_list = []
argument_list.extend(sys.argv[1:])
save_to_json_file(argument_list, filename)
