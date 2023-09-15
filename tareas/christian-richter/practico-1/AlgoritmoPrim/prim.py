""""
algoritmo de prim para generar arboles de costo minimo, recibe como parametros
los nodos y las aristas, las aristas deben tener la siguiente estructura
('a', 'b', 7) donde el primer elemento es el nodo origen, el segundo el nodo destino
y el tercero el peso de la arista

el algoritmo funciona de la siguiente manera:

1. Se elige un nodo inicial, se puede elegir cualquiera
2. Se buscan todas las aristas que conectan un nodo en el arbol con uno fuera del arbol
3. Se toma la arista de menor peso y se agrega al arbol verificando que no haya ningun ciclo
4. Se agrega el nodo al conjunto de nodos del arbol
5. Se repite el paso 2 hasta que todos los nodos esten en el arbol


"""


class Prim:

    def __init__(self) -> None:
        self.nodes = set()
        self.edges = []
        self.met = []
        self._weight = 2
        self._origin = 0
        self.destination = 1
        self.level = {}
        self.total_weight = 0

    def sort_edges(self, edges):
        return sorted(edges, key=lambda edge: edge[self._weight])

    def initialize_data(self, node):
        self.nodes.add(node)

    def apply_prim(self, nodes, edges):
        # nodo inicial, se puede elegir cualquiera
        start_node = nodes[0]
        self.nodes.add(start_node)

        while len(self.nodes) < len(nodes):
            # Buscamos todas las aristas que conectan un nodo en el árbol con uno fuera del árbol
            candidate_edges = [edge for edge in edges if
                               (edge[self._origin] in self.nodes) != (edge[self.destination] in self.nodes)]

            if not candidate_edges:
                break  # aquí se puede lanzar una excepción en caso de que no haya aristas candidatas, en otras
                # palabras, si el grafo no es conexo

            # primero ordenamos las aristas por peso
            candidate_edges.sort(key=lambda edge: edge[self._weight])
            # tomamos la arista de menor peso, verificando que no haya ningún ciclo dentro del árbol, es decir, que
            # el arbol llege a todos los nodos sin repetir aristas
            self.total_weight += candidate_edges[0][self._weight]
            min_edge = candidate_edges[0]
            self.met.append(min_edge)
            # Agregamos el nodo al conjunto de nodos del árbol, si el nodo origen ya está en el árbol, agregamos el
            # nodo destino, si el nodo destino ya está en el árbol, agregamos el nodo origen, si ninguno de los dos
            # está en el árbol, agregamos el nodo origen
            # para evitar los ciclos en el árbol de costo mínimo se verifica que el nodo origen o el nodo destino
            # no estén en el árbol
            if min_edge[self._origin] in self.nodes:
                self.nodes.add(min_edge[self.destination])
            else:
                self.nodes.add(min_edge[self._origin])

        return self.sort_edges(self.met), self.total_weight
