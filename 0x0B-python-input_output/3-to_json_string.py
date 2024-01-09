#!/usr/bin/python3
"""Function that returns the JSON representation of an object (string)."""
import json


def to_json_string(my_obj):
    """Method to representation of an object"""
    json_str = json.dumps(my_obj)
    return (json_str)
