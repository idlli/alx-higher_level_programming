#!/usr/bin/python3
"""Module for ``append_write()`` function"""


def append_write(filename="", text=""):
    """
    Appends a string into a file
    Args:
        filename (str): the target file's name
        text (str): the text to write
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
