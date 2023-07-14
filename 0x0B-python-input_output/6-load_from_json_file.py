#!/usr/bin/python3
"""Module for ``load_from_json_file()`` function"""


def load_from_json_file(filename):
    """
    Loads an object from json file
    Args:
        filename (str): the target file
    """
    import json
    with open(filename, 'r', encoding='utf-8') as file:
        return json.loads(file.read())
