import math

from .graph import Graph
from .graph_heap import GraphHeap

# The problem will be solved using betweenness algorithm that uses shortest path
# algorithm. In order to use shortest path, every edge should be converted as
# following:
#     w' = log(100 - w + C)
#  Where:
#    w' is the new edge weight
#    w is the old edge weight
#    C is approximately 2.23e-308. A very low number used just to avoid log(0)
# situation.

# More details can be found in documentation
def normalize_graph(graph):
    min_float = get_min_float()
    
    normalization_function = lambda weight: math.log(100 - weight + min_float)
    
    new_graph = graph.duplicate()
    new_graph.normalize_graph_weights(normalization_function)

    return new_graph

def get_min_float():
    from sys import float_info
    return float_info.min

def shortest_path(graph, source_vertex, algorithm='dijkstra'):
    if algorithm == 'dijkstra':
        return dijkstra_algorithm(graph, source_vertex)

def dijkstra_algorithm(graph, source_vertex):
    nodes = graph.get_nodes()

    previous = {source_vertex: None}

    graph_heap = GraphHeap(nodes)
    graph_heap.update_vertex(source_vertex, 0)

    while not graph_heap.is_empty():
        actual_vertex = graph_heap.pop_vertex()

        print("actual")
        print(actual_vertex)
        for neighbor in graph.get_node_neighbors(actual_vertex):
            alternative_distance = graph_heap.get_distance(actual_vertex) +\
                graph.get_distance_between(actual_vertex, neighbor)

            if alternative_distance < graph_heap.get_distance(neighbor):
                graph_heap.update_vertex(neighbor, alternative_distance)
                previous[neighbor] = actual_vertex

    return previous