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
        for node in self.nodes.values():
            node.normalize_weights(normalization_function)

    def get_nodes(self):
        return list(self.nodes.keys())
        
    def duplicate(self):
        from copy import deepcopy
        return deepcopy(self)

    def get_node_neighbors(self, node_id):
        return self.nodes[node_id].get_neighbors_as_list()

    def get_distance_between(self, node_id1, node_id2):
        return self.nodes[node_id1].get_weight(node_id2)