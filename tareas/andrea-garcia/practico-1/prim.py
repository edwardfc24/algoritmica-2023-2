class Prim:
    def __init__(self):
        self.nodes = {}  
        self.met = []
        self._weight = 2  
    
    def sort_edges(self, edges):
        return sorted(edges, key=lambda edge: edge[self._weight])
    
    def add_node(self, node):
        self.nodes[node] = True 
    
    def apply_prim(self, nodes, edges):
        self.add_node(nodes[0])  
        
        while len(self.met) < len(nodes) - 1:
            candidate_edges = []
            for edge in edges:
                #condicion para asegurar que solo uno de los nodos del vertice ya se encuentra en la lista de nodos visitados
                if(edge[0] in self.nodes) ^ (edge[1] in self.nodes):
                    candidate_edges.append(edge)
                    
            sorted_candidates = self.sort_edges(candidate_edges)
            
            if not sorted_candidates:
                #el ciclo se rompe si no hay mas candidatos
                break  
            
            min_edge = sorted_candidates[0]
            self.met.append(min_edge)
            #se añaden ambos nodos del vertice a la lista de nodos visitados
            self.add_node(min_edge[0])
            self.add_node(min_edge[1])
        
        return self.met
    
    def get_weight(self, met):
        weight = 0
        for item in met:
            weight += item[2]
        return weight
