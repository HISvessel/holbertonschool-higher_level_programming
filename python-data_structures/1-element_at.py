#!/usr/bin/python3
def element_at(my_list, idx):
    i = my_list[idx]
    return (i if idx in range(i) else None)
