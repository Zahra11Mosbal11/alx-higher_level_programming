#!/usr/bin/python3
"""A function that prints a square with the character #."""


def print_square(size):
    """Method for prints a square with the character #.

    Args:
        size: The size length of the square.

    Raises:
        TypeError: If size not intiger.
        ValueError: If size is less than 0.
        TypeError: If size is a float and is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
