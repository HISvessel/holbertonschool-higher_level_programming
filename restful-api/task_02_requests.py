#!/usr/bin/python3
import requests
import csv


"""this module contains two functions: fetch and print
and the function fetch and save, which prints and saves posts
respectively."""


def fetch_and_print_posts():
    """this function fetch all post requests from thr JSON
    PLaceholder and prints their titles"""

    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post["title"])


def fetch_and_save_posts():
    """this function obtains from JSONPlaceholder
    all post requests and saves its contents
    as a comma separated value file"""

    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        data = response.json()
        post_list = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in data
        ]
        with open("posts.csv", "w", newline="") as csv_file:
            fieldname = ["id", "title", "body"]
            info = csv.DictWriter(csv_file, fieldnames=fieldname)
            info.writeheader()
            info.writerows(post_list)
