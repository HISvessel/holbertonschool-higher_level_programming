#!/usr/bin/python3
from sys import argv
counter = len(argv) - 1
if counter == 0:
    print("{} arguments".format(counter), end=".\n")
elif counter == 1:
    print("{} argument:\n{}: {}".format(counter, counter, argv[counter]))
else:
    print("{} arguments".format(counter), end=":\n")
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
