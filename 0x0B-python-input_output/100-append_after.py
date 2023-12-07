#!/usr/bin/python3
""" Module contains append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends new_string after search_string in filename."""
    with open(filename, mode='r', encoding="utf-8") as fname:
        lines = fname.readlines()

    with open(filename, mode='w', encoding="utf-8") as fname:
        for line in lines:
            fname.write(line)
            if line.__contains__(search_string):
                fname.write(new_string)
