#!/usr/bin/python3
"""Module for ``save_to_json_file()`` function"""


def save_to_json_file(my_obj, filename):
    """
    saves an object as json string to a file
    Args:
        my_obj (obj): the target object
        filename (str): the name of the file to save into
    """
    import json
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
