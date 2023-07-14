#!/usr/bin/python3
"""A module that defines a magic class"""
import math


class MagicClass:
    """A magic class ;)"""

    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """Calculates the area of the circle
        Returns:
            the resulted area
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of the circle
        Retruns:
            the resulted circumference
        """
        return 2 * math.pi * self.__radius
