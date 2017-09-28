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