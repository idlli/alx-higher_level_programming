#!/usr/bin/python3
"""A module that defines an Square class"""


class Square:
    """Class defines a square object"""

    def __init__(self, size=0):
        """The class constructor
        Args:
            size (int, optional): size of the square
        """
        self.size = size

    @property
    def size(self):
        """Getter method for `size`"""
        return self.__size

    @size.setter
    def size(self, size=0):
        """Setter method for `size`
        Args:
            size (int, optional): size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Instance function for area of the square
        Returns:
            the area of the square (size ^ 2)
        """
        return self.__size ** 2
