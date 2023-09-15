"""
Este archivo es la implementación del algortimo de kruskal y funciona bajo los siguientes
parámetros:
- Una lista de Nodos ['a', 'b', 'c' ...]
- Una lista de tuplas que representan aristas [('a', 'd', 5), (inicio, fin,  peso)]
"""
class Kruskal:
    
    def __init__(self) -> None:
        self.nodes = {}
        self.edges = []
        self.met = []
        self._weight = 2
        self._origin = 0
        self.destination = 1
        self.level = {}
        self.total_weight = 0

    def sort_edges(self, edges):
        # for index in range(0, len(edges) - 1):
        #     aux = edges[index]
        #     if edges[index + 1][2] < edges[index][2]:
        #         edges[index] = edges[index + 1]
        #         edges[index + 1] = aux
        # return edges
        return sorted(edges, key=lambda edge: edge[self._weight])

    def initialize_data(self, node):
        self.nodes[node] = node
        self.level[node] = 0

    def find_root(self, node):
        # Buscamos el nodo raiz de la arista, si el valor no es el mismo
        # buscamos sobre el padre
        if self.nodes[node] != node:
            self.nodes[node] = self.find_root(self.nodes[node])
            # Acá hacemos recursivo el método para encontrar el nodo de nivel 0
        return self.nodes[node]

    def check_union(self, origin, destination):
        # 1er paso: Encontrar los nodos raíz de cada uno
        origin_root = self.find_root(origin)
        destination_root = self.find_root(destination)
        # 2do paso: Avanzar si y solo si los nodos raiz son difrentes
        if origin_root != destination_root:
            # Tratamos de guardar siempre el de menor nivel relacionado
            # a uno de mayor
            if self.level[origin_root] > self.level[destination_root]:
                self.nodes[destination_root] = origin_root
            else:
                self.nodes[origin_root] = destination_root
                # Si los niveles son iguales, se cambia el nivel del último nodo guardado
                if self.level[origin_root] == self.level[destination_root]:
                    self.level[destination_root] += 1
            return True
        return False


    def apply_kruskal(self, nodes, edges):
        # Primero ingresar los nodos para formar el nivel
        for node in nodes:
            self.initialize_data(node)
        # Ordenamos las aristas de menor a mayor peso
        sorted_edges = self.sort_edges(edges)
        # Una vez ordenado, arista por arista verifico la union
        for edge in sorted_edges:
            # Obtener los valores de la tupla
            origin, destination, weight = edge
            # Aquí viene la lógica del pseudo código
            if self.check_union(origin, destination):
                self.met.append(edge)
                self.total_weight += weight
        return self.met, self.total_weight
