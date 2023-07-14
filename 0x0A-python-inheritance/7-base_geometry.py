#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """calculates the area of the geometry"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        validates whether attribute is an int and greater than 0
        Args:
            name (str): name of the attribute
            value (obj): value of the attribute
        Raises:
            TypeError: if value in not int
            ValueError: if value is not greater than 0
        """
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
