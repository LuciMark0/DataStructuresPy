# Graph Data Structure

This is a Python implementation of a graph data structure consisting of nodes and edges. The code provides functionality to create a graph, insert nodes and edges, and retrieve information about the graph such as the edge list, adjacency list, and adjacency matrix.

## Classes

### Node

The `Node` class represents a node in the graph. Each node has a value and a list of edges.

#### Constructor

```python
def __init__(self, value):
    """Initialize a new Node with a value and an empty list of edges."""
    self.value = value
    self.edges = []
```

### Edge
The `Edge` class represents an edge in the graph. Each edge has a value, a source node, and a destination node.

#### Constructor
```python
def __init__(self, value, node_from, node_to):
    """Initialize a new Edge with a value, the source node, and the destination node."""
    self.value = value
    self.node_from = node_from
    self.node_to = node_to
```
### Graph
The `Graph` class represents a graph. It contains a list of nodes and a list of edges.

#### Constructor
```python
def __init__(self, nodes=None, edges=None):
    """Initialize a new Graph with an optional list of nodes and edges."""
    self.nodes = nodes or []
    self.edges = edges or []
```
#### Methods
`insert_node(self, new_node_val)`
Inserts a new node with the given value into the graph.

`get_node_by_value(self, value)`
Returns the node with the specified value, if it exists in the graph.

`insert_edge(self, new_edge_val, node_from_val, node_to_val)`
Inserts a new edge with the given value, connecting two nodes.

`get_edge_list(self)`
Returns a list of triples representing the edges in the graph. Each triple contains the edge value, source node value, and destination node value.

`get_adjacency_list(self)`
Returns an adjacency list representation of the graph. Each index in the list corresponds to a source node, and each entry contains a list of tuples representing the destination nodes and edge values.

`get_adjacency_matrix(self)`
Returns an adjacency matrix representation of the graph. The matrix is a 2D list where rows represent source nodes and columns represent destination nodes. Each entry in the matrix stores the edge value, or 0 if no edge exists between the nodes.

### Example Usage
```python
graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)

# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print(graph.get_edge_list())

# Should be [[ (2, 100), (3, 101), (4, 102) ], [(2, 100)], [(3, 101), (4, 103)], [(4, 102), (4, 103)]]
print(graph.get_adjacency_list())

# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print(graph.get_adjacency_matrix())
```
