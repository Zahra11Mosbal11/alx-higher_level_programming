#!/usr/bin/python3
"""Function that returns the dictionary description with simple data"""
import json


def class_to_json(obj):
    """method that convert JSON serialization obj to dictionary"""
    data = obj.__dict__
    return data
