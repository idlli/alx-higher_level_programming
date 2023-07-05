#!/usr/bin/python3
"""Module for add_integer function"""


def add_integer(a, b=98):
    """Adds two numbers

    Args:
        a (int|float): the first operand
        b (int|float, default: 98): the second operand

    Returns: the addition of the operands

    Raises: TypeError if args are not if the correct type
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    a, b = int(a), int(b)
    return a + b
