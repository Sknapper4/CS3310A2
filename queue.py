from linkedList import LinkedList


class Queue:

    # Create a first node when Queue is created
    # If no value is sent in, set first node to None
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    # Loop through the queue
    # check if there is a next node,
    # Make the return string pretty
    def __str__(self):
        walking_node = self.first
        fancy_queue = ''
        while walking_node.next_node:
            fancy_queue += str(walking_node) + ', '
            walking_node = walking_node.next_node
        fancy_queue += str(walking_node)
        return fancy_queue

    # Add a new node to the queue
    # create a new temporary node
    # If there are no nodes currently in the queue
    # make first and last node the temp node
    # if there are nodes, add the temporary node
    # to the end of the queue
    # increase the size of the queue
    def enqueue(self, new_node):
        '''

        :param new_node: Stephen
        :return:
        '''
        temp_node = LinkedList(new_node)
        if self.first is None:
            self.first = temp_node
            self.last = temp_node
            self.size += 1
            return
        self.last.next_node = temp_node
        temp_node.previous_node = self.last
        self.last = temp_node
        self.size += 1

    # remove the first node from the queue
    def dequeue(self):
        temp_node = self.first
        if temp_node is not None:
            self.first = temp_node.next_node
        self.size -= 1
        return temp_node

    # if the queue is empty
    # return false
    def is_empty(self):
        return not self.first

    # return the size of the queue
    def size(self):
        return self.size
