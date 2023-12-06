#!/usr/bin/python3
""" Module contains append_write function
"""


def append_write(filename="", text=""):
    """ function that appends a string at the end of a text file
    """
    with open(filename, "a", encoding="utf-8") as fname:
        return fname.write(text)
