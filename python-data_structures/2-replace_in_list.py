#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list


my_list = [1, 2, 3, 4, 5, 6]
print(my_list)
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)
print(new_list)
