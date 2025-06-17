import json, os
from config import BOOK_FILE


def load_from_json():
    if os.path.exists(BOOK_FILE):
        with open(BOOK_FILE) as file:
            return json.load(file)
        return []

def save_to_json(books):
    with open(BOOK_FILE, "w") as file:
        json.dump(books, file, indent=4)
