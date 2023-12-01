#!/usr/bin/python3

"""
    Module contains add_integer function
    Returns: int
    Tested in tests/0-add_integer.txt
"""


def add_integer(a, b=98) -> int:
    """
        Function adds a and b
    """
    if not isinstance(a, (int, float)):
        raise Exception("a must be an integer")
    if not isinstance(b, (int, float)):
        raise Exception("b must be an integer")
    return int(a + b)
