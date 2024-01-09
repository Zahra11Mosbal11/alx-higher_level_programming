#!/usr/bin/python3
"""Contains 9-student.py"""


class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """That retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        ret = {key: val for key, val in self.__dict__.items() if key in attrs}
        return ret

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key in json:
            setattr(self, key, json[key])
