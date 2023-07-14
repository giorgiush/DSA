class Node():
    def __init__(self, value):
        self.value = value 
        self.next = None
        self.prev = None
        
class Dll():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def print(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            
    def append(self, value):
        new = Node(value)
        if self.length > 0:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
        else:
            self.head = new
            self.tail = new
        self.length += 1
        
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -=1
    
    def prepend(self, value):
        new = Node(value)
        if self.length == 0:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
        self.length += 1
    
    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
        self.length -= 1
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index <= self.length/2:
            result = self.head
            for _ in range(index):
                result = result.next
        else:
            result = self.tail
            for _ in range(self.length - index - 1):
                result = result.prev
        return result
            
    def set(self, index, value):
        if index < 0 or index >= self.length:
            return False
        target = self.get(index)
        target.value = value
        
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new = Node(value)
            curr = self.get(index)
            prev = curr.prev
            prev.next = new
            new.prev = prev
            new.next = curr
            curr.prev = new
            self.length += 1
            
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.pop_first()
        elif index == self.length -1:
            self.pop()
        else:
            temp = self.get(index)
            before = temp.prev
            after = temp.next
            before.next =after
            after.prev = before
            temp.prev = None
            temp.next = None
            self.length -= 1
            return temp
        
    def swap_first_last(self):
        temp = self.head.value
        self.set(0, self.tail.value)
        self.set(self.length - 1, temp)
        return True
        
    def reverse(self):
        if self.length <= 0:
            return None
        if self.length == 1:
            return self.head
        last = self.tail
        for _ in range(self.length-2):
            temp = self.tail.prev
            self.tail.prev = temp.prev
            last.next = temp
            temp.prev = last
            last = temp
        last.next = self.head
        self.head.prev = last
        self.head.next = None
        self.tail.prev = None
        self.head, self.tail = self.tail, self.head
        return True
    
    def is_palindrome(self):
        if self.length % 2 == 0:
            return False
        else:
            mid = self.head
            for _ in range(self.length//2):
                mid = mid.next
            left = mid
            right = mid
            for _ in range(self.length//2):
                left = left.prev
                right = right.next
                if left.value != right.value:
                    return False
            return True
        
    def swap_pairs(self):
        if self.length <2:
            return False
        if self.length % 2 == 0:
            A = self.head
            for _ in range(self.length//2):
                B = A.next
                A.next = B.next
                B.prev = A.prev
                B.next = A
                A.prev = B
                if B.prev != None:
                    B.prev.next = B
                if A.next != None:
                    A.next.prev = A
                A = A.next
            self.head = self.head.prev
            self.tail = self.tail.next
            return True
        else:
            return False

        
        
            
            
dll = Dll()

dll.append(111)
dll.append(222)
dll.append(777)
dll.append(888)

# dll.prepend(1)
# dll.prepend(2)
# dll.insert(6, 100)
# dll.remove(6)

# dll.pop()
# dll.pop_first()
# print(dll.get(4).value)
# dll.set(4, 100)

# dll.swap_first_last()
# dll.reverse()
# print(dll.is_palindrome())
# dll.swap_pairs()

dll.print()
