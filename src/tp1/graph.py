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


def read_graph_from_file(file_path):
    file_pointer = open(file_path, 'r')

    graph = Graph()
    for line in file_pointer:
        # node1, node2, weight = line.split(',')
        print(line)
        
        graph.add_node(node1)
        graph.add_node(node2)
        graph.link_nodes(node1, node2, weight)

    file_pointer.close()
    return graph