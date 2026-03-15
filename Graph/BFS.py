# ---------------------------------------
# Breadth First Search (BFS)
# ---------------------------------------

'''
BFS (Breadth First Search)

Idea:
Traverse the graph level by level.

It is similar to:
Level Order Traversal in Trees.

Data Structure Used:
QUEUE (FIFO)

Steps:
1. Start from source node.
2. Mark it as visited.
3. Put it in the queue.
4. Remove node from queue.
5. Visit all its unvisited neighbours.
6. Repeat until queue becomes empty.

Time Complexity:
O(V + E)

Space Complexity:
O(V)
'''

from collections import deque


class Graph:

    # ---------------------------------------
    # Constructor
    # ---------------------------------------
    # vertex -> number of vertices
    def __init__(self,vertex):

        # adjacency matrix representation
        self.mat = [[0]*vertex for x in range(vertex)]

        self.size = vertex 


    # ---------------------------------------
    # Add Edge
    # ---------------------------------------
    # Undirected graph
    # so both directions are marked
    def add_edge(self,src,dest):

        if 0 <= src < self.size and 0 <= dest < self.size:

            self.mat[src][dest] = 1
            self.mat[dest][src] = 1

        else:
            print("invalid edge") 


    # ---------------------------------------
    # Print Adjacency Matrix
    # ---------------------------------------
    def print_mat(self):

        for row in self.mat:
            print(' '.join(map(str,row)))


    # ---------------------------------------
    # BFS Traversal
    # ---------------------------------------
    # src -> starting vertex

    def bfs(self,src):

        # visited list to track visited vertices
        visited = [False]*self.size

        # queue for BFS traversal
        queue = deque([src])

        # mark source as visited
        visited[src] = True 

        while(queue):

            # remove first element
            v = queue.popleft()

            # print current node
            print(v,end=" -> ")   

            # check all neighbours
            for i in range(self.size):

                if self.mat[v][i] == 1 and visited[i] == False:

                    visited[i] = True

                    queue.append(i)


# ---------------------------------------
# Driver Code
# ---------------------------------------

g = Graph(6)

g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,5)
g.add_edge(4,5)

# BFS traversal starting from vertex 0
g.bfs(0)