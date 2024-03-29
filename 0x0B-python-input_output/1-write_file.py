#!/usr/bin/python3
"""Function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Method to write in file"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
