import random

class Prim:
    def __init__(self) -> None:
        self.nodes = {} #diccionario vacio guardando un nodo clave valor para verificar si un nodo se visito o no
        self.edges = [] #Lista vacia que contendra las aristas del grafo
        self.met = [] #Lista que contendra el M.E.T
        self._weight = 2 #
        self._origin = 0
        self.destination = 1
        self.level = {} #seguimiento del nivel de cada nodo

    def initialize_data(self, node):
        self.nodes[node] = node
        self.level[node] = 0

    def obtenerAristas(self, nodo, edges):
        # Obtener todas las aristas que están conectadas al nodo dado
        return [edge for edge in edges if edge[self._origin] == nodo or edge[self.destination] == nodo]

    def obtenerAristaMenor(self, aristas):
        # Devolver la arista de menor peso en la lista de aristas
        return min(aristas, key=lambda edge: edge[self._weight])

    def agregarAlArbol(self, arista):
        # Agregar una arista al árbol de expansión mínima
        self.met.append(arista)
        # También agregar los nodos de la arista al conjunto de nodos
        self.nodes[arista[self._origin]] = arista[self._origin]
        self.nodes[arista[self.destination]] = arista[self.destination]

    def apply_prim(self, nodes, edges):
        # Inicializar estructuras de datos
        for node in nodes:
            self.initialize_data(node)

        # Elegir un nodo aleatorio como punto de inicio
        random_node = random.choice(nodes)
        visited_nodes = {random_node}
        unvisited_nodes = set(nodes) - visited_nodes
        #mientras haya nodo sin visitar
        while unvisited_nodes:
            # Obtener todas las aristas conectadas a los nodos visitados
            connected_edges = []# Lista que contendra las aristas conectadas 
            for visited_node in visited_nodes:
                connected_edges.extend(self.obtenerAristas(visited_node, edges))

            # Filtrar las aristas que conducen a nodos no visitados
            valid_edges = [edge for edge in connected_edges if edge[self._origin] in unvisited_nodes or edge[self.destination] in unvisited_nodes]

            if valid_edges:
                # Elegir la arista de menor peso
                menor_arista = self.obtenerAristaMenor(valid_edges)
                nodo_origen, nodo_destino, peso = menor_arista
                # Agregar la arista al árbol de expansión mínima
                self.agregarAlArbol(menor_arista)
                #Agregamos el nodo origen y destino a los nodos visitados
                visited_nodes.add(nodo_origen)
                visited_nodes.add(nodo_destino)
                unvisited_nodes = set(nodes) - visited_nodes #actualizar nodos no visitados
            else:
                break

        return self.met
