#!/usr/bin/python3
"""this module creates a node and a singly linked list"""


class Node:
    """this class creates a node instance"""

    def __init__(self, data, next_node=None):
        """instantiates a node object"""

        if type(data) is not int:
            raise TypeError("data must be an integer")
        if not(type(next_node) is not Node or type(next_node) is not None):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """returns the data in this node"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets the data value"""
        self.__init__(value, self.__next_node)

    @property
    def next_node(self):
        """returns the next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the next_node"""
        self.__init__(self.__data, value)


class SinglyLinkedList:
    """creates the singly linked list"""
    def __init__(self):
        """instantiates a singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a value in the correct sorted position"""
        newNode = Node(value)
        head = self.__head
        if self.__head is None:
            self.__head = newNode
            return
        elif value < head.data:
            newNode.next_node = head
            self.__head = newNode
            return
        prevnode = head
        while prevnode.next_node is not None:
            if value < (prevnode.next_node).data:
                nestnode = prevnode.next_node
                prevnode.next_node = newNode
                newNode.next_node = nestnode
                return
            prevnode = prevnode.next_node
        prevnode.next_node = newNode

    def __str__(self):
        """represents the string format of the list"""
        head = self.__head
        string = ""
        while head.next_node is not None:
            string = string + str(head.data) + "\n"
            head = head.next_node
        string = string + str(head.data)
        return string
