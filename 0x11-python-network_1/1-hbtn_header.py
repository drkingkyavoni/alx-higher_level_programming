#!/usr/bin/python3
"""Python script that takes in a URL,
sends a request to the URL and displays the
value of the X-Request-Id variable found
in the header of the response."""

from sys import argv
from urllib.request import Request, urlopen

if __name__ == "__main__":
    req = Request(argv[1])
    with urlopen(req) as response:
        result = response.getheader("X-Request-Id")
        print("{}".format(result))
