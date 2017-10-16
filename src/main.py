import operator
import sys

from political_problem.graph import read_graph_from_file
from political_problem.graph import normalize_graph
from political_problem.graph import calculate_betweenness
from political_problem.utils import print_output

graph = read_graph_from_file(sys.argv[1])
normalized_graph = normalize_graph(graph)

betweenness = calculate_betweenness(normalized_graph)

# Sorting
output_fp = open(sys.argv[2], 'w')
print_output(vertex_betweenness_dict, output_fp)
output_fp.close()