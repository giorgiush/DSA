class Graph:
    def __init__(self):
        self.adjacency_list = {}
        
    def print_graph(self):
        for i in self.adjacency_list:
            print(f"{i} : {self.adjacency_list[i]}")
        
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def add_edge(self, vert1, vert2):
        if vert1 in self.adjacency_list and vert2 in self.adjacency_list:
            self.adjacency_list[vert1].append(vert2)
            self.adjacency_list[vert2].append(vert1)
            return True
        return False
    
    def remove_edge(self, vert1, vert2):
        if vert1 in self.adjacency_list and vert2 in self.adjacency_list:
            try:
                self.adjacency_list[vert1].remove(vert2)
                self.adjacency_list[vert2].remove(vert1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vert):
        if vert in self.adjacency_list:
            for i in self.adjacency_list[vert]:
                self.adjacency_list[i].remove(vert)
            del self.adjacency_list[vert]
            return True
        return False