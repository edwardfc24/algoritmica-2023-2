from kruskal import Kruskal


if __name__ == '__main__':
    kruskal = Kruskal()
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
    met = kruskal.apply_kruskal(nodes, edges)
    print(met)