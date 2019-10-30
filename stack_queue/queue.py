class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        # add it at the start
        self.items.insert(0, item)

    def dequeue(self):
        # remove it from end
        return self.items.pop()

    def size(self):
        return len(self.items)
