#!/usr/bin/python3
"""A module that defines a class `Rectangle`"""


class Rectangle(dict):
    """
    An Rectangle class
    Attributes:
        width (int, optional): the width of the rectangle
        height (int, optional): the height of the rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute
        Args:
            value (int): the new value to set
        Raises:
            TypeError: if `value` is not an int
            ValueError: if `value` is negative
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for hight attribute
        Args:
            value (int): the new value to set
        Raises:
            TypeError: if `value` is not an int
            ValueError: if `value` is negative
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
