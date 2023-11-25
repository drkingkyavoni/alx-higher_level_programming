#!/usr/bin/python3
"""
    Module contains the say_my_name function
    Return: str
    Tests contained in tests/3-say_my_name.txt
"""


def say_my_name(first_name: str, last_name=""):
    """
        Returns a formatted firstname and lastname
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f'My name is {first_name} {last_name}')
