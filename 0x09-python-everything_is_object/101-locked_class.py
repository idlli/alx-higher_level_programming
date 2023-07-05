#!/usr/bin/python3
"""Module for the LockedClass class"""


class LockedClass:
    """LockedClass prevents the user from creating attributes"""
    __slots__ = ['first_name']
