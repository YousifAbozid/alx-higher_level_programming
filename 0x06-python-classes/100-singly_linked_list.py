#!/usr/bin/python3
"""
7. Singly linked list
A class Node that defines a node of a singly linked list
"""


class Node:
    """class Node that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """private instance attribute data and next_node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """property to retrieve it"""
        return self.__data

    @data.setter
    def data(self, value):
        """property setter to set it"""
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """property to retrieve it"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """property setter to set it"""
        if next_node is not None and type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list class"""

    def __init__(self):
        """Initialize a new Singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserting a new Node to the SinglyLinkedList class.

        The node is inserted in the list in an ordered way.

        Args:
            value (Node): the new Node to insert.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """Returning elements of the SinglyLinkedList to print."""
        elements = []
        temp = self.__head
        while temp is not None:
            elements.append(str(temp.data))
            temp = temp.next_node
        return "\n".join(elements)
