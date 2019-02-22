from first_stack import Stack


class MyQueue:

    def __init__(self, first=None):
        self.first = first
        self.last = None
        self.size = 0
        self.stack_one = Stack()
        self.stack_two = Stack()

    def __str__(self):
        my_queue_string = ''
        while self.stack_one.top:
            temp_node = self.stack_one.pop()

            my_queue_string += str(temp_node) + ', '
            self.stack_two.push(temp_node.node_data)
        while self.stack_two.top:
            temp_node = self.stack_two.pop()
            self.stack_one.push(temp_node.node_data)
        return my_queue_string

    def enqueue(self, new_node):
        if not self.stack_one.top:
            self.stack_one.push(new_node)
            self.first = self.stack_one.top
            self.last = self.stack_one.top
        else:
            while self.stack_one.top:
                moving_node = self.stack_one.pop()
                self.stack_two.push(moving_node)
            self.stack_one.push(new_node)
            self.last = new_node
            while self.stack_two.top:
                moving_node = self.stack_two.pop()
                self.stack_one.push(moving_node.node_data)
            self.first = self.stack_one.top
        self.size += 1

    def dequeue(self):
        dequeued_node = self.stack_one.pop()
        self.first = self.stack_one.top
        self.size -= 1
        return dequeued_node
