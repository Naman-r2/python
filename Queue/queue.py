# ---------------------------------------
# Queue Data Structure
# ---------------------------------------
# Queue follows FIFO principle:
# FIFO = First In First Out
#
# Insertion happens from REAR
# Deletion happens from FRONT
#
# enqueue  -> insertion operation
# dequeue  -> deletion operation


'''
Docstring for Queue Working

Initial condition:
Queue empty -> front = rear = -1

First element insertion:
front = 0
rear  = 0

Further insertion:
rear = rear + 1
(check overflow if array implementation)

Deletion:
front = front + 1
(check underflow)

Performance specific note:
In Python we usually use a list.
We don't manually maintain front or rear.

Insertion:
append() -> adds element at the rear

Deletion:
pop(0) -> removes element from front
But this shifts all elements left, so it is O(n)
'''

class queue:

    # ---------------------------------------
    # Constructor
    # ---------------------------------------
    # Initializes an empty list to store queue elements
    def __init__(self):
        self.q = []


    # ---------------------------------------
    # Check if queue is empty
    # ---------------------------------------
    # Returns True if queue length is 0
    def isEmpty(self):
        return len(self.q) == 0
    

    # ---------------------------------------
    # Insert element into queue (enqueue)
    # ---------------------------------------
    # append() adds element at the end (rear)
    def insert(self,value):
        self.q.append(value)


    # ---------------------------------------
    # Delete element from queue (dequeue)
    # ---------------------------------------
    # pop(0) removes the first element (front)
    # If queue is empty → underflow condition
    def delete(self):

        if self.isEmpty():
            print("Queue is Empty")
            return
        
        else: 
            return self.q.pop(0)


# ---------------------------------------
# Driver Code (Testing Queue)
# ---------------------------------------

q = queue()

# inserting elements into queue
q.insert(20)
q.insert(30)
q.insert(60)

# deleting elements (FIFO order)
print(q.delete())   # removes 20
print(q.delete())   # removes 30
print(q.delete())   # removes 60
print(q.delete())   # queue empty condition

    

    
