#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(my_list):
        idx = i
        print("{:d}".format(idx))

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at {:d} is {}".format(idx, element_at(my_list, idx)))