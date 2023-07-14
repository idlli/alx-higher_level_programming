#!/usr/bin/python3
"""Module for the ``is_kind_of_class()`` function"""


def is_kind_of_class(obj, a_class):
    """
    checks whether obj class is an instance of a_class
    Args:
        obj (obj): the target object
        a_class (class): the class to compare
    Returns:
        whether obj class is an instance of a_class
    """
    return isinstance(obj, a_class)
