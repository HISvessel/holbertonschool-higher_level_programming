#!/usr/bin/python3
class Person:
    """
     this starts a new class
     along with a greeting 
    

     Update: greeting to the newly initialized user
    """
    child = 2
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

class   Student:
    school = "Holberton Coding School"
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


first_child = Person("Emma", 2, "nina").introduction()
second_child = Person("Luna", 1, "baby").introduction()
print("We have a total of {} children".format(Person.child))
"""^^^this utilizes the set instance of children inside of the class,"
it cannot be changed outside of class, it is already set"""
#introduction()
#print(first_child)
#print(second_child)
"""^^^^^^
this ouputs None, for some reason 
"""
Tommy = Student("Tommy", "A")
#Access class attribute
print(f"Tommy school: {Tommy.school}")