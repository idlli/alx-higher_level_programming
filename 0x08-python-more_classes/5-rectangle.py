#!/usr/bin/python3
"""A module that defines a class `Rectangle`"""


class Rectangle:
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

    def area(self):
        """
        Calculates the area of the rectangle
        Returns:
            the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle
        Returns:
            the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """
        The unofficial string representaion of `Rectangle`
        Retruns:
            a string drawing the rectangle using the '#' char
        """
        result = ''
        if self.area() == 0:
            return result
        for row in range(self.__height):
            result += '#' * self.__width
            if row < self.__height - 1:
                result += '\n'
        return result

    def __repr__(self):
        """
        The official string representaion of `Rectangle`
        Retruns:
            a string to reconstruct the rectangle using `eval()`
        """
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        print('Bye rectangle...')
