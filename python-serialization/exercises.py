import pickle
import marshal
import shelve
import json


"""lets begin with the system module for the Python exclusive
builtin module called pickle. This will allow us to serialize more python specific
data type like tuples, sets, classes, etc. Anything beyond the scope of what something
like JSON can convert. Important things to note: Pickle is python exclusive, so there
is not cross language, pickle converts to binary file, not human readable data; and
regarding the safety of pickle conversion: they tend to be risky"""

#lets see an example with loading pickle module
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
book1 = Book("1984", "George Orwell")
 #serialize to binary file
with open("book.pkl", "wb") as file:
    pickle.dump(book1, file)
    print(f"Successfully saved your book: {book1.title} by {book1.author}")

#deserialize from the pkl file
with open("book.pkl", "rb") as file:
    loaded_book = pickle.load(file)
    print(f"Successfully loaded your stored book: {loaded_book.title} by {loaded_book.author}")
print()
#now an example of marshal
data = {"x": 42, "y": [1, 2, 3]}
with open("data.marshal", "wb") as file:
    marshal.dump(data, file)
    print(f"Data saved with marshal dump: {data}")
#readback
with open("data.marshal", "rb") as file:
    loaded_data = marshal.load(file)
    print(f"Data loaded with marshal load: {loaded_data}")


#challenge 1
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

person1 = Person("Kevin", "kevin_sanchez@hotmail.com")
with open("userinfo.pkl", "wb") as file:
    pickle.dump(person1, file)
    print("User successfully saved")

with open("userinfo.pkl", "rb") as file:
    loaded_person = pickle.load(file)
    print(f"User data loaded: name -> {loaded_person.name}; email-> {loaded_person.email}")

phonebook = {
    "Kevin": 9392060528,
    "Egmar": 124568790,
    "Joseph": 9876543210,
    "Kamila": 1563578294,
    "pages": [1, 2, 3, 4]}

with open("phonebook.marshal", "wb") as file:
    marshal.dump(phonebook, file)

with open("phonebook.marshal", "rb") as file:
    new_phonebook = marshal.load(file)
    print(f"Successfully loaded phonebook: {new_phonebook}")


#introduction into shelve
with shelve.open("myshelve.db") as db:
    db["username"] = "Kevin"
    db["email"] = "kevin@example.com"

#now its time to retrieve it
with shelve.open("myshelve.db") as db:
    print(db["username"], db["email"])

#this might not work, but its worth a shot
file = "a_file.json"
with shelve.open("myshelve.db") as db:
    dct = dict(db)
    json_string = json.dumps(dct)

new = json.loads(json_string)
print(new)

#shelve based challenge
