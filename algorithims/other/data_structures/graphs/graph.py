from typing import List, Any

class Vertex:
    value: int
    in_edges: List[Any]
    out_edges: List[Any]

    def __init__(self, value: int) -> None:
        self.value = value
        self.in_edges = []
        self.out_edges = []


class Edge:
    def initialize(self, from_vertex: Vertex, to_vertex: Vertex, cost = 1) -> None:
        pass

    def destroy(self):
        pass