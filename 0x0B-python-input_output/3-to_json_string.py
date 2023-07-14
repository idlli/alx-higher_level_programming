#!/usr/bin/python3
"""Module for ``to_json_string()`` function"""


def to_json_string(my_obj):
    """
    Turns an object to its json representation string
    Args:
        my_obj (obj): the target object
    """
    import json
    return json.dumps(my_obj)
