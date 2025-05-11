#!/usr/bin/python3
def islower(c):
    letter = ord(c)
    if letter in range(97, 123):
        True
        return letter
    else:
        False
        pass


print("3 is {}".format("lower" if islower("3") else "upper"))
print("a is {}".format("lower" if islower("c") else "upper"))
print("q is {}".format("lower" if islower("q") else "upper"))
print("Y is {}".format("lower" if islower("Y") else "upper"))
