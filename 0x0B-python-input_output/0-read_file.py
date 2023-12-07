#!/usr/bin/python3
""" Module contains read_file function
"""


def read_file(filename=""):
    """ function that reads a text file
    """
    with open(filename, encoding="utf-8") as fname:
        print(fname.read())
