class Prim:
    
    def __init__(self) -> None:
        self.nodos_mst = set()
        self.aristas_mst = []
    
    def ordenar_aristas(self, aristas):
        return sorted(aristas, key=lambda arista: arista[2])
    
    def aplicar_prim(self, nodos, aristas):
        nodo_inicial = nodos[0]  # Empezar con el primer nodo
        self.nodos_mst.add(nodo_inicial)
        
        while len(self.nodos_mst) < len(nodos):
            arista_minima = None
            for arista in aristas:
                origen, destino, peso = arista
                if origen in self.nodos_mst and destino not in self.nodos_mst:
                    if arista_minima is None or peso < arista_minima[2]:
                        arista_minima = arista
            
            if arista_minima:
                self.aristas_mst.append(arista_minima)
                self.nodos_mst.add(arista_minima[1])  # Agregar el nodo destino al MST
        
        return self.aristas_mst

if __name__ == '__main__':
    prim = Prim()
    nodos = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    aristas = [
        ('a', 'b', 7),
        ('b', 'c', 8),
        ('c', 'e', 5),
        ('e', 'g', 9),
        ('g', 'f', 11),
        ('f', 'e', 8),
        ('d', 'f', 6),
        ('d', 'e', 15),
        ('d', 'a', 5),
        ('d', 'b', 9),
        ('b', 'e', 7)
    ]
    arbol_minimo = prim.aplicar_prim(nodos, aristas)
    print(arbol_minimo)