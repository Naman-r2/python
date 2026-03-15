# ---------------------------------------
# Binary Search Tree (BST)
# ---------------------------------------

'''
Docstring for BST

Searching in Binary Tree  -> O(n)
Searching in Binary Search Tree -> O(log n)
(only if tree is balanced; otherwise it can degrade to O(n))

BST Property:
Left subtree  -> elements smaller than root
Right subtree -> elements greater than root


Inorder Successor:
Go one step to the right subtree
Then go to the LEFTMOST element

Inorder Predecessor:
Go one step to the left subtree
Then go to the RIGHTMOST element


Deletion Cases in BST

Case 1: Node is a LEAF
Parent pointer → None

Case 2: Node has ONE CHILD
Parent pointer → child node

Case 3: Node has TWO CHILDREN
Replace node with its inorder successor
Then delete the successor node
'''


# ---------------------------------------
# Node Structure
# ---------------------------------------
# Each node contains:
# data  -> value stored
# left  -> pointer to left child
# right -> pointer to right child

class node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value


# ---------------------------------------
# Insert Operation
# ---------------------------------------
# Recursively inserts element in BST
# smaller -> left
# larger  -> right

def insert(root,value):

    if root == None:
        return node(value)

    # avoid duplicate insertion
    if root.data == value:
        return root

    if root.data > value:
        root.left = insert(root.left,value)

    else:
        root.right = insert(root.right,value)

    return root


# ---------------------------------------
# Search Operation
# ---------------------------------------
# Traverses tree based on BST property

def search(root,value):

    if root == None:
        print("element not found")
        return

    if root.data == value:
        print("element found",end="\n")
        return

    if root.data > value:
        search(root.left,value)

    else:
        search(root.right,value)


# ---------------------------------------
# Find Inorder Successor
# ---------------------------------------
# Move to right subtree
# then find leftmost node

def get_successor(root):

    root = root.right

    while root != None and root.left != None:
        root = root.left

    return root


# ---------------------------------------
# Delete Operation in BST
# ---------------------------------------

def delete(root,value):

    if root == None:
        return root

    # search node in left subtree
    if root.data > value:
        root.left = delete(root.left,value)

    # search node in right subtree
    elif root.data < value:
        root.right = delete(root.right,value)

    # node found
    else:

        # Case 1 + Case 2
        # if node has only right child
        if root.left == None:
            return root.right

        # if node has only left child
        if root.right == None:
            return root.left

        # Case 3: node has two children
        else:

            # find inorder successor
            succ = get_successor(root)

            # replace node data
            root.data = succ.data

            # delete successor node
            root.right = delete(root.right,succ.data)

    return root


# ---------------------------------------
# Inorder Traversal
# ---------------------------------------
# Left → Root → Right
# For BST this prints elements in sorted order

def InOrder(root):

    if root != None:

        InOrder(root.left)

        print(root.data,end=" ")

        InOrder(root.right)



# ---------------------------------------
# Driver Code
# ---------------------------------------

root = insert(None,20)
root = insert(root,15)
root = insert(root,30)
root = insert(root,40)
root = insert(root,12)
root = insert(root,18)
root = insert(root,25)

# print sorted BST
InOrder(root)

# searching elements
search(root,45)
search(root,25)

# delete leaf node
delete(root,12)
print("\n")
InOrder(root)

# delete node with one child
delete(root,40)
print("\n")
InOrder(root)

# delete node with two children
delete(root,30)
print("\n")
InOrder(root)
