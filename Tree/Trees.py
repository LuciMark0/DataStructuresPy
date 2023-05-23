class Node:
    def __init__(self, value):
        """
        Initialize a new node with the given value.
        """
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        """
        Initialize a binary tree with a root node.
        """
        self.root = Node(root)

    def search(self, find_val):
        """
        Search for a value in the binary tree.
        Return True if the value is found, False otherwise.
        """
        return self._preorder_search(self.root, find_val)

    def _preorder_search(self, start, find_val):
        """
        Helper method for recursive search in the binary tree.
        """
        if start:
            if start.value == find_val:
                return True
            if self._preorder_search(start.left, find_val):
                return True
            if self._preorder_search(start.right, find_val):
                return True
        return False

    def print_tree(self):
        """
        Print out all tree nodes as they are visited in a pre-order traversal.
        """
        return "-".join(self._preorder_print(self.root))

    def _preorder_print(self, start):
        """
        Helper method for recursive printing of the binary tree.
        """
        if start:
            result = [str(start.value)]
            return result + self._preorder_print(start.left) + self._preorder_print(start.right)
        return []


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
print(tree.search(4))  # Should be True
print(tree.search(6))  # Should be False

# Test print_tree
print(tree.print_tree())  # Should be 1-2-4-5-3

print("*" * 20)

# Additional tests with new tree for BinaryTree

# Create a new binary tree
tree = BinaryTree(1)

# Insert elements
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# Test search
print(tree.search(4))  # Should be True
print(tree.search(6))  # Should be True
print(tree.search(8))  # Should be False

# Test print_tree
print(tree.print_tree())  # Should be 1-2-4-5-3-6-7

print("*" * 20)


class BST:
    def __init__(self, root):
        """
        Initialize a binary search tree with a root node.
        """
        self.root = Node(root)

    def insert(self, new_val):
        """
        Insert a new value into the binary search tree.
        """
        start = self.root
        while True:
            if start.value > new_val:
                if start.left:
                    start = start.left
                else:
                    start.left = Node(new_val)
                    break
            else:
                if start.right:
                    start = start.right
                else:
                    start.right = Node(new_val)
                    break

    def search(self, find_val):
        """
        Search for a value in the binary search tree.
        Return True if the value is found, False otherwise.
        """
        start = self.root
        while start:
            if start.value == find_val:
                return True
            elif start.value > find_val:
                start = start.left
            else:
                start = start.right
        return False

    def print_tree(self):
        """
        Print out all tree nodes as they are visited in an in-order traversal.
        """
        return "-".join(self._inorder_print(self.root))

    def _inorder_print(self, start):
        """
        Helper method for recursive printing of the binary search tree in an in-order traversal.
        """
        result = []
        if start:
            result += self._inorder_print(start.left)
            result.append(str(start.value))
            result += self._inorder_print(start.right)
        return result

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
print(tree.search(3))  # Should be True
print(tree.search(6))  # Should be False

print("*" * 20)

# Additional tests with new tree for BST

# Create a new binary search tree
tree = BST(5)

# Insert elements
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

# Check search
print(tree.search(4))  # Should be True
print(tree.search(9))  # Should be False

# Test print_tree method
print(tree.print_tree())  # Example output: 2-3-4-5-6-7-8