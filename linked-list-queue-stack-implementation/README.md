# Linked List

The linked list is a fundamental data structure where elements are stored in a sequence and connected using pointers. This implementation includes a `LinkedList` class with the following methods:

### `__init__(self, head=None)`

Initialize a linked list with an optional head element.

### `append(self, new_element)`

Add an element to the end of the linked list.

### `get_position(self, position)`

Get the element at a specific position in the linked list. The first position is 1. Returns `None` if the position is not found.

### `insert(self, new_element, position)`

Insert a new element at the given position in the linked list. The first position is 1. Inserting at position 3 means placing it between the second and third elements.

### `delete(self, value)`

Delete the first node with a given value from the linked list.

#### Example usage:

```python
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
```
# Queue

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. This implementation uses a linked list as the underlying data structure and includes a Queue class with the following methods:

### `__init__(self, head=None)`
Initialize a queue with an optional head element.

### `enqueue(self, new_element)`
Add an element to the end of the queue.

### `peek(self)`
Get the value of the first element in the queue without removing it.

### `dequeue(self)`
Remove and return the first element from the queue.

#### Example usage:

```python
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print(q.peek())

# Test dequeue
# Should be 1
print(q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print(q.dequeue())
# Should be 3
print(q.dequeue())
# Should be 4
print(q.dequeue())
q.enqueue(5)
# Should be 5
print(q.peek())
```
# Stack

A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. This implementation uses a linked list as the underlying data structure and includes a `Stack` class with the following methods:

### `__init__(self, top=None)`

Initialize a stack with an optional top element.

### `push(self, new_element)`

Push (add) a new element onto the top of the stack.

### `pop(self)`

Remove and return the top element from the stack.

#### Example usage:

```python
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print(stack.pop().value)  # Should print 3
print(stack.pop().value)  # Should print 2
print(stack.pop().value)  # Should print 1
print(stack.pop())        # Should print None
stack.push(e4)
print(stack.pop().value)  # Should print 4
```

# Contributing
Contributions to this repository are welcome! If you have any improvements, bug fixes, or additional data structures and algorithms implementations in Python, feel free to submit a pull request.

# License
This project is licensed under the MIT License.

# Acknowledgments
This repository was inspired by the need for a comprehensive collection of data structures and algorithms implemented in Python. Special thanks to the contributors who have helped make this project better.

If you have any questions or suggestions, please open an issue or reach out to the project maintainers.

Happy coding!

Feel free to adjust the README as per your preferences, adding more details or sections if needed.
