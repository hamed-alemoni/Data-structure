class Node(object):
    def __init__(self,element,next):
        self.__element = element
        self.__next : Node = next

    @property
    def element(self):
        return self.__element

    @element.setter
    def element(self,element):
        self.__element = element

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self,next):
        self.__next = next