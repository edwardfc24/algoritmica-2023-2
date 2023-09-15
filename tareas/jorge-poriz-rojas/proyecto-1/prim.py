"""
    Class to obtain minimum spanning tree using Prim algorithm
"""


class Prim:
    def __init__(self) -> None:
        self.nodes = {}
        self.edges = []
        self.met = []
        self._weight = 2
        self.level = {}

    def sort_edges(self, edges):
        return sorted(edges, key=lambda edge: edge[self._weight])

    def initialize_data(self, node):
        self.nodes[node] = node
        self.level[node] = 0

    def find_root(self, node):
        if self.nodes[node] != node:
            self.nodes[node] = self.find_root(self.nodes[node])
        return self.nodes[node]

    def check_union(self, origin, destination):
        origin_root = self.find_root(origin)
        destination_root = self.find_root(destination)

        if origin_root != destination_root:
            if self.level[origin_root] > self.level[destination_root]:
                self.nodes[destination_root] = origin_root
            else:
                self.nodes[origin_root] = destination_root
                if self.level[origin_root] == self.level[destination_root]:
                    self.level[destination_root] += 1
            return True
        return False
    
    def free_edges(self, edges, node_first):
        for edge in edges:
            if edge not in self.edges and edge not in self.met:
                if node_first in edge:
                    self.edges.append(edge)
        self.edges = self.sort_edges(self.edges)
        return self.edges

    def apply_prim(self, nodes, edges, node_first):
        for node in nodes:
            self.initialize_data(node)
        counter = 0
        while len(self.met) < len(nodes) - 1:
            free_edges = self.free_edges(edges, node_first)
            if not free_edges:
                break
            min_edge = free_edges[counter] 
            origin, destination, weight = min_edge
            if self.check_union(origin, destination):
                self.met.append(free_edges[counter])
                self.edges.pop(counter)
                self.free_edges(edges, origin)
                self.free_edges(edges, destination)
                counter = 0
            else:
                counter += 1
        return self.met

    def get_weight(self, met=None):
        cost = 0
        if met:
            for edge in met:
                cost += edge[self._weight]
        else:
            for edge in self.met:
                cost += edge[self._weight]
        return cost
    
