#!/usr/bin/python3
""" Module contains custom int
"""


class MyInt(int):
    """ Class that inherits from int
    """

    def __eq__(self, value):
        """ Method that returns not equals
        """
        return int.__ne__(self, value)

    def __ne__(self, value):
        """ Method that returns equals
        """
        return int.__eq__(self, value)
