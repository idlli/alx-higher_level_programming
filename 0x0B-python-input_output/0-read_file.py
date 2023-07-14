#!/usr/bin/python3
"""Module for ``read_file()`` function"""


def read_file(filename=""):
    """
    Reads and prints the content of a file to stdout
    Args:
        filename (str): the target file's name
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
