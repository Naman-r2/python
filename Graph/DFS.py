# ---------------------------------------
# Depth First Search (DFS)
# ---------------------------------------

'''
DFS (Depth First Search)

Idea:
Explore a path as deep as possible before backtracking.

Key Concepts:
- Uses a VISITED array to avoid visiting nodes again
- Uses STACK (or recursion)
- Backtracking occurs when no further nodes can be explored
- Prevents infinite cycles in graphs

Applications:
- Graph traversal
- Cycle detection
- Topological sorting
- Finding connected components

Note:
DFS traversal can form a spanning tree of the graph.
'''

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
    # Since graph is UNDIRECTED
    # both directions are marked
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
    # DFS Traversal (Iterative using Stack)
    # ---------------------------------------
    # src -> starting vertex
    def dfs(self,src):

        # visited array to track visited nodes
        visited = [False] * self.size

        # stack used for DFS traversal
        stack = [src]

        while(stack):

            # pop last element (LIFO behavior)
            v = stack.pop()

            if visited[v] == False:

                # visit node
                print(v,end=" -> ")

                visited[v] = True 

            # check neighbours
            for i in range(self.size):

                if self.mat[v][i] == 1 and visited[i] == False:

                    stack.append(i)


# ---------------------------------------
# Driver Code
# ---------------------------------------

g = Graph(6)

g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,5)

# self loop example
g.add_edge(5,5)

# start DFS from node 0
g.dfs(0)