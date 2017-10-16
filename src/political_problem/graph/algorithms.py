from .graph import Graph
from .graph_heap import GraphHeap

# The problem will be solved using betweenness algorithm that uses shortest path
# algorithm. In order to use shortest path, every edge should be converted as
# following:
#     w' = 100 - w 
#  Where:
#    w' is the new edge weight
#    w is the old edge weight
#
# More details can be found in documentation

def normalize_graph(graph):
    normalization_function = lambda weight: 100 - weight
    
    new_graph = graph.duplicate()
    new_graph.normalize_graph_weights(normalization_function)

    return new_graph

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
        
        for neighbor in graph.get_node_neighbors(actual_vertex):
            alternative_distance = graph_heap.get_distance(actual_vertex) +\
                graph.get_distance_between(actual_vertex, neighbor)

            if alternative_distance < graph_heap.get_distance(neighbor):
                graph_heap.update_vertex(neighbor, alternative_distance)
                previous[neighbor] = actual_vertex

    return previous

def calculate_betweenness(graph):
    betweeness = {
        node: 0
        for node in graph.get_nodes()
    }

    for node in graph.get_nodes():
        distances = shortest_path(graph, node)
        update_betweenness_distances(distances, betweeness)

    return betweeness        

def update_betweenness_distances(distances, betweeness):
    for destination_node in distances.keys():
        current_node = destination_node

        while current_node != None:
            betweeness[current_node] += 1
            current_node = distances[current_node] # Go to previous node