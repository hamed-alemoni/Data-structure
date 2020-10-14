import numpy as np
from Stack import Stack


class ArrayStack(Stack):

    def __init__(self, capacity=10000):
        self.__t = -1
        self.__data = np.empty(capacity)

    # this method shows size of stack
    def size(self):
        return self.__t + 1

    # this method determines the stack is empty or not
    def is_empty(self):
        return self.__t == -1

    # this method pushes an element upon of the stack
    def push(self, element):
        if self.__t == self.__data.size:
            raise OverflowError('Stack is full')
        self.__t = self.__t + 1
        self.__data[self.__t] = element

    # this method removes the upon element of the stack
    def pop(self):
        if self.is_empty():
            return None
        self.__data[self.__t] = None
        self.__t = self.__t - 1

    # this method returns the upon element of the stack
    def top(self):
        if self.is_empty():
            return None
        return self.__data[self.__t]
