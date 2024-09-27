class Prim:

    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.tree = []
        self._weight = 2

    def sort_edges(self, edges):
        return sorted(edges, key=lambda edge: edge[self._weight])

    def initialize_data(self, node):
        self.nodes[node] = node

    def apply_prim(self, nodes, edges):
        for node in nodes:
            self.initialize_data(node)
        self.edges = edges

        initial_node = nodes[0]
        connected_nodes = set([initial_node])

        while len(connected_nodes) < len(nodes):
            sorted_edges = self.sort_edges(self.edges)

            for edge in sorted_edges:
                origin, destination, weight = edge
                if origin in connected_nodes and destination not in connected_nodes:
                    self.tree.append(edge)
                    connected_nodes.add(destination)
                    break

        return self.tree
