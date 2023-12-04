#!/usr/bin/python3
""" Module contains is_same_class function
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is an instance of the class
    """
    return type(obj) is a_class
