class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class Stack:
    def __init__(self):
        self.top = None
        self.height = 0
        
    def print(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
        
    def push(self, value):
        new = Node(value)
        if self.height == 0:
            self.top = new
        else:
            new.next = self.top
            self.top = new
        self.height += 1
        
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        
        
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        
    def print(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next
            
    def enqueue(self, value):
        new = Node(value)
        if self.length == 0:
            self.first = new
            self.last = new
        else:
            self.last.next = new
            self.last = new
        self.length += 1
        
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1