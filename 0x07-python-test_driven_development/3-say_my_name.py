#!/usr/bin/python3
"""Module for say_my_name function"""


def say_my_name(first_name, last_name=""):
    """Prints users name to stdout

    Args:
        first_name (str): the user's first name
        last_name (str, optional): the user's last name

    Raises:
        TypeError: when one or more of the args is not str
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print(f'My name is {first_name} {last_name}')
