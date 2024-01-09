#!/usr/bin/python3
"""Function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Method thet write on file withot remove the old"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
