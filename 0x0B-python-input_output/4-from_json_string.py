#!/usr/bin/python3
""" Module contains from_json_string function
"""
import json


def from_json_string(my_str):
    """ function that returns an object (Python data structure)
    """
    return json.loads(my_str)
