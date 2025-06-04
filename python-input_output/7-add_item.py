#!/usr/bin/python3
"""this module has a function called add_item
it imports the functions save to json an load from json so that a command
line argument is recieved, parsed and converted as objects, which
are then brought unto a JSON doc by the use of save to JSON"""

from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


"""the module operates as per the following sequence:
a filename called add_file.json is retrieved of its json contents
if the ile does not exist, it is created with load from json
we operate the script so that command arguments are given, retrived as objects
and simultaneously written u=into the json files as json objects"""


filename = "add_file.json"
try:
    argument_list = load_from_json_file(filename)
except Exception:
    argument_list = []

argument_list.extend(argv[1:])
save_to_json_file(argument_list, filename)
