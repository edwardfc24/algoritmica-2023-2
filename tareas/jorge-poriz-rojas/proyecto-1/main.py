from prim import Prim

if __name__ == '__main__':
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

    met = prim.apply_prim(nodes, edges, nodes[3])
    print(met)

    cost = prim.get_weight(met)

    print(cost)