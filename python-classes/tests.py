#!/usr/bin/python3
class Person:
    """
     this starts a new class
     along with a greeting 

     Update: greeting to the newly initialized user
    """
    def introduction(self):
        print("Hola,", self.name,"tu tienes", self.age,"anos")
        print("Eres una", self.job)

    """ 
    this fucntion initializes a new person of the class Person
    as well as creating instances for that person age, name and motto
    """
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job


first_child = Person("Emma", 2, "nina").introduction()
second_child = Person("Luna", 1, "baby").introduction()
#introduction()
print(first_child)
print(second_child)
"""^^^^^^
this ouputs None, for some reason 
"""
