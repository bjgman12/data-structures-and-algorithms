from data_structures.stacks_and_queues.stacks_and_queues import Node,Queue
class Graph:

    def __init__(self):
        self._adjacency_list = {}

    def add_node(self,value):
        v = Vertex(value)
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
    def breadth_first(self,start):
        seen = [False] * self.size()
        ret_col = []
        q = []

        q.append(start)
        seen[0] = True

        while q:

            start = q.pop(0)
            ret_col.append(start.value)

            for key in self.get_nodes():
                if not seen[self.get_nodes().index(key)]:
                    q.append(key)
                    seen[self.get_nodes().index(key)] = True

        return ret_col
           


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