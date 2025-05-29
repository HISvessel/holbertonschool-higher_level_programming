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



#first_child = Person("Emma", 2, "nina").introduction()
#second_child = Person("Luna", 1, "baby").introduction()
#print("We have a total of {} children".format(Person.child))
"""^^^this utilizes the set instance of children inside of the class,"
it cannot be changed outside of class, it is already set"""
#introduction()
#print(first_child)
#print(second_child)
"""^^^^^^
this ouputs None, for some reason 
"""

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def description(self):
        print(f"the book{self.title} has {self.pages} pages")
    
    @classmethod
    def from_string(cls):
        pass
    
    @staticmethod
    def is_lengthy(pages):
        if pages > 500:
            return True

class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
    
    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value):
        self.__celsius = value
        
    @property #understanding the flexibility of getter setter
    def fahrenheit(self): #this stores a value in F
        return self.__celsius * 9/5 + 32
    
    fahrenheit.setter
    def fahrenheit(self, input): #this makes the stored F value turn to C
        self.__celsius = (input - 32) * 5/9

class Distance:
    def __init__(self, distance):
        self.meters = distance
    
    @property
    def meters(self):
            return self._meters

    @meters.setter
    def meters(self, input):
        self._meters = input
    
    @property
    def kilometers(self):
        return self._meters / 1000

    @kilometers.setter
    def kilometers(self, input):
        self._meters = input * 1000
   
    @property
    def feet(self):
        return self._meters * 3.2808

    @feet.setter
    def feet(self, input):
        self._meters = input * 0.3048

    @classmethod
    def from_feet(cls, in_feet):
        return cls(in_feet * 0.3048)

d1 = Distance(1000)
print("Test 1")
print("Meters:", d1.meters)
print("Kilometers:", d1.kilometers)
print("Feet:", d1.feet)

d2 = Distance(0)
d2.kilometers = 2
print("\nTest 2")
print("Meters:", d2.meters)          
print("Kilometers:", d2.kilometers)  
print("Feet:", d2.feet)              

class Currency:
    def __init__(self, usd):
        self.usd = usd
    @property
    def usd(self):
        return self.__usd
    
    @usd.setter
    def usd(self, money):
        self.__usd = money
    @property
    def eur(self):
        return self.__usd * 0.85
    
    @eur.setter
    def eur(self, money):
        self.__usd = money / 0.85
    
    @property
    def jpy(self):
        return self.__usd * 110
    
    @jpy.setter
    def jpy(self, money):
        self.__usd = money / 110
    
    @classmethod
    def from_jpy(cls, jpy):
        return cls(jpy / 110)
    
    @classmethod
    def from_eur(cls, eur):
        return cls(eur / 0.85)
print()
print("Test 1: Currency")
cash = Currency(100)  # 100 USD
print(cash.eur)       # ~85.0 EUR
cash.jpy = 11000      # Sets the value in JPY
print(cash.usd)       # Should be 100.0
new_cash = Currency.from_eur(85)
print(new_cash.usd)   # Should be 100.0
