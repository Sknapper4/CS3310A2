from first_queue import Queue
from first_stack import Stack
from myQueue import MyQueue
from myStack import MyStack


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
    print('==============================')
    print('Queue:')
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


def test_mystack():
    print('==============================')
    print('My Stack:')
    mystack = MyStack()
    for x in range(1, 10):
        mystack.push(x)

    mystack.push(0)
    print(mystack.get_max)
    print(mystack)
    print(mystack.pop())
    print('\nPopped:')
    print(mystack)


def test_myqueue():
    print('==============================')
    print('MyQueue:')
    myqueue = MyQueue()
    myqueue.enqueue(1)
    myqueue.enqueue(3)
    myqueue.enqueue(3)
    myqueue.dequeue()
    print(myqueue)


if __name__ == '__main__':
    # test_stack()
    # test_queue()
    # test_mystack()
    test_myqueue()
