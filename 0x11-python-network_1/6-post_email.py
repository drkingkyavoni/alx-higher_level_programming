#!/usr/bin/python3
"""Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as
a parameter"""

from requests import post
from sys import argv

if __name__ == "__main__":
    mail = {"email": argv[2]}
    response = post(argv[1], data=mail)
    print("{}".format(response.text))
