from Node import Node


class SingleLinkedList(object):
    def __init__(self):
        self.__head: Node = None
        self.__tail: Node = None
        self.__size = 0

    # this method shows the first element of the list
    def _first(self):
        return self.__head.element

    # this method check is list empty or not
    def is_empty(self):
        return self.__size == 0

    # this method returns size of the list
    def size(self):
        return self.__size

    # this method add a new node as a new head to the list
    def _add_first(self, element):
        self.__head = Node(element, self.__head)
        if self.is_empty():
            self.__tail = self.__head

        self.__size = self.__size + 1

    # this method add a new node as a new tail to the list
    def _add_last(self, element):
        new_node = Node(element, None)
        if self.is_empty():
            self.__head = new_node
            self.__tail = self.__head
        else:
            self.__tail.next = new_node
            self.__tail = new_node

        self.__size = self.__size + 1

    # this method remove the head of the list
    def _remove_first(self):
        if self.is_empty():
            return None
        new_head = self.__head.next

        self.__head = new_head

        self.__size = self.__size - 1

        if self.is_empty():
            self.__tail = None
