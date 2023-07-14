class MaxHeap:
    def __init__(self):
        self.heap = []
    def _left_child(self,index):
        return index*2+1
    def _right_child(self,index):
        return index*2+2
    def _parent(self,index):
        return (index-1)//2
    def _swap(self,index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]


    def insert(self, value):
        
        self.heap.append(value)
        child_index = len(self.heap)-1
        parent_index = self._parent(child_index)
        
        while child_index != 0 and self.heap[parent_index] < value:
            self._swap(parent_index, child_index)
            child_index = parent_index
            parent_index = self._parent(child_index)
                  
        
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        if len(self.heap) == 2:
            self.heap.sort()
            return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sinkdown()
        return max_val
        
    def sinkdown(self):
        current = 0
        while True:
            
            try:
                replacement = self._left_child(current)
                if self.heap[replacement] < self.heap[self._right_child(current)]:
                    replacement = self._right_child(current)
            except:
                return
            
            if self.heap[current] < self.heap[replacement]:
                self._swap(current, replacement)
                current = replacement
            else:
                return


myheap = MaxHeap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

print(myheap.heap)


myheap.remove()

print(myheap.heap)


myheap.remove()

print(myheap.heap)

myheap.remove()

print(myheap.heap)
myheap.remove()

print(myheap.heap)
myheap.remove()

print(myheap.heap)
myheap.remove()

print(myheap.heap)
myheap.remove()

print(myheap.heap)


"""
    EXPECTED OUTPUT:
    ----------------
    [95, 75, 80, 55, 60, 50, 65]
    [80, 75, 65, 55, 60, 50]
    [75, 60, 65, 55, 50]

"""