```python
# Warm-up Exercise: Node-based Linked Lists

# In this exercise, you will implement a simple singly linked list in Python.
# You will define two classes: Node and LinkedList.

# 1. Define the Node class
# Task: Implement the __init__ method for the Node class.
# This method should take a value and initialize the value and next attributes.
class Node:
    def __init__(self, value, next=None):
        # Initialize the value attribute with the given value.
        self.value = value
        
        # Initialize the next attribute with the given value.
        self.next = next

# 2. Define the LinkedList class
# Task: Implement the __init__ and append methods for the LinkedList class.
# The __init__ method should initialize the head attribute with None.
# The append method should add a new node with the given value at the end of the list.
class LinkedList:
    def __init__(self):
        # Initialize the head attribute with None.
        self.head = None

    def append(self, value):
        # Create a new node with the given value.
        new_node = Node(value)
        
        # If the list is empty, set the head to the new node.
        if self.head is None:
            self.head = new_node
        # Otherwise, iterate through the list until the last node is found,
        # and set its next attribute to the new node.
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
    def print_ll(self):
        # Traverse the list and print the value of each node.
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

# 4. Test your implementation
# Task: Create a new linked list and append some values to it.
# Then, traverse the list and print the values.

# Create a new linked list.
my_linked_list = LinkedList()

# Append some values to the linked list (e.g., 1, 2, 3, 4, 5).
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

# Traverse the linked list and print the values.
my_linked_list.print_ll()
```
