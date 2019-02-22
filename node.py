class Node:

    def __init__(self, node_data=None, previous_node=None, next_node=None):
        self.node_data = node_data
        self.previous_node = previous_node
        self.next_node = next_node

    def __str__(self):
        return str(self.node_data)

    def is_head(self):
        if self.previous_node is None:
            return True
        return False

    def is_tail(self):
        if self.next_node is None:
            return True
        return False
