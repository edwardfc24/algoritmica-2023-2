class PrimMST:
    def __init__(self) -> None:
        self.met_prim = []
        self._weight = 2

    def apply_prim(self, nodes, edges):
        included_nodes = set()
        initial_node = nodes[0]
        included_nodes.add(initial_node)

        while len(included_nodes) < len(nodes):
            min_edge = None
            for edge in edges:
                origin, destination, weight = edge
                if (origin in included_nodes and destination not in included_nodes) or (destination in included_nodes and origin not in included_nodes):
                    if min_edge is None or weight < min_edge[self._weight]:
                        min_edge = edge

            if min_edge is not None:
                origin, destination, weight = min_edge
                self.met_prim.append(min_edge)
                included_nodes.add(origin)
                included_nodes.add(destination)

        return self.met_prim 










