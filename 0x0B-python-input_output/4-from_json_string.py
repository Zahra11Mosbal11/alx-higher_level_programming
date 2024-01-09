#!/usr/bin/python3
"""Function that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """Method to represented by a JSON string"""
    py_obj = json.loads(my_str)
    return py_obj
