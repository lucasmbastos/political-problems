class Node():
    
    def __init__(self, id=None, neighbors=None):
        self.id = id

        if neighbors == None:
            self.neighbors = {}
        else:
            self.neighbors = neighbors

    def add_neighbors(self, neighbors):
        self.neighbors = {**self.neighbors, **neighbors}

    def add_neighbor(self, id, weight):
        self.add_neighbors({id:weight})

    def get_neighbors_as_list(self):
        return list(self.neighbors.keys())

    def normalize_weights(self, normalization_function):
        self.add_neighbors = {
            neighbor: normalization_function(weight)
            for neighbor, weight in self.neighbors.items()
        }

    def get_weight(self, node_id):
        return self.neighbors[node_id]