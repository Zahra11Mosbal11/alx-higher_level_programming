#!/usr/bin/python3
"""Contains 4-inherits_from.py"""


def inherits_from(obj, a_class):
    """Returns true if obj is a subclass of a_class, otherwise false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
