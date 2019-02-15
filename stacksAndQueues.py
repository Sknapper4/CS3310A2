from .linkedList import Node


class Stack:

    def __init__(self, top=None):
        self.top = top

    def push(self, new_node):
        temp_node = Node(new_node)

        if self.__sizeof__() == 0:
            self.top = temp_node
        else:
            temp_node.previous_node = self.top
            self.top.next_node = temp_node
            self.top = temp_node

    def pop(self):
        temp_node = self.top
        self.top = temp_node.previous_node
        temp_node.previous_node = None

        return temp_node

    def is_empty(self):
        return self.top is None


class Queue:

    def __init__(self, first=None):
        self.first = first

    def enqueue(self, new_node):
        temp_node = new_node
