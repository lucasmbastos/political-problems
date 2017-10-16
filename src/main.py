import operator
import sys

from political_problem import read_graph_from_file
from political_problem import normalize_graph
from political_problem import shortest_path
from political_problem import calculate_betweenness

graph = read_graph_from_file(sys.argv[1])
normalized_graph = normalize_graph(graph)

betweenness = calculate_betweenness(normalized_graph)

# Sorting
sorted_betweenness = sorted(betweenness.items(), key=operator.itemgetter(1))
sorted_betweenness = [x for x,y in sorted_betweenness]
sorted_betweenness.reverse()

#Print result to file
output_fp = open(sys.argv[2], 'w')
output_list = map(str, sorted_betweenness) # Convert to str
output_fp.write(",".join(output_list))
output_fp.write("\n")
output_fp.close()