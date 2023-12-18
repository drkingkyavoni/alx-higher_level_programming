#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a new instance of the class.

        Parameters:
            size (int): The size of the instance.
            x (int, optional): The x-coordinate of the instance. Defaults to 0.
            y (int, optional): The y-coordinate of the instance. Defaults to 0.
            id (Any, optional): The id of the instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Returns a string representation of the object.

        :return: A string representation of the object.
        :rtype: str
        """
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.size
        )

    @property
    def size(self):
        """ Get the size of the object.

        Returns:
            int: The size of the object.
        """
        return self.width

    @size.setter
    def size(self, value):
        super().validateIntValue("size", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the object.

        Args:
            *args: The positional arguments representing
            the attributes to be updated.
            **kwargs: The keyword arguments representing
            the attributes and their corresponding values to be updated.

        Returns:
            None
        """
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for attr, value in zip(attributes, args):
                self.__setattr__(attr, value)
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """ function returns dictionary representation of Rectangle class
        """
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
