from queue import Queue
from stack.py import Stack


def test_stack():
    print('Stack:')
    s = Stack()

    for i in range(0, 10):
        s.push(i)

    print(s)
    print(s.size)
    print('\nPop:')
    s.pop()
    print(s)
    print(s.size)


def test_queue():
    print('\nQueue:')
    q = Queue()

    for i in range(1, 10):
        q.enqueue(i)

    print(q)
    print('First:', q.first)
    print('Last:', q.last)
    print('size:', q.size)
    print('\nDequeue:')
    q.dequeue()
    print(q)
    print('first:', q.first)
    print('size:', q.size)


if __name__ == '__main__':
    test_stack()
    test_queue()


