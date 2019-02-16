from linkedList import LinkedList


class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    # Loop through the stack
    # check if there is a next node,
    # Make the return string pretty
    def __str__(self):
        walking_node = self.top
        stack_string = str(walking_node) + ', '
        while walking_node.previous_node:
            if walking_node.previous_node.previous_node:
                stack_string += str(walking_node.previous_node) + ', '
            else:
                stack_string += str(walking_node.previous_node)
            walking_node = walking_node.previous_node
        return stack_string

    # add a new node to the top of the stack
    def push(self, new_node):
        temp_node = LinkedList(new_node)
        if self.is_empty():
            self.top = temp_node
            self.size += 1
            return
        self.top.next_node = temp_node
        temp_node.previous_node = self.top
        self.top = temp_node
        self.size += 1

    # remove the node from the top of the stack
    def pop(self):
        temp_node = self.top
        self.top = temp_node.previous_node
        temp_node.previous_node = None
        return temp_node

    # if the stack is empty
    # return false
    def is_empty(self):
        return self.top is None

    # return the size of the stack
    def size(self):
        return self.size

