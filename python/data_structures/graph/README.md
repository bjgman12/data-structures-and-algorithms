## Graph implementation
 > implementation of the graph data structure

### Challenges 

- implement a graph data structure

- implement a depth first traversal

### Approach and Efficiency


## Basic implement API

- Graph.add_node(value)
- Graph.add_edge(start_vetex, end_vertex, weight)
- Graph.get_nodes()
- Graph.get_neighbors(vertex)
- Graph.size()

## Challenge API

### DepthFirst(graph)

#### Algo

- push root into depth_stack[list] and append to ret_collention[list]
- while depth_stack
  - peek at top of stack
  - if children not in ret_collection append to ret_collection and push on depth_stack
  - else pop stack
-return ret_collection

#### Pseudo
- def DFS_tool(graph,vertex,containter):
    - visited <-push-[vertex]
    -  non localcontainer <-append- vertex

    for neighbor in graph.get_neighbors(vertex):
        if neighbor not in visited:
            DFS(graph,neighbor,visited)


- def DFS(graph,root):
  - visited = []
  -  non local container 
  - DFS_tool(graph,root,container)
  - return container
  
