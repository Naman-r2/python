# ---------------------------------------
# Node Class for Doubly Linked List
# ---------------------------------------
# Each node stores:
# data -> value of the node
# next -> pointer to the next node
# prev -> pointer to the previous node

class Node:
    def __init__(self, value=None):
        self.data = value      # stores node value
        self.next = None       # pointer to next node
        self.prev = None       # pointer to previous node
    

# ---------------------------------------
# Doubly Linked List Class
# ---------------------------------------
# In a Doubly Linked List every node has:
# previous pointer + next pointer
# This allows traversal in both directions

class DoublyLL:
    def __init__(self):
        self.head =None        # head points to first node


    # ---------------------------------------
    # Insert node at the end
    # ---------------------------------------
    # Steps:
    # 1. Create new node
    # 2. If list empty → make it head
    # 3. Traverse to last node
    # 4. Attach new node
    def insertAtEnd(self,value):
        temp=Node(value)       # create new node

        if(self.head==None):   # if list is empty
            self.head=temp
            return

        t=self.head

        # traverse to last node
        while t.next != None:
            t=t.next
            
        # connect last node with new node
        t.next = temp
        temp.prev = t


    # ---------------------------------------
    # Insert node at the beginning
    # ---------------------------------------
    # Steps:
    # 1. Create new node
    # 2. Point new node → old head
    # 3. Update previous pointer of old head
    # 4. Update head
    def insertatbeg(self,value):
        temp = Node(value)

        if(self.head==None):
            self.head=temp
            return

        temp.next = self.head      # new node points to old head
        self.head.prev = temp      # old head points back to new node
        self.head = temp           # update head


    # ---------------------------------------
    # Insert node after a given value
    # ---------------------------------------
    # value → new value to insert
    # x     → insert after node having data = x
    def insertatmid(self,value,x):

        temp = Node(value)
        t= self.head
        
        # traverse until node with data = x
        while t.next !=0:
            if t.data ==x:
                break
            else:
                t = t.next
        
        # adjusting pointers to insert node
        temp.next = t.next
        t.next.prev = temp
        t.next = temp 
        temp.prev = t


    # ---------------------------------------
    # Delete node with given value
    # ---------------------------------------
    # Steps:
    # 1. Check if list empty
    # 2. Check if node is head
    # 3. Traverse and remove node
    # 4. Adjust prev and next pointers
    def deletionDLL(self,value):

        if self.head == None:   # empty list
            return

        temp = self.head

        # Case 1: deleting head node
        if temp.data == value:
            self.head = temp.next 
            self.head.prev = None
            return

        # traverse list
        while temp.next != None:

            if temp.data == value:
                # connect previous node to next node
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                return
            else:
                temp = temp.next

        # Case 2: deleting last node
        if temp.data == value:
            temp.prev.next = None


    # ---------------------------------------
    # Print Doubly Linked List
    # ---------------------------------------
    # Traverses from head and prints nodes
    def printDLL(self):

        t1 = self.head

        while t1 != None:
            print(t1.data , end = "<-->")
            t1 = t1.next


# ---------------------------------------
# Driver Code (Testing DLL)
# ---------------------------------------

obj= DoublyLL()

# insert elements at end
obj.insertAtEnd(10)
obj.insertAtEnd(20)

# insert 50 after node containing 10
obj.insertatmid(50,10)

# delete node with value 20
obj.deletionDLL(20)

# print the doubly linked list
obj.printDLL()