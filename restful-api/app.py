from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
BOOK_FILE = "book_list.json"
books = [] # an array of books to be uploaded
@app.route('/') #the root route
def home(): #function to display homescreen
    return "Welcome to the book API"

@app.route('/books', methods=['GET']) # book redirection, the place where our primary data is stored
def get_book():
    return jsonify(books)

@app.route("/books", methods=['POST'])
def add_book(): # method to add a book to the display in our /book redirect
    new_book = request.get_json()
    books = load_book_from_json()
    books.append(new_book)
    save_book_to_json(books)

    return jsonify(new_book), 201

@app.route('/books', methods=['GET'])
def load_book_from_json():
    if os.path.exists(BOOK_FILE):
        with open(BOOK_FILE) as file:
            return json.load(file)
    return []

@app.route("/books/batch", methods=['POST'])
def save_book_to_json(books):
    with open(BOOK_FILE, "w") as file:
        json.dump(books, file, indent=4)
    
@app.route("", methods=['POST'])
def batch_add_books():
    many_books = request.get_json(books)
    if many_books is not list:
        return "400 Error (nad request)"
    existing_books = load_book_from_json()
    existing_books.extend(many_books)
    save_book_to_json(existing_books)

    return jsonify(existing_books), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)