from prim import PrimMST  

if __name__ == "__main__":
    prim_mst = PrimMST()
    nodes = ['A', 'B', 'C', 'D', 'E','F','G']
    edges = [('A', 'B', 7),
            ('A', 'D', 5),
            ('D', 'F', 6),
            ('D', 'B', 9),
            ('D', 'E', 15),
            ('F', 'E', 8),
            ('G', 'E', 9),
            ('F', 'G', 11),
            ('E', 'C', 5),
            ('C', 'B', 8),
            ('E', 'B', 7)
            ]

    print("Prim MST:")
    print(prim_mst.apply_prim(nodes, edges))

