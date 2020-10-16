"""
Math 560
Project 2
Fall 2020

p2stack.py

Partner 1:
Partner 2:
Date:
"""

"""
Stack Class
"""
class Stack:

    """
    Class attributes:
    stack    # The array for the stack.
    top      # The index of the top of the stack.
    numElems # The number of elements in the stack.
    """

    """
    __init__ function to initialize the Stack.
    Note: intially the size of the stack defaults to 3.
    Note: the stack is initally filled with None values.
    Note: since nothing is on the stack, top is -1.
    """
    def __init__(self, size=3):
        self.stack = [None for x in range(0,size)]
        self.top = -1
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.stack)) + ' ]\n'
        s += ('Top: %d' % self.top) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the stack is full.
    """
    def isFull(self):
        if self.numElems == len(self.stack):
            return True
        return False

    """
    isEmpty function to check if the stack is empty.
    """
    def isEmpty(self):
        if self.numElems == 0:
            return True
        return False

    """
    resize function to resize the stack by doubling its size.
    """
    def resize(self):
        size = len(self.stack)
        temp = [None for x in range(0, size*2)]
        temp[0:size] = self.stack[:]
        self.stack = temp
        return

    """
    push function to push a value onto the stack.
    """
    def push(self, val):
        if self.isFull():
            self.resize()
        self.top += 1
        self.numElems += 1
        self.stack[self.top] = val
        return

    """
    pop function to pop the value off the top of the stack.
    """
    def pop(self):
        if self.isEmpty():
            print("???")
            raise Exception("Can not pop with empty stack!\n")
            return None
        temp = self.stack[self.top]
        self.stack[self.top] = None
        self.numElems -= 1
        self.top -= 1
        return temp
