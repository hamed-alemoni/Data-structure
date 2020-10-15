from SingleLinkedList import SingleLinkedList
from Stack import Stack


class SingleLinkedListStack(SingleLinkedList, Stack):
    def __init__(self):
        SingleLinkedList.__init__(self)

    def pop(self):
        return super().remove_first()

    def size(self):
        return super().size()

    def is_empty(self):
        return super().is_empty()

    def push(self, element):
        super().add_first(element)

    def top(self):
        return super().first()