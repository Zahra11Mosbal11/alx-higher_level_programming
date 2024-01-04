#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Class that defines properties of Rectangle.
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol: Used as symbol for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for retrieving the width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for retrieving the height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """That returns the rectangle area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return 2*width + 2*height (or return 0 if width or height is 0)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = ""
        for i in range(self.__height):
            rect += str(self.print_symbol) * self.__width + "\n"
        return rect.rstrip("\n")

    def __repr__(self):
        """Representation of the rectangle to be able to recreate a new"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Destructor method called when the object be destroyed."""
        type(self).number_of_instances -= 1
        print("{}".format("Bye rectangle..."))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """That returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.area()
        area2 = rect_2.area()
        if area1 >= area2:
            return rect_1
        else:
            return area2