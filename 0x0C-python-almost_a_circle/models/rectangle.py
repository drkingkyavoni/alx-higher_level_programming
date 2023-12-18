#!/usr/bin/python3
""" Module contains a Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """ Class contains attributes and methods
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes Rectangle class
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ define width property
        """
        return self.__width

    @property
    def height(self):
        """ define height property
        """
        return self.__height

    @property
    def x(self):
        """ define x property
        """
        return self.__x

    @property
    def y(self):
        """ define y property
        """
        return self.__y

    @width.setter
    def width(self, value):
        """ set width as private
        """
        self.validateIntValue("width", value, False)
        self.__width = value

    @height.setter
    def height(self, value):
        """ set height as private
        """
        self.validateIntValue("height", value, False)
        self.__height = value

    @x.setter
    def x(self, value):
        """ set x as private
        """
        self.validateIntValue("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """ set y as private
        """
        self.validateIntValue("y", value)
        self.__y = value

    def validateIntValue(self, name, value, flag=True) -> None:
        """ validate value as integer
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if not flag and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if flag and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self) -> int:
        """ calculate area of rectangle
        """
        return self.height * self.width

    def display(self):
        """ prints in stdout the Rectangle instance with the character #
        """
        print("{}".format("\n" * self.y), end="")
        print("{}".format("\n".join(
            [" " * self.x + "#" * self.width
             for _ in range(self.height)]
        )))

    def __str__(self):
        """ returns string [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.width, self.height
        )

    def update(self, *args, **kwargs):
        """ function updates class attributes
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for attr, value in zip(attributes, args):
                self.__setattr__(attr, value)
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """ function returns dictionary representation of Rectangle class
        """
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
