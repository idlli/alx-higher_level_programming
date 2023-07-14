#!/usr/bin/python3
"""A module that defines and implements a sigly linked list"""


class Node:
    """Single node for a linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method for `data`
        Returns:
            the `data` attribute
        """
        return self.__data

    @data.setter
    def data(self, data):
        """Setter method for `data`
        Args:
            data (int): one element of liked list
        Raises:
            TypeError when arguments are not correct
        """
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        self.__data = data

    @property
    def next_node(self):
        """Getter method for `next_node`
        Returns:
            the `next_node` attribute
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node=None):
        """Setter method for `next_node`
        Args:
            next_node (:obj:`Node`): next node in the list
        Raises:
            TypeError when arguments are not correct
        """
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = next_node


class SinglyLinkedList:
    """Class that defines a singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new sorted value to the linked list
        Args:
            value (int): a new value to insert
        """
        if self.__head is None:
            self.__head = Node(value)
            return
        new = Node(value)
        if value <= self.__head.data:
            new.next_node, self.__head = self.__head, new
            return
        node = self.__head
        while node.next_node is not None:
            if value <= node.next_node.data:
                new.next_node, node.next_node = node.next_node, new
                return
            node = node.next_node
        node.next_node = new

    def __str__(self):
        if self.__head is None:
            return ''
        node = self.__head
        string = ''
        while True:
            string += str(node.data)
            if node.next_node:
                string += '\n'
                node = node.next_node
            else:
                break
        return string
