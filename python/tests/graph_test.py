from data_structures.graph.graph import Graph,Vertex,Edge, DF
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

# def test_expected_output():
#     g = Graph()
#     a = g.add_node('a')
#     b = g.add_node('b')
#     c = g.add_node('c')
#     d = g.add_node('d')
#     e = g.add_node('e')
#     f = g.add_node('f')
#     nodeg = g.add_node('g')
#     h = g.add_node('g')

#     g.add_edge(a,b)
#     g.add_edge(a,d)
#     g.add_edge(b,d)
#     g.add_edge(b,c)
#     g.add_edge(c,nodeg)
    
#     g.add_edge(d,e)
#     g.add_edge(d,h)
#     g.add_edge(d,f)

#     actual = DF(g,g.root)
#     expected = ['a','b','c','g','d','e','h','f']
#     assert actual == expected
    
