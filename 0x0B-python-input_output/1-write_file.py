#!/usr/bin/python3
""" Module contains write_file function
"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file
    """
    with open(filename, mode='w', encoding='utf-8') as fname:
        return fname.write(text)
