#!/usr/bin/python3
def uppercase(str):
    newstring = ""
    for letter in str:
        if ord(letter) in range(97, 123):
            newstring += chr(ord(letter) - 32)
        else:
            newstring += letter
    print({}.format(newstring))
