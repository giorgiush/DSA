class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class Ll:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def print(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next   
            
    def append(self, value):
        new = Node(value)
        if self.head == None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        self.length += 1
        return True
        
    def pop(self):
        temp = self.head
        if self.length > 1:
            while temp != self.tail:
                if temp.next == self.tail:
                    self.tail = temp
                    self.tail.next = None
                    self.length -= 1
                else:
                    temp = temp.next  
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        return True
    
    def prepend(self, value):
        new = Node(value)
        if self.length < 1:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head = new
        self.length += 1
        return True
            
    def popfirst(self):
        if self.length <1:
            return None
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1
        return True
            
    def get(self, index):
        if index <0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.data = value
            
    def insert(self, index, value):
        new = Node(value)
        if index <0 or index >= self.length:
            return False
        if index == 0:
            self.prepend(value)
            return True
        elif index == self.length-1:
            self.append(value)
            return True
        temp = self.head
        for _ in range(index-1):
            temp = temp.next
        new.next = temp.next
        temp.next = new
        self.length += 1
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.popfirst()
            return True
        elif index == self.length-1:
            self.pop()
            return True
        temp = self.get(index-1)
        garbage = temp.next
        temp.next = garbage.next
        garbage.next = None
        self.length -= 1
        return True
    
    def reverse(self):
        first = self.head
        second = first.next
        third = second.next
        while first != self.tail:
            second.next = first
            first = second
            second = third
            if third is not None:
                third = third.next
        self.head, self.tail = self.tail, self.head
        self.tail.next = None
        
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next           
            if fast == slow:
                return True
        return False
    
    def reverse_between(self, m, n):
        if self.length < 1:
            return None
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        for i in range(m):
            prev = prev.next
        curr = prev.next
        temp = curr.next
        for i in range(n-m):
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            temp = curr.next
        self.head = dummy.next
        
    def partition_list(self, x):
        new = Node(0)
        new.next = self.head
        P2 = new
        P3 = new
        while P2.data < x:
            P1 = P2
            P2 = P2.next   
            P3 = P3.next
        A = P2.next
        while A != None:
            if A.data < 4:
                P3.next = A.next
                P1.next = A
                A.next = P2
                A = P3.next
                P1 = P1.next
            else:
                A = A.next
                P3 = P3.next
        self.head = new.next
        
    def remove_duplicates(self):
        temp = set()
        temp.add(self.head.data)
        previous = self.head
        current = self.head.next
        while current:
            if current.data in temp:
                current = current.next
                previous.next = current
                self.length -= 1
            else:
                temp.add(current.data)
                previous = current
                current = current.next
                

def kth_item_from_end(ll, k):
    if k == 0:
        return None
    fast = ll.head
    slow = ll.head
    for _ in range(k):
        if fast == None:
            return None
        fast = fast.next
    while fast != None:
        fast = fast.next
        slow = slow.next
    return slow.data
        
         
ll = Ll()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

# ll.remove_duplicates()
# ll.partition_list(4)
# print(kth_item_from_end(ll, 0))

# ll.tail.next = ll.head
# print(ll.has_loop())

# print(ll.find_middle_node().data)

# ll.pop()
# ll.prepend(7)
# ll.popfirst()
# print(ll.get(0).data)
# ll.set(1, 99)
# ll.insert(2, 78)
# ll.remove(1)
# ll.reverse()
# ll.reverse_between(0,2)

ll.print()
