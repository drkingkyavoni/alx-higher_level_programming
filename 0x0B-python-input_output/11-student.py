#!/usr/bin/python3
""" Module contains a class Student
"""


class Student:
    """ Class Student contains
        Attributes:
            first_name: str
            last_name: str
            age: int
        Methods:
            to_json
    """

    def __init__(self, first_name, last_name, age):
        """ initialize function
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ function that returns a dictionary str of a Student instance
            Return:
                dict
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in
                    self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
