#!/usr/bin/python3
""" Module contains class_to_json function
"""


def class_to_json(obj):
    """ function that returns the dictionary for a class obj
    """
    return {k: v for k, v in obj.__dict__.items()
            if not callable(v) and not k.startswith("__")}
