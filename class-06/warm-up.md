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
        # Your code here
        
        # Initialize the next attribute with the given value.
        # Your code here

# 2. Define the LinkedList class
# Task: Implement the __init__ and append methods for the LinkedList class.
# The __init__ method should initialize the head attribute with None.
# The append method should add a new node with the given value at the end of the list.
class LinkedList:
    def __init__(self):
        # Initialize the head attribute with None.
        # Your code here

    def append(self, value):
        # Create a new node with the given value.
        # Your code here
        
        # If the list is empty, set the head to the new node.
        # Otherwise, iterate through the list until the last node is found,
        # and set its next attribute to the new node.
        # Your code here
        
    def print_ll(self):
        # Traverse the list and print the value of each node.
        # Your code here


# 4. Test your implementation
# Task: Create a new linked list and append some values to it.
# Then, traverse the list and print the values.

# Create a new linked list.
# Your code here

# Append some values to the linked list (e.g., 1, 2, 3, 4, 5).
# Your code here

# Traverse the linked list and print the values.
# Your code here
```
