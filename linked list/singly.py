# ---------------------------------------
# Node Class
# ---------------------------------------
# A Node represents a single element of the linked list.
# Each node stores:
# 1. data  -> value of the node
# 2. next  -> reference (pointer) to the next node in the list

class Node:
    def __init__(self,info,next=None):
        self.data = info     # stores the value of the node
        self.next = next     # pointer to the next node (default = None)


# ---------------------------------------
# Singly Linked List Class
# ---------------------------------------
# A Singly Linked List contains nodes where each node
# points to the next node. The list starts with a head pointer.

class SinglyLinkedList:
    def __init__(self,head=None):
        self.head = head     # head points to the first node of the list


    # ---------------------------------------
    # Insert a node at the end of the list
    # ---------------------------------------
    # Steps:
    # 1. Create a new node.
    # 2. If the list is empty → make it the head.
    # 3. Otherwise traverse until the last node.
    # 4. Attach new node at the end.
    def insertAtEnd(self,value):
        temp = Node(value)   # create new node

        if self.head != None:        # if list is not empty
            t1 = self.head           # start traversal from head

            # move until last node
            while(t1.next!=None):
                t1 = t1.next 

            # attach new node at the end
            t1.next = temp

        else:
            # if list is empty, new node becomes head
            self.head = temp


    # ---------------------------------------
    # Insert a node at the beginning
    # ---------------------------------------
    # Steps:
    # 1. Create a new node.
    # 2. Point new node to current head.
    # 3. Update head to new node.
    def insertatbeg(self,value):
        temp=Node(value)     # create new node
        temp.next = self.head  # new node points to old head
        self.head = temp       # head updated to new node


    # ---------------------------------------
    # Insert a node after a specific value
    # ---------------------------------------
    # value → new value to insert
    # x     → insert after node having data = x
    #
    # Steps:
    # 1. Traverse the list.
    # 2. When node.data == x
    # 3. Insert new node after it.
    def insertInMid(self,value,x):
        temp = Node(value)   # create new node
        t1 = self.head       # start traversal from head

        while(t1.next != None):

            # check if current node matches x
            if(t1.data == x):

                # adjust links to insert new node
                temp.next = t1.next
                t1.next = temp

            t1 = t1.next


    # ---------------------------------------
    # Delete a node with a given value
    # ---------------------------------------
    # Steps:
    # 1. Check if head contains the value.
    # 2. Traverse the list keeping track of previous node.
    # 3. Change links to remove the node.
    def deleteLL(self,value):

        prev = self.head
        t1 = self.head

        # Case 1: value is at head
        if t1.data ==value:
            self.head = t1.next

        # Traverse the list
        while(t1.next != None):

            # if node found
            if t1.data == value:

                # bypass the node
                prev.next=t1.next
                break

            else:
                # move both pointers forward
                prev = t1
                t1 = t1.next

        # Case 2: if value is in the last node
        if(t1.data ==value):
            prev.next =None


    # ---------------------------------------
    # Print Linked List
    # ---------------------------------------
    # Traverses from head and prints each node's data.
    def printLL(self):
        t1 = self.head

        # traverse until end of list
        while(t1!=None):
            print(t1.data)
            t1 = t1.next


# ---------------------------------------
# Driver Code (Testing the Linked List)
# ---------------------------------------

obj = SinglyLinkedList()

# inserting elements at the end
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)

# inserting element at beginning
obj.insertatbeg(5)

# inserting 40 after node with value 20
obj.insertInMid(40,20)

# deleting node with value 30
obj.deleteLL(30)

# printing the linked list
obj.printLL()
