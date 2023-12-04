#!/usr/bin/python3
""" Module contains class BaseGeometry
"""


class BaseGeometry:
    """
    class BaseGeometry
    Attributes:
    Methods:
        area()
    """

    def __init__(self):
        """ initialization function
        """
        pass

    def area(self):
        """ function raises an Exception with an error message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ function validates value
        """
        if not (type(value) is int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
