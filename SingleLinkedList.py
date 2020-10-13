from Node import Node


class SingleLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # this method check is list empty or not
    def is_empty(self):
        return self.__size == 0

    # this method add a new node as a new head
    def add_first(self, element):
        self.__head = Node(element, self.__head)
        if self.is_empty():
            self.__tail = self.__head

        self.__size = self.__size + 1
