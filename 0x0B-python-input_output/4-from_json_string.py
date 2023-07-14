#!/usr/bin/python3
"""Module for ``from_json_string()`` function"""


def from_json_string(my_str):
    """
    Turns a json string into an object
    Args:
        my_str (str): the target json string
    """
    import json
    return json.loads(my_str)
