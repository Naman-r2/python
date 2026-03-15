# ---------------------------------------
# TREE DATA STRUCTURE
# ---------------------------------------

'''
Binary Tree Concepts

Binary Tree:
A tree where each node can have at most 2 children.

Binary Search Tree (BST):
Left subtree  -> elements smaller than root
Right subtree -> elements greater than root

Strict Binary Tree:
Every node has either 0 or 2 children.

Complete Binary Tree:
All levels are filled except possibly the last,
and nodes are filled from left to right.

Skew Binary Tree:
All nodes lie only on left OR only on right side.

Degenerated Tree:
Tree behaves like a linked list (zig-zag structure).

Extended Binary Tree:
Dummy nodes are added to leaf nodes so every node
has either 0 or 2 children.
'''

# ---------------------------------------
# Binary Tree Representation
# ---------------------------------------

'''
1. Array Representation

Left child  -> 2*i + 1
Right child -> 2*i + 2

Works best for COMPLETE binary trees.
Drawback -> memory wastage when tree is sparse.


2. Linked List Representation

Each node contains:
[left pointer][data][right pointer]
'''


# ---------------------------------------
# Node Structure (Linked Representation)
# ---------------------------------------

class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None


# ---------------------------------------
# Binary Search Tree Class
# ---------------------------------------

class BST:

    def __init__(self):
        self.root = None


    # ---------------------------------------
    # Insert Node in BST
    # ---------------------------------------
    # smaller -> left
    # larger  -> right

    def insert(self,value):

        newnode = Node(value)

        if self.root == None:
            self.root = newnode
            return

        temp = self.root

        while True:

            if value < temp.data:

                if temp.left == None:
                    temp.left = newnode
                    return
                else:
                    temp = temp.left

            else:

                if temp.right == None:
                    temp.right = newnode
                    return
                else:
                    temp = temp.right


# ---------------------------------------
# Tree Traversals
# ---------------------------------------

'''
Preorder Traversal
Root -> Left -> Right
'''

def preorder(root):

    if root != None:

        print(root.data,end=" ")

        preorder(root.left)

        preorder(root.right)



'''
Inorder Traversal
Left -> Root -> Right
'''

def inorder(root):

    if root != None:

        inorder(root.left)

        print(root.data,end=" ")

        inorder(root.right)



'''
Postorder Traversal
Left -> Right -> Root
'''

def postorder(root):

    if root != None:

        postorder(root.left)

        postorder(root.right)

        print(root.data,end=" ")



# ---------------------------------------
# Driver Code
# ---------------------------------------

tree = BST()

tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)

print("Preorder Traversal:")
preorder(tree.root)

print("\nInorder Traversal:")
inorder(tree.root)

print("\nPostorder Traversal:")
postorder(tree.root)
