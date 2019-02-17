from queue import Queue


class MyStack:

    # TODO Matthew is teaching stephen how great todos are
    def __init__(self, top=None):
        self.top = None
        self.size = 0
        self.queue_one = Queue()
        self.queue_two = Queue()


    def __str__(self):
        # TODO something here!
        my_stack_string = ''
        for x in range(self.queue_one.size):
            temp_node = self.queue_one.dequeue()
            self.queue_two.enqueue(temp_node)
            my_stack_string += str(temp_node) + ', '
        for y in range(self.queue_two.size):
            self.queue_one.enqueue(self.queue_two.dequeue())
        return my_stack_string

    def push(self, new_node):
        if self.queue_one.size < 1:
            self.queue_one.enqueue(new_node)
            self.top = new_node
            self.size += 1
            return
        for x in range(self.queue_one.size):
            self.queue_two.enqueue(self.queue_one.dequeue())
        self.queue_one.enqueue(new_node)
        for x in range(self.queue_two.size):
            self.queue_one.enqueue(self.queue_two.dequeue())
        self.top = new_node
        self.size += 1

    def pop(self):
        pop_node = self.queue_one.dequeue()
        temp_node = self.queue_one.dequeue()
        self.top = temp_node
        self.push(temp_node)
        self.size -= 1
        return pop_node

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.size
