**Problem Description: Inverting a Binary Tree**

In this problem, you are given the root node of a binary tree. The task is to "invert" the tree, also known as creating a mirror image of the tree, by swapping the left and right children of all nodes in the tree. The resulting tree should have the property that an inorder traversal will result in the values appearing in descending order.

Let's discuss an example. Suppose you have the following binary tree:

```
      4
     / \
    2   7
   / \ / \
  1  3 6  9
```

The inverted version of this tree is as follows:

```
      4
     / \
    7   2
   / \ / \
  9  6 3  1
```

As you can see, the left and right subtrees for each node have been swapped, creating a "mirror image" of the original tree.

**Input**:

Your function will take one input parameter:

1. The root node of the binary tree.

**Output**:

Your function should return the root node of the inverted binary tree.

**Function Signature**:

In Python, your function signature would be something like:

```python
def invert_tree(root):
    pass  # your code here
```
