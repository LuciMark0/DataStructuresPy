# Graph Data Structure

This Python code implements a Graph data structure using classes and provides various methods to manipulate and analyze the graph. The graph consists of nodes and edges connecting those nodes. The code supports operations like inserting nodes and edges, retrieving adjacency lists and matrices, performing depth-first search (DFS), and breadth-first search (BFS) traversal.

## Classes

The code defines three classes: `Node`, `Edge`, and `Graph`.

### Node

The `Node` class represents a node in the graph. Each node has a value, a list of edges connected to it, and a visited flag to track traversal status.

### Edge

The `Edge` class represents an edge connecting two nodes in the graph. It has a value and references to the source (`node_from`) and destination (`node_to`) nodes.

### Graph

The `Graph` class represents the entire graph. It contains a list of nodes, a list of edges, a list of node names (optional), and a node map for efficient node lookup.

The class provides the following methods:

- `set_node_names(names)`: Sets the names of the nodes in the graph. The Nth name in the `names` list corresponds to node number N.
- `insert_node(new_node_val)`: Inserts a new node with the given value into the graph.
- `insert_edge(new_edge_val, node_from_val, node_to_val)`: Inserts a new edge between two nodes or creates new nodes if necessary.
- `get_edge_list()`: Returns a list of triples representing the edges in the graph. Each triple contains the edge value, the value of the source node, and the value of the destination node.
- `get_edge_list_names()`: Returns a list of triples representing the edges in the graph. Each triple contains the edge value, the name of the source node, and the name of the destination node.
- `get_adjacency_list()`: Returns a list of lists representing the adjacency list of the graph. Each section in the list corresponds to a "from" node and contains tuples representing the adjacent nodes and edge values.
- `get_adjacency_list_names()`: Returns a list of lists representing the adjacency list of the graph. Each section in the list contains tuples representing the adjacent nodes (by name) and edge values.
- `get_adjacency_matrix()`: Returns a matrix (2D list) representing the adjacency matrix of the graph. Each element in the matrix corresponds to an edge value, or 0 if no edge exists.
- `find_max_index()`: Returns the highest node number found in the graph or the length of the node names if set using `set_node_names()`.
- `find_node(node_number)`: Returns the node with the given value or None if not found.
- `dfs(start_node_num)`: Performs a depth-first search traversal starting from the node with the given number and returns a list of traversed node values.
- `dfs_names(start_node_num)`: Performs a depth-first search traversal starting from the node with the given number and returns a list of traversed node names.
- `bfs(start_node_num)`: Performs a breadth-first search traversal starting from the node with the given number and returns a list of traversed node values.
- `bfs_names(start_node_num)`: Performs a breadth-first search traversal starting from the node with the given number and returns a list of traversed node names.
### Usage
Here's an example of how to use the code:
```python
graph = Graph()

# Set node names
graph.set_node_names(('Mountain View', 'San Francisco', 'London', 'Shanghai', 'Berlin', 'Sao Paolo', 'Bangalore'))

# Insert edges
graph.insert_edge(51, 0, 1)     # MV <-> SF
graph.insert_edge(51, 1, 0)     # SF <-> MV
graph.insert_edge(9950, 0, 3)   # MV <-> Shanghai
graph.insert_edge(9950, 3, 0)   # Shanghai <-> MV
graph.insert_edge(10375, 0, 5)  # MV <-> Sao Paolo
graph.insert_edge(10375, 5, 0)  # Sao Paolo <-> MV
graph.insert_edge(9900, 1, 3)   # SF <-> Shanghai
graph.insert_edge(9900, 3, 1)   # Shanghai <-> SF
graph.insert_edge(9130, 1, 4)   # SF <-> Berlin
graph.insert_edge(9130, 4, 1)   # Berlin <-> SF
graph.insert_edge(9217, 2, 3)   # London <-> Shanghai
graph.insert_edge(9217, 3, 2)   # Shanghai <-> London
graph.insert_edge(932, 2, 4)    # London <-> Berlin
graph.insert_edge(932, 4, 2)    # Berlin <-> London
graph.insert_edge(9471, 2, 5)   # London <-> Sao Paolo
graph.insert_edge(9471, 5, 2)   # Sao Paolo <-> London

# Print edge list
print("Edge List")
pprint.pprint(graph.get_edge_list_names())

# Print adjacency list
print("\nAdjacency List")
pprint.pprint(graph.get_adjacency_list_names())

# Print adjacency matrix
print("\nAdjacency Matrix")
pprint.pprint(graph.get_adjacency_matrix())

# Perform DFS traversal
print("\nDepth First Search")
pprint.pprint(graph.dfs_names(2))

# Perform BFS traversal
print("\nBreadth First Search")
pprint.pprint(graph.bfs_names(2))
```
This example demonstrates the creation of a graph with nodes and edges, setting node names, and performing various operations like printing the edge list, adjacency list, adjacency matrix, DFS traversal, and BFS traversal.

Feel free to modify the code and adapt it to your specific needs.

I hope this README helps you understand the provided code and its functionality. If you have any further questions, please let me know!
