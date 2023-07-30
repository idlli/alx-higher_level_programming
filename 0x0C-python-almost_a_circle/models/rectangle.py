#!/usr/bin/python3
"""Module for the ``Rectangle`` class"""
from models.base import Base


class Rectangle(Base):
    """
    Class that represents a Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter for the ``width`` attribute
        Returns:
            the value of ``width`` attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for the ``width`` attribute
        Args:
            value (int): the new value to be assigned to width
        Raises:
            TypeError: if value is not int
            ValueError: if value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        getter for the ``height`` attribute
        Returns:
            the value of ``height`` attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for the ``height`` attribute
        Args:
            value (int): the new value to be assigned to height
        Raises:
            TypeError: if value is not int
            ValueError: if value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        getter for the ``x`` attribute
        Returns:
            the value of ``x`` attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter for the ``x`` attribute
        Args:
            value (int): the new value to be assigned to x
        Raises:
            TypeError: if value is not int
            ValueError: if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """
        getter for the ``y`` attribute
        Returns:
            the value of ``y`` attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter for the ``y`` attribute
        Args:
            value (int): the new value to be assigned to y
        Raises:
            TypeError: if value is not int
            ValueError: if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        calculates the area of the rectangle
        Returns:
            the area (w * h)
        """
        return self.__width * self.__height

    def display(self):
        """
        prints the rectangle using the '#' character
        """
        print('\n' * self.__y, end='')
        for _ in range(self.__height):
            print(' ' * self.__x, '#' * self.__width, sep='')

    def update(self, *args, **kwargs):
        """
        updates the attributes of the rectangle
        Args:
            *args: the arguments tuple
            *kwargs: the keyword arguments dict
        """
        attrs = ('id', 'width', 'height', 'x', 'y')
        if len(args) > 0:
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for attr, value in kwargs.items():
                if attr in attrs:
                    setattr(self, attr, value)

    def to_dictionary(self):
        """
        return the dict representation of the rectangle
        Returns:
            a dictionary containing all the attributes and thier values
        """
        attrs = ('id', 'width', 'height', 'x', 'y')
        return {attr: getattr(self, attr) for attr in attrs}

    def __str__(self):
        id = self.id
        w, h = self.__width, self.__height
        x, y = self.__x, self.__y
        return f'[Rectangle] ({id}) {x}/{y} - {w}/{h}'
