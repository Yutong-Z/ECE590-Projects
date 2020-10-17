"""
Math 560
Project 2
Fall 2020

p2queue.py

Partner 1: Yutong Zhaang (yz566)
Partner 2: Jiaxi Yin (jy280)
Date: 15/10/2020
"""

"""
Queue Class
"""
class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 3.
    Note: the queue is initally filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.queue)) + ' ]\n'
        s += ('Front: %d' % self.front) + '\n'
        s += ('Rear: %d' % self.rear) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the queue is full.
    """
    def isFull(self):
        if self.numElems == len(self.queue):
            return True
        return False

    """
    isEmpty function to check if the queue is empty.
    """
    def isEmpty(self):
        if self.numElems == 0:
            return True
        return False

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """
    def resize(self):
        #Reset the wrapped around queue and double the size
        self.queue = self.queue[self.front:]+self.queue[:self.rear]+[None for x in range(0,len(self.queue))]
        self.front = 0
        self.rear = self.numElems
        return

    """
    push function to push a value into the rear of the queue.
    """
    def push(self, val):
        #Resize when pushing to a full queue
        if self.isFull():
            self.resize()
        self.queue[self.rear] = val
        self.rear += 1
        self.numElems += 1
        #Wrap around
        if self.rear == len(self.queue):
            self.rear = 0;
        return

    """
    pop function to pop the value from the front of the queue.
    """
    def pop(self):
        #Exit when pop on empty queue
        if self.isEmpty():
            raise Exception("Can not pop with empty queue!\n")
        temp = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        self.numElems -= 1
        #Wrap around
        if self.front == len(self.queue):
            self.front = 0;
        return temp
