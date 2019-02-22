from linkedList import LinkedList


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __str__(self):
        '''
        make the queue look pretty
        :return: the pretty string
        '''
        walking_node = self.first
        fancy_queue = ''
        while walking_node.next_node:
            fancy_queue += str(walking_node) + ', '
            walking_node = walking_node.next_node
        fancy_queue += str(walking_node)
        return fancy_queue

    def enqueue(self, new_node):
        '''
        create a new LinkedList node
        if there is nothing in the queue,
            set all the first and last to the new node
        if the queue already exists,
            set the last nodes next node to the new node
            make the new nodes previous node the last node
            set the new node as the new last node
        increment the size
        :param new_node: Stephen
        :return:
        '''
        temp_node = LinkedList(new_node)
        if not self.first:
            self.first = temp_node
            self.last = temp_node
        else:
            self.last.next_node = temp_node
            temp_node.previous_node = self.last
            self.last = temp_node
        self.size += 1

    def dequeue(self):
        '''
        set a temporary node to the first
        if the first node exists
            change the first node to the next node
        decrement size
        :return: the first node
        '''
        temp_node = self.first
        if temp_node:
            self.first = temp_node.next_node
        self.size -= 1
        return temp_node

    def is_empty(self):
        return not self.first

    def size(self):
        return self.size
