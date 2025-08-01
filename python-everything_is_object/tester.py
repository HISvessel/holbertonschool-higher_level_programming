import copy
i = 0
j = 0

for i in range(1, 5):
    for j in range(i):
        print(i)

print("-" * 20)

class Toy:
    def __init__(self, color, name):
        self.color = color
        self.name = name


class Kid:
    def __init__(self, name, toys=None):
        self.name = name
        self.toys = toys if toys is not None else []
    
    def add_toy(self, toy):
        return self.toys.append(toy)
    

Alice = Kid("Alice")
Bob = Kid("Bob")

Toy_1 = Toy("Red","Ball")
Toy_2 = Toy("Blue", "Wagon")

Alice.add_toy(Toy_1)
Bob.add_toy(Toy_2)
toy_for_Alice = Alice.toys

print(Alice.toys == toy_for_Alice)
print(Alice.toys is toy_for_Alice)
print(Alice.toys)
toy_for_Alice = ["White", "Pike"]
print(toy_for_Alice)
print(Alice.toys)
print(Bob.toys)

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    wheels = 4

    def honk(self):
        return ("HONK")

car1 = Car("Toyota", "Corolla", 1985)
truck = Car("Hino", "Truck", 1997)
trucker_wheels = Car.wheels
trucker_wheels = 6
print(Car.wheels)
print(trucker_wheels)
print(trucker_wheels is Car.wheels)

def copy_integer(x):
    return x

a = 10
b = copy_integer(a)
print(a)
print(b)
print(id(a))
print(id(b))
b = 11
print(a)

class spaceship:
    def __init__(self, name, crew):
        self.name = name
        self.crew = crew
    
    def _str_(self):
        return (f"{self.name} contains the following members: {', '.join(self.crew)}")

original = spaceship("Voyager", ["Alice", "Bob"])
original_crew = original.crew
original_name = original.name
clone = copy.copy(original)

cloned_crew = clone.crew
cloned_crew.append("Joyce")
cloned_name = clone.name
cloned_name = "Voyager 2"
print("Original team: ", original_crew)
print("Modified team: ", cloned_crew)
print("This is our first tripulation ship's name:", original_name)
print("This is our copied tripulation ship's name:", cloned_name)