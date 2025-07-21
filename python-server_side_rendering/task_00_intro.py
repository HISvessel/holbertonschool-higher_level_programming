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

        env = Environment(
            loader=FileSystemLoader("templates")
        )
        #this variable gets the template(defined in the main function)
        our_template = env.get_template(template)
        for attendee in attendees:
            at_name = attendee["name"]
            at_title = attendee["event_title"]
            at_date = attendee["event_date"]
            at_location = attendee["event_location"]
            new_template = our_template.render(name = at_name, event_title = at_title, 
                                               event_date = at_date, event_location = at_location)

    except (Exception, TypeError):
        if template is not type(str):
            raise TypeError("Our template must be a string")
    
        if len(template) == 0:
            raise Exception("The template must not be empty")

        if attendees is not type(list):
            raise TypeError("You must incluse a list of dictionaries")
        
        if len(attendees) == 0:
            raise Exception("List must not be empty")
