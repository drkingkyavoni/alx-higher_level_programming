#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request"""

from requests import post
from sys import argv

if __name__ == "__main__":
    data = {"q": "" if len(argv) == 1 else argv[1]}

    try:
        result = post("http://0.0.0.0:5000/search_user", data=data)

        if d := result.json():
            print("[{}] {}".format(d.get("id"), d.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
