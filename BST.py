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
             
                    
                    
# tr = Tree()
# tr.insert(100)
# tr.insert(50)
# tr.insert(120)
# tr.insert(110)
# tr.insert(130)
# tr.insert(105)
# tr.insert(115)
# tr.insert(125)
# tr.insert(150)
# tr.insert(103)
# tr.insert(107)
# tr.insert(112)
# tr.insert(118)
# tr.insert(119)

# tr.delete(115)
# print(tr.root.right.left.right.right.value)
# #print(tr.contains(118))