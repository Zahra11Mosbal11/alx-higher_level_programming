#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""


    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""


        return (self.__size)

    @size.setter
    def size(self, value):
        """Property setter for size.

        Args:
            value (int): size of a square (1 side).

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""


        return (self.__size * self.__size)

    def my_print(self):
        """ prints in stdout the square with the character #"""


        for i in range(0, self.__size):
            for l in range(0, self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
