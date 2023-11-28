#!/usr/bin/python3
"""
    Module contains LockedClass
    No tests for this module
"""


class LockedClass:
    """
        Class contains slots for first_name
    """
    __slots__ = ['first_name']

    def __init__(self, first_name='') -> None:
        """
            Function initializes first_name
            Returns: None
        """
        self.first_name = first_name
