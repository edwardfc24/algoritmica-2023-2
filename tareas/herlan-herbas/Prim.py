class Prim:
    
    def __init__(self) -> None:
        self.nodes = {}
        self.edges = []
        self.met = []
        self._weight = 2
        self._origin = 0
        self.destination = 1
    
    def sort_edges(self, edges):
        return sorted(edges, key=lambda edge: edge[self._weight])
    
    def initialize_data(self, node):
        self.nodes[node] = None

    def apply_prim(self, nodes, edges):
        for node in nodes:
            self.initialize_data(node)
        
        # Elegir un nodo inicial arbitrario
        start_node = nodes[0]
        self.nodes[start_node] = start_node
        
        while len(self.met) < len(nodes) - 1:
            eligible_edges = []
            
            for edge in edges:
                origin, destination, weight = edge
                
                if self.nodes[origin] is not None and self.nodes[destination] is None:
                    eligible_edges.append(edge)
                elif self.nodes[destination] is not None and self.nodes[origin] is None:
                    eligible_edges.append(edge)
            
            if not eligible_edges:
                break
            
            # Elegir la arista de menor peso entre los nodos elegibles
            min_edge = min(eligible_edges, key=lambda edge: edge[self._weight])
            origin, destination, weight = min_edge
            
            if self.nodes[origin] is None:
                self.nodes[origin] = origin
            else:
                self.nodes[destination] = destination
            
            self.met.append(min_edge)
        
        return self.met
    
    def get_met_cost(self, met=None):
        cost = 0
        if met:
            for edge in met:
                cost += edge[self._weight]
        else:
            for edge in self.met:
                cost += edge[self._weight]
        return cost

