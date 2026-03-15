# ---------------------------------------
# Tree Traversal
# ---------------------------------------
# Tree traversal means visiting every node
# of a tree exactly once in a specific order.
#
# Three common Depth First Traversals:
#
# 1. Preorder  -> Root Left Right
# 2. Inorder   -> Left Root Right
# 3. Postorder -> Left Right Root
#
# These traversals are usually implemented
# using recursion.


'''
Traversal Order Summary

Preorder:
1. Visit Root
2. Traverse Left Subtree
3. Traverse Right Subtree

Inorder:
1. Traverse Left Subtree
2. Visit Root
3. Traverse Right Subtree

Postorder:
1. Traverse Left Subtree
2. Traverse Right Subtree
3. Visit Root

Recursion idea:
Each function calls itself on left and right subtree.
'''


# ---------------------------------------
# Node Class for Binary Tree
# ---------------------------------------
# Each node contains:
# data  -> value of node
# left  -> pointer to left child
# right -> pointer to right child

class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None
    

# ---------------------------------------
# Preorder Traversal
# ---------------------------------------
# Order: Root → Left → Right
#
# Steps:
# 1. Print root
# 2. Traverse left subtree
# 3. Traverse right subtree

def preOrder(root):

    # base condition for recursion
    if root != None:

        print(root.data,end=" ")

        # recursive call for left subtree
        preOrder(root.left)

        # recursive call for right subtree
        preOrder(root.right)


# ---------------------------------------
# Inorder Traversal
# ---------------------------------------
# Order: Left → Root → Right
#
# Steps:
# 1. Traverse left subtree
# 2. Print root
# 3. Traverse right subtree

def InOrder(root):

    if root != None:

        # visit left subtree
        InOrder(root.left)

        # print root node
        print(root.data,end=" ")

        # visit right subtree
        InOrder(root.right)


# ---------------------------------------
# Postorder Traversal
# ---------------------------------------
# Order: Left → Right → Root
#
# Steps:
# 1. Traverse left subtree
# 2. Traverse right subtree
# 3. Print root

def PostOrder(root):

    if root != None:

        # visit left subtree
        PostOrder(root.left)

        # visit right subtree
        PostOrder(root.right)

        # print root node
        print(root.data,end=" ")
        

# ---------------------------------------
# Creating Binary Tree (Driver Code)
# ---------------------------------------
# Tree structure created here:
#
#        1
#      /   \
#     3     5
#    / \     \
#   2   4     8
#

root = Node(1)

root.left = Node(3)
root.right = Node(5)

root.left.left = Node(2)
root.left.right = Node(4)

root.right.right = Node(8)


# ---------------------------------------
# Calling Traversals
# ---------------------------------------

# Preorder traversal
preOrder(root)

print("\n")

# Inorder traversal
InOrder(root)

print("\n")

# Postorder traversal
PostOrder(root)