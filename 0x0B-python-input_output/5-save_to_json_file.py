#!/usr/bin/python3
""" Module contains save_to_json_file function.
"""
import json


def save_to_json_file(my_obj, filename):
    """ function that writes an object to a text file, using a JSON
    """
    with open(filename, 'w', encoding="utf-8") as fname:
        json.dump(my_obj, fname)
