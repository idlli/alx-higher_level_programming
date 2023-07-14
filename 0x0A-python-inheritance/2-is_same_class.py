#!/usr/bin/python3
"""Module for the ``is_same_class()`` function"""


def is_same_class(obj, a_class):
    """
    checks whether obj class is a_class
    Args:
        obj (obj): the target object
        a_class (class): the class to compare
    Returns:
        whether obj class is a_class
    """
    return type(obj) == a_class
