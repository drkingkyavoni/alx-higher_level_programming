#!/usr/bin/python3
""" Module contains MyList class
"""


class MyList():
    """
    Class MyList
    """
    def __init__(self):
        """
        initializes the list
        """
        self.list = []

    def append(self, element):
        """
        appends element to list
        """
        self.list.append(element)

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self.list))

    def __str__(self):
        """
        returns the string representation of the list
        """
        return str(self.list)
