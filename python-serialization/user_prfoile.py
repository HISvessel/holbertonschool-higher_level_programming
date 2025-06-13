#!/usr/bin/python3
import sys
import shelve
import json


"""this script allows for a database program done through shelve module
to store command line arguments stored as profiles. Script is to be
run as an executable in a command line. The program takes arguments
to create, update, list, export and delete profiles into shelve DB and JSON files.

Arguments: takes one of the following first arguments
1) add= adds a user
2) list= lists all users on database
3) update= updates existing profile
4) export= exports profiles to JSON
5) delete= deletes the user

kwargs:
1) add takes three additional inputs: a name, the age and an email
2) update takes as next input an existing user and then rewrites the data
by taking three additional arguments as per the add option's sequence
3) delete takes a single argument of the existing profile, else no deletion is performed
list and export take no further arguments"""

DB_name = "user_profile.db"
def add_user(name, age, email):
    with shelve.open(DB_name) as db:
        db[name] = {"name": name, "age": age, "email": email}
        print(f"User {name} has been added.")
    
def list_users():
    with shelve.open(DB_name) as db:
        print("Users in data base:")
        for key in db:
            print(f"-{key}': {db[key]}")

def export_users():
    with shelve.open(DB_name) as db:
        data = dict(db)
        with open("database_file.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Data exported.")

def update_user(profile, new_name, new_age, new_email):
    with shelve.open(DB_name, writeback=True) as db: #opens database to check if exists
        if profile in db: #checks for the existence of the profile
            db[profile]["name"] = new_name
            db[profile]["age"] = new_age
            db[profile]["email"]= new_email
            print("Profile updated")
        else:
            print(f"No record found for {profile}")

def delete_user(profile):
    with shelve.open(DB_name, writeback=True) as db:
        if profile in db:
            del(db[profile])
            print(f"{profile} has been deleted. Goodbye, {profile}")
        else:
            print(f"{profile} was not found on database")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please enter one of the following commands: add, update, list, export or delete")
        sys.exit(1)
    
    option = ["add", "update", "list", "export", "delete"]

    if sys.argv[1] == option[0] and len(sys.argv) == 5:
        _, _, name, age, email = sys.argv
        add_user(name, age, email)
    elif sys.argv[1] == option[1] and len(sys.argv) == 6:
        update_user(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif sys.argv[1] == option[2]:
        list_users()
    elif sys.argv[1] == option[3]:
        export_users()
    elif sys.argv[1] == option[4] and len(sys.argv) == 3:
        delete_user(sys.argv[2])
    else:
        print("Invalid usage")