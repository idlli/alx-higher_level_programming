#!/usr/bin/python3
"""Module for the ``lookup()`` function"""


def lookup(obj):
    """
    returns list of attributes and methods of an object
    Args:
        obj (obj): the target object
    Returns:
        list of attributes and methods of obj
    """
    return dir(obj)
