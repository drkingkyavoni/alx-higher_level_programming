#!/usr/bin/python3
""" Module contains add_attribute function
"""


def add_attribute(obj, name, value):
    """ function that adds a new attribute to
    an object if it’s possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
