#!/usr/bin/python3
"""Defind aclass Node."""


class Node:
    """
    class Node that defines a node of a singly linked list.

    Attributes:
        datd.
    """
    def __init__(self, data, next_node=None):

        """Creates new instances of Node.

        Args:
            __data (int): the date in node.
            __next_node (Node): new node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Return the data in node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Property setter of data
        
        Args:
            value (int): the data of node.

        Raises:
            TypeError: data must be an integer.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Return the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Property setter of next_node

        Args:
            value (Node): the next node

        Raises:
            TypeError: next_node must be a Node object
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

"""Defind class SinglyLinkedList"""


class SinglyLinkedList:
    """
    Class that defines a singly linked list.

    Attributes:
        head: pointer to the node.
    """
    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """Represents the class objects as a string.

        Returns: The class object represented as a string.
        """
        to_print = self.__head
        print_node = []
        while to_print:
            print_node.sort()
            print_node.append(str(to_print.data))
            to_print = to_print.next_node

        print_node.sort(key=int)
        return ("\n".join(print_node))
    def sorted_insert(self, value):
        """Inserts a new node at a given position.

        Args:
            value: value.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node
