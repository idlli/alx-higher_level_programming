#!/usr/bin/python3
"""Module for ``MyInt`` class"""


class MyInt(int):
    """Class that defines MyInt which inherits from int"""

    __eq__ = int.__ne__
    __ne__ = int.__eq__
