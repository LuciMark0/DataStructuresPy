class Element:
    """
    Represents an element/node in a linked list.
    """
    def __init__(self, value):
        """
        Initialize an element with a given value.
        """
        self.value = value
        self.next = None

class LinkedList:
    """
    Represents a linked list.
    """
    def __init__(self, head=None):
        """
        Initialize a linked list with a head element (optional).
        """
        self.head = head

    def append(self, new_element):
        """
        Add an element to the end of the linked list.
        """
        if self.head:
            # Find the last element
            current = self.head
            while current.next:
                current = current.next
            # Append the new element
            current.next = new_element
        else:
            # If the list is empty, set the new element as the head
            self.head = new_element

    def get_position(self, position):
        """
        Get the element at a specific position in the linked list.
        The first position is 1.
        Returns None if the position is not found.
        """
        current = self.head
        for _ in range(position - 1):
            if current is None:
                return None
            current = current.next
        return current

    def insert(self, new_element, position):
        """
        Insert a new element at the given position in the linked list.
        The first position is 1.
        Inserting at position 3 means placing it between the second and third elements.
        """
        if position == 1:
            # Insert at the beginning
            new_element.next = self.head
            self.head = new_element
            return

        current = self.head
        for _ in range(position - 2):
            if current is None:
                return
            current = current.next

        # Insert at the given position
        new_element.next = current.next
        current.next = new_element

    def delete(self, value):
        """
        Delete the first node with a given value from the linked list.
        """
        if self.head is None:
            return

        if self.head.value == value:
            # If the head has the value, update the head to the next element
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if current.next:
            # Delete the next element with the given value
            current.next = current.next.next


# Test cases
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

print("*" * 20)



class Queue:
    """
    Represents a queue data structure using a linked list.
    """
    def __init__(self, head=None):
        """
        Initialize a queue with a head element (optional).
        """
        self.storage = [head]

    def enqueue(self, new_element):
        """
        Add an element to the end of the queue.
        """
        self.storage.append(new_element)

    def peek(self):
        """
        Get the value of the first element in the queue without removing it.
        """
        return self.storage[0]

    def dequeue(self):
        """
        Remove and return the first element from the queue.
        """
        if self.storage:
            return self.storage.pop(0)
        return None


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

print("*" * 20)

class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        """
        Push (add) a new element onto the top of the stack.
        """
        self.ll.insert(new_element,1)

    def pop(self):
        """
        Remove and return the top element from the stack.
        """
        removed = self.ll.head
        if removed:
            self.ll.delete(self.ll.head.value)
        return removed


# Test cases
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

