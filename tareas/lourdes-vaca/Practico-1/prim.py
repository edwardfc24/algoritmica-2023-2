import sys

class Prim:

    def __init__(self, vertices, edges, nodes):
        self.vertices = vertices
        self.edges = edges
        self.nodes = nodes
        self.MST = []
        self.total_weight = 0  

    def printSolution(self):
        print("Arista | Peso")
        for s, d, w in self.MST:
            print("%s - %s : %s" % (s, d, w))
        print("Peso total del árbol de expansión mínima", self.total_weight)

    def prim(self):
        visited = [False] * self.vertices
        visited[0] = True
        edgeNum = 0
        while edgeNum < self.vertices - 1:
            minimum = sys.maxsize
            for i in range(self.vertices):
                if visited[i]:
                    for j in range(self.vertices):
                        if (not visited[j]) and self.edges[i][j]:
                            if self.edges[i][j] < minimum:
                                minimum = self.edges[i][j]
                                s = i
                                d = j
            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            self.total_weight += self.edges[s][d]  
            visited[d] = True
            edgeNum += 1
        self.printSolution()

nodes = ['a', 'b', 'c', 'd', 'e']
edges = [
    [1, 10, 4, 3,5],
    [0, 5, 15, 20,1],
    [20, 2, 30, 7, 6],
    [0, 5, 15, 0, 8],
    [8, 7, 9, 20,10]
]

g = Prim(5, edges, nodes)
g.prim()
