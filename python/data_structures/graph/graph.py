from .. import d





class Graph:

    def __init__(self):
        self._adjacency_list = {}
        self.root = None

    def add_node(self,value):
        v = Vertex(value)
        if not self._adjacency_list:
            self.root = v
        self._adjacency_list[v] = []
        return v

    def add_edge(self,origin,dest,weight = 1):
        if origin not in self._adjacency_list:
            raise KeyError('Origin not in Graph')
        if dest not in self._adjacency_list:
            raise KeyError('Destination not in Graph')

        edge = Edge(dest,weight)

        adjs = self._adjacency_list[origin]
        adjs.append(edge)
        origin.edges.append((edge.vertex.value,edge.weight))
        return edge

    def get_nodes(self):
        ret_collection = []
        [ret_collection.append(item) for item in self._adjacency_list.keys()]
        return ret_collection

    def size(self):
        return len(self._adjacency_list)

    def get_neighbors(self,sel_vertex):
        return sel_vertex.edges
    
    def __repr__(self):
        if not self._adjacency_list:
            return 'Null'
        else:
            ret_val = []
            [ret_val.append(f'{node.value} : {self._adjacency_list[node]}') for node in self._adjacency_list.keys()]
            holder = ','
            str_ver = f'{holder.join(ret_val)} '
            return str_ver 
           


class Vertex:
    def __init__(self,value):
        self.value = value
        self.edges = []
class Edge:
    def __init__(self,vertex, weight=1):
        self.vertex = vertex
        self.weight = weight
    def __repr__(self):
        return f'{self.weight},{self.vertex}'

def DF(graph,root):
    visited = []
    ret_col = []

    def DF_Tool(graph,vertex):
        nonlocal visited
        nonlocal ret_col
        visited.append(vertex)
        ret_col.append(vertex)

        for link in graph.get_neighbors(vertex):
            if link not in visited:
                DF_Tool(graph,link)
     
    DF_Tool(graph,root)

    return ret_col

if __name__ == '__main__':
    print('Life')
    test = Queue()