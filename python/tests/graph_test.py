from data_structures.graph.graph import Graph,Vertex,Edge
import pytest

def test_create_vertex_pass():
    vertex = Vertex('a')
    expected = 'a'
    assert vertex.value == expected

def test_create_vertex_fail():
    vertex = Vertex('a')
    expected = 'b'
    assert vertex.value != expected

def test_add_vertex():
    g = Graph()
    expected = 'a'
    actual = g.add_node('a').value

    assert expected == actual

def test_add_edge_true():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    g.add_edge(a,b)

    assert True

def test_size():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')

    expected = 2
    actual = g.size()
    assert actual == expected

def test_get_nodes():
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    expected = ['a','b']
    actual = []
    [actual.append(item.value) for item in g.get_nodes()]
    assert actual == expected

def test_get_neigh():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    g.add_edge(a,b)
    actual = g.get_neighbors(a)
    expected = [('b', 1 )]
    assert actual == expected

def test_one_node_one_edge():
    g = Graph()
    a = g.add_node('a')
    g.add_edge(a,a)
    actual = g.get_neighbors(a)
    expected = [('a',1 )]

    assert actual == expected

def test_empty_graph():
    g = Graph()
    assert str(g) == 'Null'

def test_repr():
    g = Graph()
    g.add_node('a')
    g.add_node('b')

    actual = g
    expected = 'a : [],b : [] '
    assert str(actual) == expected
