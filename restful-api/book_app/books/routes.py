from flask import Blueprint, jsonify, request
import json, os
from .utils import load_from_json, save_to_json
from config import RESET_TOKEN


books_bp = Blueprint("books", __name__)
books = []


@books_bp.route("/books", methods=['GET']) # book redirection, the place where our primary data is displayed
def get_book():
    return jsonify(load_from_json()), 200

@books_bp.route("/books", methods=['POST'])
def add_book(): # method to add a book to the display in our /book redirect
    new_book = request.get_json()
    books = load_from_json()
    books.append(new_book)
    save_to_json(books)

    return jsonify(new_book), 201

@books_bp.route("/books/batch", methods=['POST'])
def batch_add_books(): # method to add numerous books
    many_books = request.get_json()

    if not isinstance(many_books, list):
        return jsonify({"Error": "bad request: expected a list of books"}), 404
    try:
        existing_books = load_from_json()
        existing_books.extend(many_books)
        save_to_json(existing_books)

        return jsonify(existing_books), 201
    except FileNotFoundError:
        return jsonify({"Error": "File does not exist"}), 500

@books_bp.route("/books/<int:id>", methods= ['PUT'])
def update_book(id): # method to update an existing book inside of our JSON file; fetched by iD
    updated_data = request.get_json()
    try:
        books = load_from_json()
        book_found = False
        for book in books:
            if book["id"] == id:
                book.update(updated_data)
                book_found = True
                break

        if book_found == False:
            return jsonify({"Error": "book not found"}), 404
        save_to_json(books)
        return jsonify({"Success": "Book updated", "book": book}), 201

    except FileNotFoundError:
            return jsonify({"Error": "File not found"}), 500

@books_bp.route("/books/<int:id>", methods=["DELETE"]) #method to delete a single book. Fetching done by iD
def delete_book(id):
    try:
        books = load_from_json()
        book_found = False
        for book in books:
            if book["id"] == id:
                books.remove(book)
                book_found = True
                break
        if book_found == False:
            return jsonify({"Error": "book not found"}), 404

        save_to_json(books)
        return jsonify({"Message": "book deleted succesfully"}), 200

    except FileNotFoundError:
        return jsonify({"Error": "File not found"}), 500


@books_bp.route("/reset", methods= ["POST"])
#resetting method, it loads the file and overrides content by dumping an empty list

def reset_books():
    if request.headers.get("X-Reset-Token") is not RESET_TOKEN:
        return jsonify({"error": "unauthorized access"}), 403
    seed_data = []
    save_to_json(seed_data)
    return jsonify({"Message":"Books database reset successfully"}), 200
