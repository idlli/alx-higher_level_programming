#!/usr/bin/python3
"""Module for the ``inherits_from()`` function"""


def inherits_from(obj, a_class):
    """
    checks whether obj class is subclass of a_class
    Args:
        obj (obj): the target object
        a_class (class): the class to compare
    Returns:
        whether obj class is subclass of a_class
    """
    return type(obj) != a_class and isinstance(obj, a_class)
