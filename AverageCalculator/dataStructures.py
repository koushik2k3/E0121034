class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)
    
class MyQueue:
    def __init__(self):
        self.head = None
        self.ct = 0
    def printer(self):
        trvl = self.head
        vals = []
        while trvl is not None:
            vals += [trvl.data]
            trvl = trvl.next
        return vals
    def enqueue(self, node):
        trvl = self.head
        if trvl is None:
            self.head = node
        else:
            while trvl.next is not None:
                trvl = trvl.next
            trvl.next = node
        self.ct +=1
    def dequeue(self):
        data = self.head.data
        self.head = self.head.next
        self.ct -= 1
        return data
    
class LimitedQueue:
    def __init__(self, window):
        self.window = window
        self.queue = MyQueue()
        self.set = set()

    def add(self, element):
        if element not in self.set:
            if (self.queue.ct) >= self.window:
                oldest_element = self.queue.dequeue()
                self.set.remove(oldest_element)
            self.queue.enqueue(Node(element))
            self.set.add(element)

    def printer(self):
        return self.queue.printer()