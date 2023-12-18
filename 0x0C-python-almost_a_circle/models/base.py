#!/usr/bin/python3
""" Module contains a Base class
"""
import csv
import json
from pathlib import Path


class Base:
    """ Base class
        Attributes:
            __nb_objects: int
        Methods:
            __init__
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializing function
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ function returns the JSON string
        representation of dict list
        """
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        """
        filename: str = cls.__name__ + ".json"
        if list_objs is not None:
            list_objs: list[Base] = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string to a Python object.

        Parameters:
            json_string (str): The JSON string to be converted.

        Returns:
            object: The Python object represented by the JSON string.
            If the input is an empty string, an empty list is returned.
        """
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance of the class using the provided dictionary.

        Parameters:
            **dictionary (dict): A dictionary containing the attributes
            of the instance.

        Returns:
            obj: An instance of the class with its attributes updated
            based on the provided dictionary.
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            obj = Rectangle(10, 9)
        elif cls is Square:
            obj = Square(10)
        else:
            obj = None
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
        Load data from a file and return a list of instances of the class.

        :param cls: The class to create instances of.
        :return: A list of instances of the class.
        """
        filename = '{}.json'.format(cls.__name__)
        if not Path(filename).is_file():
            return []
        with open(filename, encoding="utf-8") as file:
            return [cls.create(**d) for d in cls.from_json_string(file.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save objects to a CSV file.

        Args:
            list_objs (list): A list of objects to be saved.

        Returns:
            None
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            list_objs = [[o.id, o.height, o.width, o.x, o.y]
                         for o in list_objs]
        elif cls is Square:
            list_objs = [[o.id, o.size, o.x, o.y]
                         for o in list_objs]
        else:
            list_objs = None
        with open("{}.csv".format(cls.__name__), "w") as file:
            csv.writer(file).writerows(list_objs)


@classmethod
def load_from_file_csv(cls):
    """
    Loads objects from a CSV file and returns a list of objects.

    Parameters:
    - None

    Returns:
    - list_objs (list)
    """
    from models.rectangle import Rectangle
    from models.square import Square
    with open(f"{cls.__name__}.csv", "r") as file:
        reader = csv.reader(file)
        if cls is Rectangle:
            list_objs = [Rectangle(id=d[0], height=d[1], width=d[2],
                                   x=int(d[3]), y=int(d[4])) for d in reader]
        elif cls is Square:
            list_objs = [Square(id=d[0], size=d[1],
                                x=int(d[3]), y=int(d[4])) for d in reader]
        else:
            list_objs = []
    return list_objs
