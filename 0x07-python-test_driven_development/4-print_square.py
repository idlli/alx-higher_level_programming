#!/usr/bin/python3
"""Module for the print_swuare function"""


def print_square(size):
    """
    Prints a square using the '#' character

    Args:
        size (int): the size of the square

    Raises:
        TypeError: if type of size in not int
        ValueError: if size < 0
    """
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if not isinstance(size, (int, float)):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    size = int(size)
    # if size == 0:
    #     print()
    #     return
    for _ in range(size):
        print('#' * size)
