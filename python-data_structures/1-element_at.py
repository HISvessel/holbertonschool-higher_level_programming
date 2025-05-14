#!/usr/bin/python3
def element_at(my_list, idx):
    num = my_list[idx] if idx < len(my_list) else None
    return (num if idx > 0 else None)
