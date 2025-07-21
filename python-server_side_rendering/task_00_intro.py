import os


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

    if not isinstance(template, str):
            print(f"Template must be a string, got {type(template)}")
            return

    if template.strip == "":
        print(f"Template is empty, no output file generated.")
        return

    if not isinstance(attendees, list):
        print("Attendees a list of dictionaries")
        return
        
    if not attendees:
        print("No data provided, no output files generated")
        return

        #this variable gets the template(defined in the main function)
    for i, attendee in enumerate(attendees):
        at_name = attendee.get("name") or 'N/A'
        at_title = attendee.get("event_title") or 'N/A'
        at_date = attendee.get("event_date") or 'N/A'
        at_location = attendee.get("event_location") or 'N/A'
        new_template = (template
                        .replace('{name}', at_name)
                        .replace('{event_title}', at_title)
                        .replace('{event_date}', at_date)
                        .replace('{event_location}', at_location)
                        )
        out_doc = f"output_{i}.txt"
    
    try:
        with open(out_doc, 'w') as file:
             file.write(new_template)
    except OSError as e:
         print(f"[Error] Could not write {out_doc}: {e}")
