#!/usr/bin/python3
"""Containes the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """That it returns [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.height)

    def update(self, *args, **kwargs):
        """Update the Square.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        attrs = ["id", "size", "x", "y"]
        if args:
            for i, val in enumerate(args):
                setattr(self, attrs[i], val)

        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
