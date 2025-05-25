#!/usr/bin/python3
from sys import argv
from calculator_1 import add

if __name__ == "__main__":
    total = 0
    for arg in argv[1:]:
        total = add(total, int(arg))
    print("{}".format(total))