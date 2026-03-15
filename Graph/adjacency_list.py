# ---------------------------------------
# Graph Representation using Adjacency List
# ---------------------------------------

'''
Docstring for Adjacency List

Advantage:
If the graph is SPARSE (few edges),
memory wastage is very low compared to adjacency matrix.

Disadvantage:
If the graph is DENSE (many edges),
adjacency matrix may be better since lists become large.

Graph Degree

In Directed Graph:
degree = indegree + outdegree

indegree  -> number of incoming edges
outdegree -> number of outgoing edges

In Undirected Graph:
degree = number of connected edges
'''

class Graph:

    # ---------------------------------------
    # Constructor
    # ---------------------------------------
    # adjList is a dictionary where:
    # key   -> vertex
    # value -> list of connected vertices
    def __init__(self):
        self.adjList = {}


    # ---------------------------------------
    # Add Vertex
    # ---------------------------------------
    # Creates a vertex if it doesn't exist
    def add_vertex(self,vertex):

        if vertex not in self.adjList:
            self.adjList[vertex] = []


    # ---------------------------------------
    # Add Edge
    # ---------------------------------------
    # src  -> source vertex
    # dest -> destination vertex
    #
    # This implementation represents an
    # UNDIRECTED GRAPH, so both directions are added
    def addEdge(self,src,dest):

        # ensure vertices exist
        self.add_vertex(src)
        self.add_vertex(dest)

        # add connection
        self.adjList[src].append(dest)

        # because graph is undirected
        self.adjList[dest].append(src)


    # ---------------------------------------
    # Print Graph
    # ---------------------------------------
    # Displays adjacency list structure
    def printG(self):

        for vertex in self.adjList:
            print(vertex, "->", self.adjList[vertex], end="\n")


# ---------------------------------------
# Driver Code
# ---------------------------------------

g = Graph()

# adding edges
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(1,4)
g.addEdge(4,3)
g.addEdge(2,4)
g.addEdge(4,5)
g.addEdge(3,5)

# print adjacency list
g.printG()
    