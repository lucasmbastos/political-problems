from political_problem import read_graph_from_file
from political_problem import normalize_graph
from political_problem import shortest_path

graph = read_graph_from_file("../examples/Ex1.txt")
normalized_graph = normalize_graph(graph)
print(graph.nodes)

print(shortest_path(graph, 0))