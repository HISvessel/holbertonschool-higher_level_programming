#!/usr/bin/python3
"""this module creates three classes, one named FIsh
one named Bird and a third named FlyingFish; each with their
own methods and inheritance

the purpose is to understand the effect of multiple inheritance,
and how ordering classes upon inheritance can affect the class
when overriding similar methods"""


class Fish:
    """this class contains two methods:
    the swim method, which prints out the animals natural behaviour
    and the habitat method, which prints the animals habitat"""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """this class contains two methods:
    the fly method, which prints the animals behaviour
    and habitat, which shows us where the animal lives"""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("the bird lives in the sky")


class FlyingFish(Fish, Bird):
    """this final class contains inheritance of our previous classes
    and contain a combination of the three methods:
    it adopts the fly method from Bird
    the swim method from fish
    and the habitat method from both
    but, each with the quirk that makes the flying fish"""

    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
