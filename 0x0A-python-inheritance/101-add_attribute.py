#!/usr/bin/python3
"""Module for add_attribute() function"""


def add_attribute(obj, name, value):
    """
    Sets an attribute of an instance if possible
    Args:
        obj (obj): the target object
        name (str): the attribute name
        value (any): the attribute value
    """
    if '__slots__' in dir(obj) and name not in obj.__slots__:
        raise TypeError("can't add new attribute")
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
