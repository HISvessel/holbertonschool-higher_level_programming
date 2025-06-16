#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status code:", response.status_code)
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post["title"])

def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        data = response.json()
        post_list = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in data
        ]
        with open("posts.csv", "w", newline="") as csv_file:
            fieldname = ["id", "title", "body"]
            info = csv.DictWriter(csv_file, fieldname=fieldname)
            info.writeheader()
            info.writerows(post_list)
            

fetch_and_print_posts()
fetch_and_save_posts