import operator

from political_problem.graph import read_graph_from_file
from political_problem.graph import normalize_graph
from political_problem.graph import calculate_betweenness
from political_problem.utils import print_output

graph = read_graph_from_file("../examples/Ex4.txt")
normalized_graph = normalize_graph(graph)

vertex_betweenness_dict = calculate_betweenness(normalized_graph)

print_output(vertex_betweenness_dict)
