from first_queue import Queue
from first_stack import Stack
from myQueue import MyQueue
from myStack import MyStack
import csv
import time


def read_stack_input_file():
    mystack = MyStack()
    action_count = 0
    output_file = open('output/stack_output.txt', 'w+')
    output_file.write("Stack: \n\nResults from MyStack implementation:\n\n")
    with open("input/stack_input.txt") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            action_word = row[0]
            if row[1]:
                value = row[1]
            if action_word == 'Push':
                mystack.push(value)
            if action_word == 'Pop':
                popped_value = mystack.pop()
                if popped_value:
                    output_string = 'Item' + str(popped_value) + ' popped\n'
                    output_file.write(output_string)
                else:
                    output_file.write('Can\'t pop from an empty stack\n')
            if action_word == 'getMax':
                if mystack.get_max:
                    output_string = 'Max value' + str(mystack.get_max) + '\n'
                    output_file.write(output_string)
                else:
                    output_string = 'Max value is' + str(mystack.get_max) + 'as stack is empty\n'
                    output_file.write(output_string)
            action_count += 1
    output_file.close()
    print('My Stack: ', mystack)
    print(action_count)


def read_queue_input_file():
    myqueue = MyQueue()
    action_count = 0
    output_file = open('output/queue_output.txt', 'w+')
    output_file.write('Queue: \n\nResults from MyQueue implementation:\n')
    with open("input/queue_input.txt") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            action_word = row[0]
            if row[1]:
                value = row[1]
            if action_word == 'Enqueue':
                myqueue.enqueue(value)
            if action_word == 'Dequeue':
                myqueue.dequeue()
            action_count += 1
    output_file.close()
    print('My Queue: ', myqueue)


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
    for x in range(0, 10):
        mystack.push(x)

    mystack.push(98)
    print(mystack.get_max)
    print(mystack)
    print(mystack.pop())
    print('\nPopped:')
    print(mystack)
    print(mystack.get_max)


def test_myqueue():
    print('==============================')
    print('MyQueue:')
    myqueue = MyQueue()

    for x in range(0, 10):
        myqueue.enqueue(x)

    print(myqueue)
    myqueue.dequeue()
    myqueue.dequeue()
    myqueue.dequeue()
    print(myqueue)
    print(myqueue.first)
    print(myqueue.last)


if __name__ == '__main__':
    read_stack_input_file()
    read_queue_input_file()
    # test_stack()
    # test_queue()
    # test_mystack()
    # test_myqueue()
