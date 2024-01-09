#!/usr/bin/python3
"""Function that creates an Object from a “JSON file“"""
import json


def load_from_json_file(filename):
    """Mrthod to creates an Object from a “JSON file"""
    with open(filename, 'r') as file:
        obj_json = json.load(file)
        return obj_json
