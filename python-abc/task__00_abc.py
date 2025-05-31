#!/usr/bin/python3
"""creating an abstract class that other subclasses will inherit from"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """A class that contains an abstract method called sound"""
    @abstractmethod
    def sound(self):
        pass


"""creating two concrete classes called Dog and Cat"""


class Dog(Animal):
    def sound(self):
        return (f"Bark")


class Cat(Animal):
    def sound(self):
        return (f"Meow")
