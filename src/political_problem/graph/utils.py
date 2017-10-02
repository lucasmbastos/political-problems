from .graph import Graph

def read_graph_from_file(file_path):
    file_pointer = open(file_path, 'r')

    graph = Graph()
    
    for line in file_pointer:
        
        if line_is_not_valid(line):
            break

        node1, node2, weight = parse_line(line)

        graph.add_node(node1)
        graph.add_node(node2)
        graph.link_nodes(node1, node2, weight)

    file_pointer.close()
    return graph

def line_is_not_valid(line):
    return line == '0,0,0\n'

def parse_line(line):
    line_strips = line.strip().split(',')
    return [
        int(line_strips[0]), 
        int(line_strips[1]),
        float(line_strips[2]),
    ]