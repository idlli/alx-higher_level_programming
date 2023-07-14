#!/usr/bin/python3
"""Module for Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that defines a square which inhirits from Rectangle"""

    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)
