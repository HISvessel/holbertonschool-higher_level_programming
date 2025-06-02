#!/usr/bin/python3
"""this module demonstrates the capacity of
polymorphism and reusability
we have two initial classes, each with a single methos
SwimMixin with its swim method
FlyMixin with its fly method
and finally
a Dragon, that inherits from fly and swim; also with a signature"""


class SwimMixin:
    """this class has a method that prints a single message"""

    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """this second class has a method that prints a single message"""

    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """this class has a single unique method called roar
    it is also inheriting the capacity to swim and fly
    from the FLyMixin and SwimMixin classes.

    Here, we see polymorphism in action"""

    def roar(self):
        print("The dragon roars!")
