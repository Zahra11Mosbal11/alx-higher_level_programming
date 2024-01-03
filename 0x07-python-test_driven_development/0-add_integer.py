#!/usr/bin/python3
"""A function that adds 2 integers."""


def add_integer(a, b=98):
    """Adds 2 integers.

    Args:
        a: the first number.
        b: the secand one.

    Raise:
        TypeError: a and b must be first casted to integers if they are float.

    Returns:
        An integer: the addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return (a + b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
