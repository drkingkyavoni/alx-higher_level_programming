#!/usr/bin/python3
"""script that takes in a URL and an email,
sends a POST request to the passed URL with
the email as a parameter"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    mail = urlencode({"email": argv[2]}).encode("ascii")
    # print(mail)
    req = Request(argv[1], mail)
    with urlopen(req) as response:
        print(response.read().decode("utf-8"))
