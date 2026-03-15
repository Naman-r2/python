# ---------------------------------------
# Graph Representation using Adjacency Matrix
# ---------------------------------------

'''
Docstring for Graph

Types of Graphs

1. Undirected Graph
Edges have no direction
Example: A --- B

2. Directed Graph
Edges have direction
Example: A → B

3. Weighted Graph
Edges contain weights (cost/distance)


Graph Density

Dense Graph:
Number of edges is high (many 1's in matrix)

Sparse Graph:
Number of edges is low


Graph Representation Methods

1. Adjacency Matrix
2. Adjacency List


Adjacency Matrix

A 2D matrix where:
matrix[i][j] = 1  → edge exists between i and j
matrix[i][j] = 0  → no edge

Advantages:
- Very simple representation
- Fast edge lookup

Disadvantages:
- Wastes memory when graph is sparse
- Requires V² space
'''

class Graph:

    # ---------------------------------------
    # Constructor
    # ---------------------------------------
    # vertex -> number of vertices in graph
    def __init__(self,vertex):

        # create V x V matrix filled with 0
        self.mat = [[0]*vertex for x in range(vertex)]

        # store number of vertices
        self.size = vertex 


    # ---------------------------------------
    # Add Edge
    # ---------------------------------------
    # src  -> source vertex
    # dest -> destination vertex
    #
    # Since this is an UNDIRECTED graph:
    # we mark both directions

    def add_edge(self,src,dest):

        if 0 <= src < self.size and 0 <= dest < self.size:

            # mark edge
            self.mat[src][dest] = 1
            self.mat[dest][src] = 1

        else:
            print("invalid edge") 


    # ---------------------------------------
    # Print Adjacency Matrix
    # ---------------------------------------

    def print_mat(self):

        for row in self.mat:

            # map() converts elements to string
            # join() prints them with spaces
            print(' '.join(map(str,row)))


# ---------------------------------------
# Driver Code
# ---------------------------------------

G = Graph(5)

# adding edges
G.add_edge(0,1)
G.add_edge(0,2)
G.add_edge(1,3)
G.add_edge(2,4)
G.add_edge(2,3)
G.add_edge(3,4)

# print adjacency matrix
G.print_mat()
