#!/usr/bin/python3
""" Module contains load_from_json_file
"""
import json


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file”
    """
    with open(filename, 'r') as fname:
        return json.load(fname)
