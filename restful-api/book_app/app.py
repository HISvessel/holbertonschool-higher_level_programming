from flask import Flask
from books import books_bp

"""this module contains a simple test web aplication for creating our own list of books as inventory.
The application is run with the Flask module and data is stored in a JSON file. This acts as a mockup of our big
project coming up as our Hbnb is starting to integrate coding and class creation, therefore, the idea is to grease the groove
and begin with something simple but effective that can be developed with no knowledge of front end developing.
Our app is meant to work with curl and postman inputs taken from our terminal, and the following functions are enabled:
a greeting in our APIs root, a page redirection for showing the books we have stored, and functions for the addition, update and deleting of
books, plus an extra option for resetting our db(used as a resource for debugging and troubleshooting).

The file has now been changed to allow for more controlled
inputs and fixes from their respective methods. Routes have been
added to call the specific book routes from the routes.py
file contained inside of the book module.
"""

app = Flask(__name__)
app.register_blueprint(books_bp) #calls the book route


@app.route('/') #the root route
def home(): #function to display homescreen with a single message
    return "Welcome to the book API. What book would you like to find?"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

