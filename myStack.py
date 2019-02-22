from first_queue import Queue
from first_stack import Stack


class MyStack:

    def __init__(self, top=None):
        self.top = top
        self.size = 0
        self.queue_one = Queue()
        self.queue_two = Queue()
        self.max_stack = Stack()

    def __str__(self):
        my_stack_string = ''
        while self.queue_one.first:
            temp_node = self.queue_one.dequeue()
            self.queue_two.enqueue(temp_node.node_data)
            if temp_node.next_node:
                my_stack_string += str(temp_node) + ', '
            else:
                my_stack_string += str(temp_node)
        while self.queue_two.first:
            self.queue_one.enqueue(self.queue_two.dequeue().node_data)
        return my_stack_string

    def push(self, new_node):
        '''
        if the first queue is empty, just add the node
        if it isn't, move the first queue into the second
            add the new node to the first queue,
            then move the second queue back to the first
        increment the size at the end of either action
        :param new_node:
        :return:
        '''
        if not self.queue_one.first:
            self.queue_one.enqueue(new_node)
            self.top = new_node
            self.max_stack.push(new_node)
            self.size += 1
            return
        while self.queue_one.first:
            moving_node = self.queue_one.dequeue()
            self.queue_two.enqueue(moving_node.node_data)
        self.queue_one.enqueue(new_node)
        self.discover_if_new_max(new_node)
        while self.queue_two.first:
            moving_node = self.queue_two.dequeue()
            self.queue_one.enqueue(moving_node.node_data)
        self.top = self.queue_one.first
        self.size += 1

    def pop(self):
        '''
        pop the first node into a variable
        use a temp node to set the new top of the stack
            and then push that node back to the stack
        pop the max_stack twice to remove the double push
        decrement size at the end
        :return: the popped node
        '''
        pop_node = self.queue_one.dequeue()
        temp_node = self.queue_one.dequeue()
        self.top = temp_node
        self.push(temp_node.node_data)
        self.max_stack.pop()
        self.max_stack.pop()
        self.size -= 1
        return pop_node

    def is_empty(self):
        '''
        :return: whether the top is empty
        '''
        return self.top is None

    def size(self):
        return self.size

    @property
    def get_max(self):
        return self.max_stack.top

    def discover_if_new_max(self, new_value):
        '''
        check if the new value is greater than the current max
            push the new value if it is larger
            push the current top if it is not
        :param new_value:
        '''
        if new_value > self.max_stack.top.node_data:
            self.max_stack.push(new_value)
        else:
            self.max_stack.push(self.max_stack.top.node_data)
