#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Class that defines properties of Rectangle by: (based on 0-rectangle.py).

    Attributes:
        width: The width of rectangle.
        height: the heidht of rectangle.
    """
    def __init__(self, width=0, height=0):
        """Creates new instances of rectangle..

        Args:
            width: The width of rectangle.
            height: the heidht of rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter method for retrieving the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for width.

        Args:
            value (int): size of a rectangle.

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for retrieving the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for height.

        Args:
            value (int): size of a rectangle.

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """That returns the rectangle area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return 2*width + 2*height (or return 0 if width or height is 0)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))
