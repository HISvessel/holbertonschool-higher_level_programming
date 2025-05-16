#!/usr/bin/python3
def max_integer(my_list=[]):
    last = len(my_list) - 1
    my_list.sort()
    return my_list[last] if len(my_list) > 0 else None
