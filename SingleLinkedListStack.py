from SingleLinkedList import SingleLinkedList
from Stack import Stack


class SingleLinkedListStack(Stack,SingleLinkedList):
    def __init__(self):
        pass
        #super(SingleLinkedListStack, self).__init__()

    def pop(self):
        super(SingleLinkedListStack, self).remove_first()

    def size(self):
        super(SingleLinkedListStack, self).size()

    def is_empty(self):
        super(SingleLinkedListStack, self).is_empty()

    def push(self, element):
        super(SingleLinkedListStack, self).add_first(element)

    def top(self):
        super(SingleLinkedListStack, self).first()