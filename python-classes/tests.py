#!/usr/bin/python3
class Person:
    """
     this starts a new class
     along with a greeting 

     Update: greeting to the newly initialized user
    """
    def introduction(self):
        print("Hello,", self.name,"you are", self.age,"years old.")
        print("You work as a", self.job)

    """ 
    this fucntion initializes a new person of the class Person
    as well as creating instances for that person age, name and motto
    """
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job


Person("Calvin", 23, "croupier").introduction()
#introduction()
print(Person)
"""^^^^^^
this ouputs None, for some reason 
"""
