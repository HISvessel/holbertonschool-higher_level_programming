#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        a_list = my_list
        a_list[idx] = element
    return a_list
