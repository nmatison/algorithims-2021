from typing import List
from pytest import mark
from algorithims.other.data_structures.graphs.graph import Vertex, Edge
from algorithims.other.data_structures.graphs.topological_sort.khans_algorithm import topological_sort

v1: Vertex = Vertex("Wash Markov")
v2: Vertex = Vertex("Feed Markov")
v3: Vertex = Vertex("Dry Markov")
v4: Vertex = Vertex("Brush Markov")
v5: Vertex = Vertex("Cuddle Markov")
v6: Vertex = Vertex("Walk Markov")
v7: Vertex = Vertex("Teach Markov")
v8: Vertex = Vertex("Worship Markov")


class TestKhansAlgorithm:

    def __init__(self):
        self.vertices: List[Vertex] = [
            v1, v2, v3, v4, v5, v6, v7, v8
        ]

    @mark.parametrize(
        'description, edges, solutions',
        [   (
            'it sorts the vertices correctly', [
                Edge(v1, v2),
                Edge(v1, v3),
                Edge(v2, v4),
                Edge(v3, v4),
                Edge(v2, v5),
                Edge(v4, v6),
                Edge(v5, v6),
                Edge(v6, v7),
                Edge(v7, v8),
            ],
            [
                [v1.value, v2.value, v3.value, v4.value, v5.value, v6.value, v7.value, v8.value],
                [v1.value, v2.value, v3.value, v5.value, v4.value, v6.value, v7.value, v8.value],
                [v1.value, v3.value, v2.value, v4.value, v5.value, v6.value, v7.value, v8.value],
                [v1.value, v3.value, v2.value, v5.value, v4.value, v6.value, v7.value, v8.value],
                [v1.value, v2.value, v5.value, v3.value, v4.value, v6.value, v7.value, v8.value]
            ]
        ),
            ('if a solution is not possible (cyclical graph), then it returns []', [
                Edge(v1, v2),
                Edge(v1, v3),
                Edge(v2, v4),
                Edge(v3, v4),
                Edge(v2, v5),
                Edge(v4, v6),
                Edge(v5, v6),
                Edge(v6, v7),
                Edge(v7, v8),
                Edge(v8, v2),
            ], [[]])
        ]
    )
    def test__khans_algorithm(self, description: str, edges: List[Edge], solutions: List[List[Vertex]]) -> None:
        actual: List[Vertex] = topological_sort(self.vertices)
        actual_values = [vertex.value for vertex in actual]

        assert actual_values in solutions
