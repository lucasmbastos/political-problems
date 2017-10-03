import operator

def print_output(vertex_betweenness_dict):
    vertex_sorted_by_id = sort_vertex_by_id(vertex_betweenness_dict)
    vertex_sorted_by_betweeness = sort_vertex_by_betweenness(
        vertex_sorted_by_id
    )

    sorted_betweenness = [x for x,y in vertex_sorted_by_betweeness]
    sorted_betweenness_as_string = list(
        map(lambda x: str(x), sorted_betweenness)
    )

    print(','.join(sorted_betweenness_as_string))

def sort_vertex_by_id(vertex_betweenness_dict):
    return sorted(vertex_betweenness_dict.items(), key=operator.itemgetter(0))

def sort_vertex_by_betweenness(vertex_betweenness_list):
    return sorted(
        vertex_betweenness_list, 
        key=operator.itemgetter(1),
        reverse=True
    )