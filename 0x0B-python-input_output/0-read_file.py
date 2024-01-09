#!/usr/bin/python3
"""A function that reads a text file."""


def read_file(filename=""):
    """Method that read from file and print it"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
