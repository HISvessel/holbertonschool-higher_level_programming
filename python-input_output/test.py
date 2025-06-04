"""tutoring session to better understand conversion from Python
to JSON and from JSON to Python"""
from json import load, loads, dump, dumps

#EX 1: this takes a JSON string and converts it to a Python object
json_string = '{"name": "Alice", "age": 30, "is_student": true}'
data = loads(json_string)
print("EX1:")
print(data) #output : {"name": "Alice", "age": 30, "is_student" = true}, confirming that it is an object
print(type(data)) #output: <class 'dict'>, confirming that it was converted to a dictionary

#Ex 2: this function loads a JSON form a file
with open("person.json", "w") as file:
    data = load(file)