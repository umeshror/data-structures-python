"""
Given the Stack class below, implement a Queue class using two stacks!
Use a Python list data structure as your Stack.

"""


class Queue2Stacks(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, element):
        self.in_stack.append(element)

    def dequeue(self):
        if not self.out_stack:  # out_stack is empty
            while self.in_stack:
                # create out stack for FIFO
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()


q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)

for i in range(5):
    print (q.dequeue())
