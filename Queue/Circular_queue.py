# ---------------------------------------
# Circular Queue
# ---------------------------------------
# A Circular Queue is an improved version of a normal queue.
#
# In a normal queue:
# insertion -> rear = rear + 1
# deletion  -> front = front + 1
#
# Problem:
# After many deletions, empty spaces appear at the front,
# but they cannot be reused.
#
# Circular Queue solves this by connecting the end of the
# array back to the beginning (circular structure).


'''
Docstring for Circular Queue Working

Normal Queue:
insert  -> rear + 1
delete  -> front + 1

Circular Queue:
If there is no space at the end,
insertion continues at the beginning (if free).

Empty condition:
front = rear = -1

Full condition:
(rear + 1) % size == front

We use MODULUS (%) operator because when rear
reaches the end, the next position should become 0.

Insertion index:
(rear + 1) % size

Deletion index:
(front + 1) % size
'''


class CircularQueue:

    # ---------------------------------------
    # Constructor
    # ---------------------------------------
    # size -> maximum capacity of queue
    def __init__(self,size):
        self.size = size

        # create fixed size list with None values
        self.item = [None] * size

        # initialize front and rear pointers
        self.front = self.rear = -1


    # ---------------------------------------
    # Enqueue (Insertion)
    # ---------------------------------------
    # Adds element at rear position
    def enqueue(self,value):

        # check FULL condition
        if ((self.rear + 1) % self.size == self.front):
            print("Queue is full")

        # inserting first element
        elif self.front == -1:
            self.front = self.rear = 0
            self.item[self.rear] = value 

        else:
            # move rear circularly
            self.rear = (self.rear + 1) % self.size

            # insert value
            self.item[self.rear] = value 


    # ---------------------------------------
    # Dequeue (Deletion)
    # ---------------------------------------
    # Removes element from front
    def dequeue(self):

        # check EMPTY condition
        if self.front == -1:
            print("Queue is empty")

        # if only one element remains
        elif self.front == self.rear :
            print(self.item[self.front])

            # reset queue
            self.front = self.rear = -1

        else:
            # print removed element
            print(self.item[self.front])

            # move front circularly
            self.front = (self.front + 1) % self.size 



# ---------------------------------------
# Driver Code (Testing Circular Queue)
# ---------------------------------------

cq = CircularQueue(5)

# inserting elements
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)

# deleting one element
cq.dequeue()

# inserting again (circular reuse)
cq.enqueue(60)
cq.enqueue(40)

# multiple deletions
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()

