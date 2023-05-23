# Tree Data Structure in Python

This repository provides implementations of tree data structures and related algorithms in Python. The goal is to offer a comprehensive set of examples that can be used as a reference or learning resource for understanding fundamental concepts of tree-based data structures.

## Tree Data Structure

A tree is an abstract data type that emulates a hierarchical structure. It consists of nodes connected by edges, with one node designated as the root. Each node can have zero or more child nodes, forming subtrees. Trees are commonly used in various applications, such as representing hierarchical relationships, organizing data, and enabling efficient search and traversal operations.

## Features

### Binary Tree

The `BinaryTree` class represents a binary tree, where each node has at most two child nodes: a left child and a right child. The implementation includes the following features:

- **Initialization**: Create a binary tree with a root node.
- **Search**: Find a value in the binary tree. Returns `True` if the value is found, `False` otherwise.
- **Print Tree**: Print all tree nodes as they are visited in a pre-order traversal.

### Binary Search Tree (BST)

The `BST` class represents a binary search tree, which is a special type of binary tree. In a binary search tree, for any given node, all values in its left subtree are less than the node's value, and all values in its right subtree are greater than the node's value. The implementation includes the following features:

- **Initialization**: Create a binary search tree with a root node.
- **Insertion**: Insert a new value into the binary search tree.
- **Search**: Find a value in the binary search tree. Returns `True` if the value is found, `False` otherwise.
- **Print Tree**: Print all tree nodes as they are visited in an in-order traversal.

## Usage

To use the tree data structures and algorithms implemented in this repository, follow these steps:

1. Clone the repository: `git clone https://github.com/your_username/DataStructuresPy.git`
2. Navigate to the tree directory: `cd DataStructuresPy/tree`
3. Choose the desired implementation (binary tree or binary search tree).
4. Explore the provided code examples and usage instructions in the corresponding README file.

Feel free to modify the code or integrate it into your own projects as needed. Contributions and feedback are also welcome!

## Examples

Here are a few examples of how to use the tree data structures:

```python
# Binary Tree Example
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.search(4))  # Should be True
print(tree.search(6))  # Should be False
print(tree.print_tree())  # Should be 1-2-4-5-3

# Binary Search Tree Example
bst = BST(4)
bst.insert(2)
bst.insert(1)
bst.insert(3)
bst.insert(5)

print(bst.search(3))  # Should be True
print(bst.search(6))  # Should be False
print(bst.print_tree())  # Example output: 1-2-3-4-5
