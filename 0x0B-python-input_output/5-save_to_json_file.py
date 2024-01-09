#!/usr/bin/python3
"""Function that writes an Object to a text file, using"""
import json


def save_to_json_file(my_obj, filename):
    """write in file an obj"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
