#!/usr/bin/python3
"""Module for the ``Student`` class"""


class Student:
    """Class representing a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Serializes the object
        Args:
            attrs (list): used to retrieve only specific attributes
        """
        if type(attrs) == list:
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }
        else:
            return self.__dict__
