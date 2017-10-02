import operator

from political_problem import read_graph_from_file
from political_problem import normalize_graph
from political_problem import shortest_path
from political_problem import calculate_betweenness

graph = read_graph_from_file("../examples/Ex5.txt")
normalized_graph = normalize_graph(graph)

# TODO -- in case of draw, output must be ordered by key

betweenness = calculate_betweenness(normalized_graph)
sorted_betweenness = sorted(betweenness.items(), key=operator.itemgetter(1))
sorted_betweenness = [x for x,y in sorted_betweenness]
sorted_betweenness.reverse()

print(betweenness)
print(sorted_betweenness)