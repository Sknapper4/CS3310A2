from first_stack import Stack


class MyQueue:

    def __init__(self, first=None):
        self.first = first
        self.last = None
        self.size = 0
        self.stack_one = Stack()
        self.stack_two = Stack()

    def __str__(self):
        return str(self.first)

    def enqueue(self, new_node):
        if self.stack_one.size < 1:
            self.stack_one.push(new_node)
            self.first = self.stack_one.top
            self.last = self.stack_one.top
            self.size += 1
            return
        for x in range(self.stack_one.size):
            moving_node = self.stack_one.pop()
            self.stack_two.push(moving_node)
        self.stack_one.push(new_node)
        self.last = new_node
        for y in range(self.stack_two.size):
            moving_node = self.stack_two.pop()
            self.stack_one.push(moving_node)
        self.first = self.stack_one.top
        self.size += 1

    def dequeue(self):
        for x in range(self.stack_one.size):
            moving_node = self.stack_one.pop()
            self.stack_two.push(moving_node)
        dequeued_node = self.stack_two.pop()
        self.size -= 1
        self.last = self.stack_two.top
        for x in range(self.stack_two.size):
            moving_node = self.stack_two.pop()
            self.stack_one.push(moving_node)
        self.first = self.stack_one.top
        return dequeued_node
