#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

from requests import get

if __name__ == "__main__":
    response = get("https://alx-intranet.hbtn.io/status")
    print("{}".format("Body response:"))
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
