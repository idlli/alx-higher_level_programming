#!/usr/bin/python3
"""A module that defines an Square class"""


class Square:
    """Class defines a square object"""

    def __init__(self, size=0):
        """The class constructor
        Args:
            size (int, optional): size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
