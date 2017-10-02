import heapq

# Heap used in Dijkstra Algorith
class GraphHeap():
    
    def __init__(self, nodes):
        self.key_value_pair = {
            node: float("Inf")
            for node in nodes
        }

        self.key_heap = [float("Inf") for node in nodes]

        self.non_heap_distances = {}

    def push_vertex(self, node_id, distance):
        if node_id not in self.key_value_pair:
            heapq.heappush(self.key_heap, distance)
            self.key_value_pair[node_id] = distance

    def update_vertex(self, node_id, distance):
        print(self.key_value_pair)
        old_distance = self.key_value_pair[node_id]
        self.key_value_pair[node_id] = distance

        old_distance_position_in_key = self.key_heap.index(old_distance)
        del self.key_heap[old_distance_position_in_key]

        heapq.heappush(self.key_heap, distance)


    def pop_vertex(self):
        key_to_pop = heapq.heappop(self.key_heap)

        for node_id, distance in self.key_value_pair.items():
            if distance == key_to_pop:
                del self.key_value_pair[node_id]
                self.non_heap_distances[node_id] = distance
                return node_id

    def is_empty(self):
        return len(self.key_value_pair) == 0

    def get_distance(self, node_id):
        return {**self.key_value_pair, **self.non_heap_distances}[node_id]