from pytest import fixture
from algorithims.other.data_structures.graphs.graph import Vertex, Edge


class TestVertex:
    def test__init__stores_value(self) -> None:
        vertex = Vertex(7)

        assert vertex.value == 7

    def test__init__initaites_in_edges_as_an_empty_array(self) -> None:
        vertex = Vertex(7)

        assert vertex.in_edges == []

    def test__init__initaites_out_edges_as_an_empty_array(self) -> None:
        vertex = Vertex(7)

        assert vertex.out_edges == []


class TestEdge:
    pass