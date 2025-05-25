#!/usr/bin/python3
from sys import argv
from calculator_1 import add

if __name__ == "__main__":
    total = (add(total, int(arg)) for arg in argv[1:])
    print("{}".format(total))