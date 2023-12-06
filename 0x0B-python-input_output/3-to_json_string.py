#!/usr/bin/python3
""" Module contains to_json_string function
"""
import json


def to_json_string(my_obj):
    """ function that returns the JSON representation of an object
    """
    return json.dumps(my_obj)
