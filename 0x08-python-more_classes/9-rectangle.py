#!/usr/bin/python3
"""A module that defines a class `Rectangle`"""


class Rectangle:
    """
    An Rectangle class
    Attributes:
        width (int, optional): the width of the rectangle
        height (int, optional): the height of the rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Determines which of two rectangles is bigger (based on area)
        Args:
            rect_1 (Rectangle): the first rectangle
            rect_2 (Rectangle): the second rectangle
        Retruns:
            the rectangle with the bigger area
        Raises:
            TypeError: if the arguments are not rectangles
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Factory method to create a square
        Args:
            size (int, optional): the size of the square
        Returns:
            a new rectangle with same width and height = size
        """
        return cls(size, size)

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
            result += str(self.print_symbol) * self.__width
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
        Rectangle.number_of_instances -= 1
