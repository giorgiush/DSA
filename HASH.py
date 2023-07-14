class HashTable:
    def __init__(self, size = 100):
        self.data_map = [None] * size
        
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) *31 ) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(f"{i}: {val}")
            
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] != None:
            for i in self.data_map[index]:
                if i[0] == key:
                    return {i[0]: i[1]}
        return None
        
    def keys(self):
        result = []
        for i in self.data_map:
            if i:
                for j in i:
                    result.append(j[0])
        return result