from kruskal import Kruskal
from prim import Prim

if __name__ == '__main__':
    kruskal = Kruskal()
    prim = Prim()
    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    edges = [
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
    
    met_kruskal = kruskal.apply_kruskal(nodes, edges)
    print("Kruskal:")
    print(met_kruskal)
    print(f'Peso: {kruskal.get_weight(met_kruskal)}')
    
    met_prim = prim.apply_prim(nodes, edges)
    print("Prim:")
    print(met_prim)
    print(f'Peso: {prim.get_weight(met_prim)}')
    
    
