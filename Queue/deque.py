# ---------------------------------------
# Double Ended Queue (Deque)
# ---------------------------------------
# Deque = Double Ended Queue
#
# In a normal queue:
# insertion -> rear
# deletion  -> front
#
# In a DEQUE:
# insertion and deletion can happen from BOTH ends
#
# Operations:
# insertFront
# insertRear
# deleteFront
# deleteRear


'''
Docstring for Deque Working

Insertion at front:
If using array implementation:
front = front - 1

Deletion at rear:
rear = rear - 1

But in Python we usually use LIST.

Insertion operations:
append(value)      -> insert at end (rear)
insert(0,value)    -> insert at beginning (front)

Deletion operations:
pop()              -> remove from end
pop(0)             -> remove from front

Note:
pop(0) and insert(0,value) are O(n) because elements shift.
'''


class deque:

    # ---------------------------------------
    # Constructor
    # ---------------------------------------
    # Creates an empty list to represent deque
    def __init__(self):
        self.q = []


    # ---------------------------------------
    # Check if deque is empty
    # ---------------------------------------
    def isEmpty(self):
        return len(self.q) == 0
    

    # ---------------------------------------
    # Insert element at rear (end)
    # ---------------------------------------
    # append() adds element at end of list
    def insertEnd(self,value):
        self.q.append(value)
    

    # ---------------------------------------
    # Insert element at front (beginning)
    # ---------------------------------------
    # insert(0,value) places element at index 0
    def insertBeg(self,value):
        self.q.insert(0,value)


    # ---------------------------------------
    # Delete element from front
    # ---------------------------------------
    # pop(0) removes first element
    def deleteFront(self):

        if self.isEmpty():
            print("Queue is Empty")
            
        else: 
            return self.q.pop(0)
    

    # ---------------------------------------
    # Delete element from end
    # ---------------------------------------
    # pop() removes last element
    def deleteEnd(self):

        if self.isEmpty():
            print("Queue is Empty")
            
        else: 
            return self.q.pop()



# ---------------------------------------
# Driver Code (Testing Deque)
# ---------------------------------------

dq = deque()

# inserting elements
dq.insertEnd(10)   # [10]
dq.insertBeg(20)   # [20,10]
dq.insertEnd(30)   # [20,10,30]
dq.insertEnd(40)   # [20,10,30,40]
dq.insertBeg(50)   # [50,20,10,30,40]

# deleting elements
print(dq.deleteEnd())    # removes 40
print(dq.deleteFront())  # removes 50

print(dq.deleteEnd())    # removes 30
print(dq.deleteFront())  # removes 20

print(dq.deleteEnd())    # removes 10
print(dq.deleteFront())  # queue empty