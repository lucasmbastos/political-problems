from .node import Node

class Graph:

    def __init__(self):
        self.nodes = {}

    def add_node(self, id, neighbors=None):
        if id not in self.nodes:
            self.nodes[id] = Node(id, neighbors)

    def link_nodes(self, node1, node2, weight):
        self.nodes[node1].add_neighbor(node2, weight)
        self.nodes[node2].add_neighbor(node1, weight)

    def normalize_graph_weights(self, normalization_function):
        self.nodes = {
            node_id: node_object.normalize_weights(normalization_function)
            for node_id, node_object in self.nodes.items()
        }

    def duplicate(self):
        from copy import deepcopy
        return deepcopy(self)

    def get_nodes(self):
        return list(self.nodes.keys())