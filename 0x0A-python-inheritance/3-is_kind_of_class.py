#!/usr/bin/python3
""" Module contains is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance or inherited instance of a class
    """
    return isinstance(obj, a_class)
