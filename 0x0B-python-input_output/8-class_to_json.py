#!/usr/bin/python3
"""Function that returns the dictionary description with simple data"""


def class_to_json(obj):
    """method that convert JSON serialization obj to dictionary"""
    return obj.__dict__
