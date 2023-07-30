#!/usr/bin/python3
"""Module for the ``Square`` class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class that represents a Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        getter for the ``size`` attribute
        Returns:
            the value of ``size`` attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter for the ``size`` attribute
        Args:
            value (int): the new value to be assigned to size
        Raises:
            TypeError: if value is not int
            ValueError: if value is <= 0
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updates the attributes of the square
        Args:
            *args: the arguments tuple
            *kwargs: the keyword arguments dict
        """
        attrs = ('id', 'size', 'x', 'y')
        if len(args) > 0:
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for attr, value in kwargs.items():
                if attr in attrs:
                    setattr(self, attr, value)

    def to_dictionary(self):
        """
        return the dict representation of the square
        Returns:
            a dictionary containing all the attributes and thier values
        """
        attrs = ('id', 'size', 'x', 'y')
        return {attr: getattr(self, attr) for attr in attrs}

    def __str__(self):
        id = self.id
        size = self.width
        x, y = self.x, self.y
        return f'[Square] ({id}) {x}/{y} - {size}'
