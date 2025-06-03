#!/usr/bin/python3

"""This module contains a series of casses, programs and tests
to better understand the implementation of UML in the concept
of Object Oriented Programming. We will see the implementations of
the following UML relationships:
1) Association
2) Generalization
3) Aggregation
4) Composition
5) Realization
6) Dependancy"""

"""Case -> Association
here we see the relationship between two separate unrelated
and non inherited classes that have a relation with each other: 
a student which learns from a teacher and has other
teachers stored in a list of its own attribute, and a teacher, who teaches students that a re contained within a 
list of students inside of its own attributes"""
class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

class Student:
    def __init__(self, name):
        self.name = name
        self.teachers = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)




"""Case-> Generalization
here we see the type of relationship that incorporates inheritance
for more direct association between classes: a class of Dog and Cat
that incorproates from a class called animal. As a result
of inheritance, thw ==e cat and dog take name from the animal class
and a speak method called '-_def speak_' that is inherited and passed
with an overwritten method of speaking that is signature to the dog and the cat"""

"""And so, what is the generalization method saying? that
the class dog has an 'is an' relationship with the Animal class.
The same happens for the cat class, which is an animal from class Animal
Generalization, then, begins when inheritance is performed"""

"""this example would also show an example of a realization:
where, as working with inheritance and overriding, the Cat and Dog
classes inherit the speak method from the Animal class and pass their own message"""
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


"""Case-> Aggregation

back to the concept of inheritance, here we see how a department
is given an employee by name and position. This type of relation
shows how a Employee adds to the aggregation of the add_employee
method inside the Department class"""

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

