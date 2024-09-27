from prim import Prim

if __name__ == '__main__':
    prim = Prim()
    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    edges = [
        ('a', 'b', 8),
        ('b', 'c', 10),
        ('b', 'e', 4),
        ('c', 'd', 5),
        ('d', 'e', 7),
        ('d', 'g', 11),
        ('e', 'f', 2),
        ('f', 'g', 12),
        ('f', 'h', 14),
        ('f', 'i', 6),
        ('f', 'j', 9),
        ('g', 'h', 20),
        ('h', 'i', 17),
        ('i', 'j', 3)
    ]

    tree = prim.apply_prim(nodes, edges)
    print(tree)
