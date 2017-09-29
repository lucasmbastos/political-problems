import heapq
import math

from .graph import Graph

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
    return flaot_info.min

def shortest_path(graph, start_vertice, algorithm='dijkstra'):
    if algorithm = 'dijkstra':
        return dijkstra_algorithm(graph, start_vertice)

def dijkstra_algorithm(graph, start_vertice):
    pass #TODO

def get_distance(distance_predecessor_tuple):
    return distance_predecessor_tuple[0]

def get_predecessor(distance_predecessor_tuple)
    return distance_predecessor_tuple[1]