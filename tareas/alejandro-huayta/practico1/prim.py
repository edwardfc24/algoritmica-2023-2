import sys


class prim:

    def __init__(self, vertice, edges, nodes):
        self.vertice = vertice
        self.edges = edges
        self.nodes = nodes
        self.MST = []

    def printSolucion(self):
        print("Edge : Weight")
        for s, d, w in self.MST:
            print("%s - %s : %s" % (s, d, w))

    def prim(self):
        visita = [0]*self.vertice
        edgeNum = 0
        visita[0] = True
        while edgeNum < self.vertice - 1:
            minimo = sys.maxsize
            for i in range(self.vertice):
                if visita[i]:
                    for j in range(self.vertice):
                        if ((not visita[j]) and self.edges[i][j]):
                            if minimo > self.edges[i][j]:
                                minimo = self.edges[i][j]
                                s = i
                                d = j
            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            visita[d] = True
            edgeNum += 1
        self.printSolucion()


nodes = ['a', 'b', 'c', 'd', 'e']
edges = [
    [0, 10, 20, 0, 0],
    [10, 0, 30, 5, 0],
    [20, 30, 0, 15, 6],
    [0, 5, 15, 0, 8],
    [0, 10, 20, 0, 0],
    [10, 0, 30, 5, 0],
    [20, 30, 0, 15, 6],
    [0, 5, 15, 0, 8]
]
g = prim(5, edges, nodes)
g.prim()