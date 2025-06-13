"""tutoring session to better understand conversion from Python
to JSON and from JSON to Python"""
import json

#EX 1: this takes a JSON string and converts it to a Python object
#json_string = '{"name": "Alice", "age": 30, "is_student": true}'
#data = json.loads(json_string)
#print("EX1:")
#print(data) #output : {"name": "Alice", "age": 30, "is_student" = true}, confirming that it is an object
#print(type(data)) #output: <class 'dict'>, confirming that it was converted to a dictionary

#Ex 2: this function loads a JSON form a file
#with open("person.json", "w") as file:
#    data = json.load(file)


"""part 2: working a custom file with serialization"""
#username = input("Welcome to this file creator. First, we'll start off wth your name:")
#fave_number = input("Now, let me have your favorite number, if you have one:")
#print("Great! Now saving....")
#print()
#user_info = {"name": username,"favorite_number": fave_number}
#user_file = "new_file.json"
#with open(user_file, "w", encoding="utf-8") as file:
#    json.dump(user_info, file)
#    print("Data saved successfully!")

"""part 3: serializing into JSON file"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def person_dict(obj):
        return obj.__dict__
    
    def to_dict(self):
        return {"name": self.name, "age": self.age, "__person__": True}
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['age'])

    #serializing to a JSON String
person1 = Person("Kevin", 28)
json_str = json.dumps(person1.person_dict())
print(json_str)
print()    
    #deserializing from a JSON String
person2 = Person("Alice", 25)
data = person2.to_dict()
print("Serialized dictionary:", data) #prints a dictionary

person3 = Person.from_dict(data)
print("Deserialized object:", person3.name, person3.age) #prints the string serialized back to the object

#custom encoder function
#this encodes into an dictionary from an object
def encode_person(obj):
    if isinstance(obj, Person):
        return obj.to_dict()
    raise TypeError(f"object of the type {obj.__class__.__name__} is not JSON serializable")

#custom decoder function
#this converts from dictionary to object
def decode_person(dct):
    if "__person__" in dct:
        return Person.from_dict(dct)
    return dct
person = Person("Bob", 45)

#serialize into a JSON string
json_string = json.dumps(person, default=encode_person)
print("This was converted to JSON string:", json_string)

#deserialize from the string into an Object
p2 = json.loads(json_string, object_hook=decode_person)
print(f"Deserialized object: name({p2.name}), age({p2.age})")

# chalenge mode
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def book_to_dict(self):
        return {"title": self.title, "author": self.author, "year": self.year, "__book__": True}

    @classmethod
    def dict_to_book(cls, data):
        return cls(data["title"], data["author"], data["year"])

def encode_book(book):
    if isinstance(book, Book):
        return book.book_to_dict()
    raise TypeError(f"This object cannot be encoded")

def decode_book(dict):
    if "__book__" in dict:
        return Book.dict_to_book(dict)
    return dict

book_1 = Book("Lord of the Rings", "JRR Tolkien", 1954)
data = book_1.book_to_dict()
json_book_string = json.dumps(data, default=encode_book)
print("This was converted to a dict", json_book_string)

book2 = json.loads(json_book_string, object_hook=decode_book)
print(f"We have obtained your book. It is {book2.title}, written by {book2.author}, in the year of {book2.year}")

