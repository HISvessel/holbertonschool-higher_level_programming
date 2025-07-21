from task_00_intro import generate_invitations
import os

template_file = os.path.exists()

if template_file:
    print("File exists; proceeding to install.")
with open('template.txt', 'r', encoding="utf-8") as file:
    template_content = file.read() #this is for opening and reading the file

    attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

generate_invitations(template_content, attendees)
