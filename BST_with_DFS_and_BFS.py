class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
        
class Tree:
    
    def __init__(self):
        self.root = None
        
    def _r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value < current_node.value:
            return self._r_contains(current_node.left, value)
        if value > current_node.value:
           return self._r_contains(current_node.right, value)
        if value == current_node.value:
            return True

    def _r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if current_node.value > value:
            current_node.left = self._r_insert(current_node.left, value)
        if current_node.value < value:
            current_node.right = self._r_insert(current_node.right, value)
        return current_node
        

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self._r_insert(self.root, value)
        # new = Node(value)
        # if not self.root:
        #     self.root = new
        #     return True
        # temp = self.root
        # while True:
        #     if value == temp.value:
        #         return False
        #     if value < temp.value:
        #         if not temp.left:
        #             temp.left = new
        #             return True
        #         temp = temp.left 
        #     else:
        #         if not temp.right:
        #             temp.right = new
        #             return True
        #         temp = temp.right
                
    def contains(self, value):
        return self._r_contains(self.root, value)
        # if not self.root:
        #     return False
        # temp = self.root
        # while temp.value != value:
        #     if value < temp.value:
        #         if not temp.left:
        #             return False
        #         temp = temp.left
        #     else:
        #         if not temp.right:
        #             return False
        #         temp = temp.right
        # return True
            
            
            
    def delete(self, value):
        self._r_delete(self.root, value)
        
        
    def _r_delete(self, current_node, value):
        if current_node == None:
            return None
        if current_node.value > value:
            current_node.left = self._r_delete(current_node.left, value)   
        if current_node.value < value:
            current_node.right = self._r_delete(current_node.right, value)
            
        if current_node.value == value:
            
            # if no children, gets replaced by None
            if current_node.left == None and current_node.right == None:
                return None
            
            #if only 1 child, gets replaced by it
            elif current_node.left == None:
                return current_node.right
            elif current_node.right == None:
                return current_node.left
            
            #if 2 children, current node swaps VALUES with lowest value NODE from right branch before deleting it
            else:
                min_val = self._min_val(current_node.right)
                current_node.value, min_val.value = min_val.value, current_node.value
                current_node.right = self._r_delete(current_node.right, min_val.value)
            
        return current_node
    
    
    #gets NODE with min value
    def _min_val(self, root):
        if root.left == None:
            return root
        return self._min_val(root.left)
    
    
    def BFS(self):
        if self.root == None:
            return None
        result = []
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
        return result
    
    
    def DFS_PreOrder(self):
        if self.root == None:
            return None
        result = []
        def traverse(current):
            result.append(current.value)
            if current.left != None:
                traverse(current.left)
            if current.right != None:
                traverse(current.right)
        traverse(self.root)
        return result
    
    
    def DFS_PostOrder(self):
        if self.root == None:
            return None
        result = []
        def traverse(current):
            if current.left != None:
                traverse(current.left)
            if current.right != None:
                traverse(current.right)
            result.append(current.value)
        traverse(self.root)
        return result
    
    
    def DFS_InOrder(self):
        if self.root == None:
            return None
        result = []
        def traverse(current):
            if current.left != None:
                traverse(current.left)
            result.append(current.value)
            if current.right != None:
                traverse(current.right)
        traverse(self.root)
        return result
    
    
    
tr = Tree()
tr.insert(47)
tr.insert(21)
tr.insert(76)
tr.insert(18)
tr.insert(27)
tr.insert(52)
tr.insert(82)

print(f"       {tr.root.value}")
print(f"   {tr.root.left.value}      {tr.root.right.value}")
print(f" {tr.root.left.left.value}  {tr.root.left.right.value}  {tr.root.right.left.value}  {tr.root.right.right.value}")

print(tr.BFS())
print(tr.DFS_PreOrder())
print(tr.DFS_PostOrder())
print(tr.DFS_InOrder())
