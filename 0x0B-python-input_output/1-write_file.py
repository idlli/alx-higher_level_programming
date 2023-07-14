#!/usr/bin/python3
"""Module for ``write_file()`` function"""


def write_file(filename="", text=""):
    """
    Writes a string into a file
    Args:
        filename (str): the target file's name
        text (str): the text to write
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
