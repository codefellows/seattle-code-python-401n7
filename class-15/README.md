# TASK 1: Define a Node class with an __init__ method that takes
# a value (an integer) and optional left and right children (Node instances),
# and has a __str__ method that returns the instance's value as a string.
class Node:
    # Complete the __init__ method
    def __init__(self, value, left=None, right=None):
        # self.value =
        # self.left =
        # self.right =
        pass  # Remove this line, complete the __init__ method

    # Complete the __str__ method to return the value.
    def __str__(self):
        return self  # What's wrong with this line of code?


# TASK 2: Define a BinaryTree class with an __init__ method
# that takes an optional root (a Node instance).
class BinaryTree:
    def __init__(self, root=None):
        pass  # Replace this line with the correct code.

    # TASK 3: Add comments to the `inorder_traversal` method explaining each line of code.
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value)
            self.inorder_traversal(node.right)

    # TASK 4: Add a method to insert a new value into the binary tree.
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_helper(self.root, value)

    def _insert_helper(self, current_node, value):
        pass  # Replace this line with the correct code.


if __name__ == "__main__":
    # Example usage:
    # binary_tree = BinaryTree(Node(10))
    # binary_tree.inorder_traversal(binary_tree.root)

    # TASK 5: Insert values into the binary tree using the insert method
    # Examples:
    # binary_tree.insert(5)
    # binary_tree.insert(15)

    # TASK 6: Call the inorder_traversal method to print all values in the binary tree
    # Example:
    # binary_tree.inorder_traversal(binary_tree.root)
