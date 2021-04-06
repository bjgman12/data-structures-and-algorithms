from data_structures.graph.graph import Graph,Vertex,Edge



def DF(graph,root):
    visited = []
    ret_col = []

    def DF_Tool(graph,vertex):
        nonlocal visited
        nonlocal ret_col
        visited.push(vertex)
        ret_coll.append(vertex.value)

        for link in graph.get_neighbors(vertex):
            if link not in visited:
                DF_Tool(graph,link)
     
    DF_Tool(graph,root)

    return ret_col
