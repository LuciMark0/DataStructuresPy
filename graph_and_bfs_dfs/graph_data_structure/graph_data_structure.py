class Node:
    def __init__(self, value):
        """Initialize a new Node with a value and an empty list of edges."""
        self.value = value
        self.edges = []


class Edge:
    def __init__(self, value, node_from, node_to):
        """Initialize a new Edge with a value, the source node, and the destination node."""
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph:
    def __init__(self, nodes=None, edges=None):
        """Initialize a new Graph with an optional list of nodes and edges."""
        self.nodes = nodes or []
        self.edges = edges or []

    def insert_node(self, new_node_val):
        """Insert a new node with the given value into the graph."""
        new_node = Node(new_node_val)
        self.nodes.append(new_node)

    def get_node_by_value(self, value):
        """Return the node with the specified value, if it exists in the graph."""
        for node in self.nodes:
            if node.value == value:
                return node
        return None

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        """Insert a new edge with the given value, connecting two nodes."""
        node_from = self.get_node_by_value(node_from_val)
        node_to = self.get_node_by_value(node_to_val)

        if node_from is None:
            node_from = Node(node_from_val)
            self.nodes.append(node_from)
        if node_to is None:
            node_to = Node(node_to_val)
            self.nodes.append(node_to)

        new_edge = Edge(new_edge_val, node_from, node_to)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Return a list of triples representing the edges in the graph.
        Each triple contains the edge value, source node value, and destination node value."""
        return [(edge.value, edge.node_from.value, edge.node_to.value) for edge in self.edges]

    def get_adjacency_list(self):
        """Return an adjacency list representation of the graph.
        Each index in the list corresponds to a source node,
        and each entry contains a list of tuples representing the destination nodes and edge values."""
        adj_list = []

        for node in self.nodes:
            if node.edges:
                edge_list = [(edge.node_to.value, edge.value) for edge in node.edges]
                adj_list.append(edge_list)
            else:
                adj_list.append([])

        return adj_list

    def get_adjacency_matrix(self):
        """Return an adjacency matrix representation of the graph.
        The matrix is a 2D list where rows represent source nodes and columns represent destination nodes.
        Each entry in the matrix stores the edge value, or 0 if no edge exists between the nodes."""
        num_nodes = len(self.nodes)
        adj_matrix = [[0] * (num_nodes + 1) for _ in range(num_nodes + 1)]

        for edge in self.edges:
            adj_matrix[edge.node_from.value][edge.node_to.value] = edge.value

        return adj_matrix


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

print("*" * 20)