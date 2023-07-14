#!/usr/bin/python3
"""Module for ``append_after()`` function"""


def append_after(filename="", search_string="", new_string=""):
    """
    Searches for string in file and adds a line after each occurence
    Args:
        filename (str): the target file's name
        search_string (str): the string to search for
        new_string (str): the line to add
    """
    lines = None
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].find(search_string) != -1:
            lines.insert(i + 1, new_string)
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)
