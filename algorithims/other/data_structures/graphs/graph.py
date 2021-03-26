from typing import List, Any, Optional

class Vertex:
    value: int
    in_edges: List[Any]
    out_edges: List[Any]

    def __init__(self, value: int) -> None:
        self.value = value
        self.in_edges = []
        self.out_edges = []


class Edge:
    from_vertex: Optional[Vertex]
    to_vertex: Optional[Vertex]
    cost: int

    def __init__(self, from_vertex: Vertex, to_vertex: Vertex, cost = 1) -> None:
        self.from_vertex = from_vertex
        from_vertex.out_edges.append(self)
        self.to_vertex = to_vertex
        to_vertex.in_edges.append(self)
        self.cost = cost

    def destroy(self):
        self.from_vertex.out_edges = [edge for edge in self.from_vertex.out_edges if edge is not self]
        self.to_vertex.in_edges = [edge for edge in self.to_vertex.in_edges if edge is not self]
        self.from_vertex = None
        self.to_vertex = None
