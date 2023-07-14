#!/usr/bin/python3
"""Module for the MyList class"""


class MyList(list):
    """
    Mylist class which inhirits from list
    """

    def print_sorted(self):
        """
        prints the list sorted in ascending order
        """
        print(sorted(self))
