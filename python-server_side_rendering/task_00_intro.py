import flask
from jinja2 import PackageLoader, Environment, select_autoescape, FileSystemLoader


"""this module contains a function that generates a personalized
invitation file from a template with placeholders and a list
of objects.

For this function to work, we must find a way to read the file
and render the content of our list of dictionaries and create
for separaaate individuals. the idea is to learn about rendering
personal information to separate users in order to better understand
the concept of server side perks, which include individual and personalized
experience that caters to users based on their info

in order to do this, we use Jinja to generate an HTML that will be
filles with three separate invitations, all under one template that
will then be filled with unique information for each separate
invitation."""

def generate_invitations(template, attendees):
    try:

        """this function generates a personalized invitation
        based off of a template. This function assumes a file is
        already open, so what we do is iterate through our dictionary
        of attendees and replace the placeholder values with the
        dictionary values by their keys. I can assume we will read
        through the HTML templace and append the value to the respective
        element(take the name in the dictionary and replacing it with
        the value stored). Everytime, we generate individual
        files for each member of the dictionary."""
        env = Environment(
            loader=FileSystemLoader("templates")
        )
        #this variable gets the template and renders it at the same time
        text = env.get_template("template.txt").render()

        print(text) #testing to see if the text prints

    except (Exception, TypeError):
        if template is not type(str):
            raise TypeError("Our template must be a string")
    
        if len(template) == 0:
            raise Exception("The template must not be empty")

        if attendees is not type(list):
            raise TypeError("You must incluse a list of dictionaries")
        
        if len(attendees) == 0:
            raise Exception("List must not be empty")