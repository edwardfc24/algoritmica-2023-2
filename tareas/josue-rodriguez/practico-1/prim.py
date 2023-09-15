class Prim:
    
    def __init__(self) -> None:
        self.nodes = {}
        self.edges = []
        self.met = []
        self._weight = 2
        self._origin = 0
        self.destination = 1
        self.level = {}
    
    def sort_edges(self, edges):
        return sorted(edges, key=lambda edge: edge[self._weight])
    
    def initialize_data(self, node):
        self.nodes[node] = node
        self.level[node] = 0

    def find_root(self, node):
        if self.nodes[node] != node:
            self.nodes[node] = self.find_root(self.nodes[node])
        return self.nodes[node]
    
    def check_union(self, origin, destination):
        origin_root = self.find_root(origin)
        destination_root = self.find_root(destination)
        if origin_root != destination_root:
            if self.level[origin_root] > self.level[destination_root]:
                self.nodes[destination_root] = origin_root
            else:
                self.nodes[origin_root] = destination_root
                if self.level[origin_root] == self.level[destination_root]:
                    self.level[destination_root] += 1

    def apply_prim(self, nodes, edges):
        # Primero ingresar los nodos para formar el nivel 
        for node in nodes:
            self.initialize_data(node)
        
        # Inicializar la lista con el primer nodo
        visited_nodes = [nodes[0]]
        
        # Repetir hasta que se visiten todos los nodos
        while len(visited_nodes) < len(nodes):
            # Encontrar la arista más cercana a cualquier nodo en la lista
            min_edge = None
            for edge in edges:
                if edge[self._origin] in visited_nodes and edge[self.destination] not in visited_nodes:
                    if min_edge is None or edge[self._weight] < min_edge[self._weight]:
                        min_edge = edge
            
            # Verificar si se encontró una arista válida
            if min_edge is not None:
                # Agregar el nodo más cercano a la lista de nodos visitados
                visited_nodes.append(min_edge[self.destination])
                
                # Agregar la arista a la lista de aristas del árbol de expansión mínimo
                self.met.append(min_edge)
            else:
                # Si no se encontró ninguna arista válida, salir del bucle
                break
        
        return self.met
