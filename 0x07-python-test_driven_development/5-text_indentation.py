#!/usr/bin/python3
"""A function that prints a text with 2 new lines"""


def text_indentation(text):
    """Method to prints a text with 2 new lines.

    Args:
        text: the string.

    Raises:
        TypeError: If test not string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = (char + "\n\n").join(
            [line.strip(" ") for line in text.split(char)])
    
    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
