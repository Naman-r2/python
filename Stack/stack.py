# ---------------------------------------
# Stack Data Structure
# ---------------------------------------
# Stack follows the LIFO principle:
# LIFO = Last In First Out
#
# The last element inserted is the first one removed.
#
# Main operations:
# push  -> insert element
# pop   -> remove top element
# peek  -> view top element
# length -> number of elements in stack


class stack:

    # ---------------------------------------
    # Constructor
    # ---------------------------------------
    # Initializes an empty list that will store stack elements
    def __init__(self):
        self.s = []


    # ---------------------------------------
    # Length of Stack
    # ---------------------------------------
    # Returns number of elements currently in stack
    def length(self):
        return len(self.s) 
        

    # ---------------------------------------
    # Push Operation
    # ---------------------------------------
    # Adds a new element to the TOP of stack
    # insert(0,value) places element at index 0
    def push(self,value):
        self.s.insert(0,value)


    # ---------------------------------------
    # Peek Operation
    # ---------------------------------------
    # Returns the top element without removing it
    # If stack is empty → raise exception
    def peek(self):

        if len(self.s) == 0:
            raise Exception("stack is empty")

        else:
            return self.s[0]
        

    # ---------------------------------------
    # Pop Operation
    # ---------------------------------------
    # Removes and returns the top element
    # If stack is empty → raise exception
    def pop(self):

        if len(self.s) == 0:
            raise Exception("stack is empty")

        else:
            return self.s.pop(0)
        


# ---------------------------------------
# Driver Code (Testing Stack)
# ---------------------------------------

stk = stack()

# push elements onto stack
stk.push(10)
stk.push(20)

# view top element
stk.peek()

# remove top element
stk.pop()

# check stack size
stk.length()
