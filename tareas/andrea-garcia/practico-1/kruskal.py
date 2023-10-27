class Kruskal:
    def __init__(self):
        self.nodes = {}
        #self.edges = []
        self.met = []
        #self.aux = []
        self._weight = 2  #atributo privado de la clase
        #self._origin = 0
        #self.destination = 1
        self.level = {}
    
    def sort_edges(self, edges):
        return sorted(edges, key=lambda edge: edge[self._weight])    
    
    def initialize_data(self, node):
        self.nodes[node] = node
        self.level[node] = 0
        
    def find_root(self, node):
        #buscar el nodo raiz de la arista, si el valor no es el mismo, buscamos sobre el padre
        if self.nodes[node] != node:
            self.nodes[node] = self.find_root(self.nodes[node])
            #aqui hacemos recursivo el metodo para encontrar el nodo del nivel 0
        return self.nodes[node]
    
    def check_union(self, origin, destination): #para revisar si añadiendo un vertice entre origin y destination crearia un ciclo en el mst 
        # Paso 1: Encontrar los nodos raiz de cada uno
        origin_root = self.find_root(origin)
        destination_root = self.find_root(destination)
        # Paso 2: Avanzar si y solo si los nodos raiz son diferentes 
        if origin_root != destination_root:  #si comparten padre, formaran un ciclo
            # Tratamos de guardar siempre el de menor nivel relacionado a uno de mayor
            if self.level[origin_root] > self.level[destination_root]:
                #si el nivel del origen es mayor al de destino, el destino se vuelve hijo del nodo origen 
                self.nodes[destination_root] = origin_root
            else:
                # el nodo origen se vuelve padre del nodo destino
                self.nodes[origin_root] = destination_root
                # Si los niveles son iguales, se cambia el nivel del ultimo nodo guardado
                if self.level[origin_root] == self.level[destination_root]:
                    self.level[destination_root] += 1
            return True #no se forma ciclo
        return False #se forma ciclo
    
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
            # Aqui viene la logica del pseudo Codigo
            if self.check_union(origin, destination):
                self.met.append(edge)
            # if self.find_root(origin) != self.find_root(destination):
            #     self.check_union(origin, destination)
            #     self.met.append(edge)
        return self.met
    
    def get_weight(self, met):
        weight = 0
        for item in met:
            weight += item[2]
        return weight
   
    