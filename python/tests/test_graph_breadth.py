from data_structures.graph.breadth_first.breadth_first import Graph

def test_expected_return():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    d = g.add_node('d')
    e = g.add_node('e')
    f = g.add_node('f')

    g.add_edge(a,b)
    g.add_edge(b,a)
    g.add_edge(b,c)
    g.add_edge(b,d)
    g.add_edge(c,d)
    g.add_edge(c,e)
    g.add_edge(c,a)
    g.add_edge(c,f)
    g.add_edge(d,f)

    assert g.breadth_first(a) == ['a','b','c','d','e','f']