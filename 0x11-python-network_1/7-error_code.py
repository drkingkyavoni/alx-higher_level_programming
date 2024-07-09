#!/usr/bin/python3
"""Python script that takes in a URL,
sends a request to the URL and
displays the body of the response."""

from sys import argv

from requests import get

if __name__ == "__main__":
    result = get(argv[1])
    if result.status_code < 400:
        print(result.text)
    else:
        print("Error code: {}".format(result.status_code))
