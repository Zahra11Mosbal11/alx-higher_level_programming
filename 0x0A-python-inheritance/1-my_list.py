#!/usr/bin/python3
"""Contains MyList that inherits from list"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """Obj initializtion"""
        super().__init__()

    def print_sorted(self):
        """Method to prints the list."""
        print(sorted(self))
