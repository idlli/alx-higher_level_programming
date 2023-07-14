#!/usr/bin/python3
"""Module for ``class_to_json()`` function"""


def class_to_json(obj):
    """
    Serializes an object
    Args:
        obj (obj): the target object
    """
    return obj.__dict__
