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

    def test__edge__init(self) -> None:
        from_vertex: Vertex = Vertex(2)
        to_vertex: Vertex = Vertex(3)
        edge = Edge(from_vertex, to_vertex)

        assert edge.from_vertex == from_vertex
        assert edge.to_vertex == to_vertex
        assert edge.cost == 1
        assert from_vertex.out_edges[0] == edge
        assert to_vertex.in_edges[0] == edge

    def test__edge__destroy(self) -> None:
        from_vertex: Vertex = Vertex(2)
        to_vertex: Vertex = Vertex(3)
        edge = Edge(from_vertex, to_vertex)

        edge.destroy()

        assert edge.from_vertex is None
        assert edge.to_vertex is None
        assert edge not in from_vertex.out_edges
        assert edge not in to_vertex.in_edges

