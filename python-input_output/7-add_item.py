#!/usr/bin/python3
"""this module has a function called add_item"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_file.json"
argument_list = load_from_json_file(filename)
argument_list = []
argument_list.extend(argv[1:])
save_to_json_file(argument_list, filename)
