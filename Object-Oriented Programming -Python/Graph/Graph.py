#  File: Graph.py

#  Description: Completes some methods to traverse a graph of given properties.

#  Student Name: Shawn Hu

#  Student UT EID: sh42578

#  Partner Name: Aasim Rajabali

#  Partner UT EID: afr447

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 1 May 2015

#  Date Last Modified: 6 May 2015

import copy

def colEmpty(matrix,col_num):
    for row in matrix:
        if row[col_num] != 0:
            return False
    return True

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack)-1]

    def isEmpty(self):
        return (len(self.stack) == 0)

    def size(self):
        return len(self.stack)

class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        return (self.queue.pop(0))

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


class priorityQueue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)
        self.queue.sort

    def dequeue(self):
        return (self.queue.pop(0))

    def isEmpty(self):
        return len(self.queue) == 0

class Vertex(object):
    def __init__(self,label):
        self.label = label
        self.visited = False

    #determine if vertex was visited
    def wasVisited(self):
        return self.visited

    #determine the label of the vertex
    def getLabel(self):
        return self.label

    #string representation of the vertex
    def __str__(self):
        return str(self.label)

class Edge(object):
    def __init__(self, fr, to, weight = 1):
        self.fr = fr
        self.to = to
        self.weight = weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __add__(self, other):
        newEdge = Edge(self.fr, other.to, self.weight + other.weight)
        return newEdge

class Graph(object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    #check if a vertex already exists
    def hasVertex(self,label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).label):
                return True
        return False

    #given a label, get the index
    def getIndex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if ((self.Vertices[i]).getLabel() == label):
                return i
        return -1

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def getEdgeWeight(self,fromVertexLabel, toVertexLabel):
        fromVertex = self.getIndex(fromVertexLabel)
        toVertex = self.getIndex(toVertexLabel)
        num = self.adjMat[fromVertex][toVertex]
        if num == 0:
            return -1
        return num

    # get a list of neighbors that you can go to from a vertex
    # return empty list if there are none
    def getNeighbors(self, vertexLabel):
        neighbors = []
        vertex = self.getIndex(vertexLabel)
        nVert = len(self.Vertices)
        for i in range(nVert):
            if self.adjMat[vertex][i] == 0:
                continue
            else:
                neighbors.append(self.Vertices[i])
        return neighbors

    #get a copy of the list of vertices
    def getVertices(self):
        newList = list(self.Vertices)
        return newList

    def isCycleStartWith(self, Node):
        q1 = Queue()
        q1.enqueue(Node)
        visited  = []

        while not q1.isEmpty():
            v1 = q1.dequeue()
            neighbors = self.getNeighbors(v1)
            if Node in neighbors:
                return True
            visited.append(v1)
            for i in neighbors:
                if not i in visited:
                    q1.enqueue(i)
        return False

    #determine if the graph has a cycle
    def hasCycle(self):
        for i in self.Vertices:
            if self.isCycleStartWith(i):
                return True
        return False


    #return a list of vertices after a topological sort
    def toposort(self):
        matrix = copy.deepcopy(self.adjMat)
        vertices = copy.deepcopy(self.Vertices)
        if self.hasCycle():
            return None
        while matrix != []:
            happy = True
            for col in range (len(matrix)):
                #if we already removed something
                if not happy:
                    continue
                if colEmpty(matrix, col):
                    #indicates that we remove a row
                    happy = False
                    a = vertices[col].label
                    print(a)
                    #remove vertex entry
                    filler = vertices.pop(col)
                    #remove column
                    for row in matrix:
                        filler = row.pop(col)
                    #remove associated row
                    filler = matrix.pop(col)
        return



    #add a vertex given a label
    def addVertex(self,label):
        if not self.hasVertex(label):
            self.Vertices.append(Vertex(label))

            #add a new column in the adjacency matrix for the new vertex
            nVert = len(self.Vertices)
            for i in range(nVert-1):
                (self.adjMat[i]).append(0)

            #add a new row for the vertex in the adjacency matrix
            newRow = []
            for i in range(nVert):
                newRow.append(0)
            self.adjMat.append(newRow)

    #add weighted directed edge to graph
    def addDirectedEdge(self,start,finish,weight = 1):
        self.adjMat[start][finish] = weight

    #add weighted undirected edge to the graph
    def addUndirectedEdge(self,start,finish,weight = 1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    #return an unvisited vertex adjacent to vertex v
    def getAdjUnvisitedVertex(self,v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
                return i
        return -1

    #Depth first search in a graph
    def dfs(self,v):
        #create a stack
        theStack = Stack()

        #mark the vertex as visited and push on the stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theStack.push(v)

        while (not theStack.isEmpty()):
            #get an adjacent unvisited vertex
            u = self.getAdjUnvisitedVertex(theStack.peek())
            if u == -1:
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theStack.push(u)

        #the stack is empty, so reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    #Breadth first search in a graph
    def bfs(self,v):
        #create a queue
        theQueue = Queue()

        #mark the vertex as visited and enqueue
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theQueue.enqueue(v)

        while (not theQueue.isEmpty()):
            #get the vertex at the front
            v1 = theQueue.dequeue()
            #get an adjacent unvisited vertex
            v2 = self.getAdjUnvisitedVertex(v1)
            while (v2 != -1):
                (self.Vertices[v2]).visited = True
                print(self.Vertices[v2])
                theQueue.enqueue(v2)
                v2 = self.getAdjUnvisitedVertex(v1)

        #Queue is empty, so reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False


    def edgeList(self):
        numedges = 0
        mat = copy.deepcopy(self.adjMat)
        for row in mat:
            for element in row:
                if element != 0:
                    numedges += 1
        for x in range (numedges):
            a = leastelement(mat)
            for row in range (len(self.Vertices)):
                for col in range (len(self.Vertices)):
                    if mat[row][col] == leastelement(mat):
                        print (self.Vertices[row].label+ '--'+ self.Vertices[col].label, mat[row][col])
                        mat[row][col] = 0

    #like the getneighbors function but with indices
    def getNeighborIndices(self, index):
        mat = copy.deepcopy(self.adjMat)
        indxs = []
        for x in range (len(mat[index])):
            if mat[index][x] != 0:
                indxs.append([x, mat[index][x]])
        return indxs

    #will use a priority queue to always traverse the shortest path available, finding the shortest path to each notde visited
    def shortestPath(self, start):
        startIndex = self.getIndex(start)
        #makes it so that no place can travel back to the start, simplifying the print process later
        mat = copy.deepcopy(self.adjMat)
        vertices = copy.deepcopy(self.Vertices)
        pathlengths = list(float('inf') for x in range (len(vertices)))
        pathlengths[startIndex] = 0
        pq = priorityQueue()
        for x in range (len(vertices)):
            if mat[startIndex][x] != 0:
                newEdge = Edge(startIndex, x, mat[startIndex][x])
                pq.enqueue(newEdge)
        while not pq.isEmpty():
            branch = pq.dequeue()
            if branch.weight < pathlengths[branch.to]:
                pathlengths[branch.to] = branch.weight
                #horrible, horrible coding convention. I should never have written a helper function to do this.
                #for what it's worth, double[0] will be the index of a vertex you can go to,
                #double[1] will be the weight of the edge
                for double in self.getNeighborIndices(branch.to):
                    newEdge = Edge(branch.to, double[0], double[1])
                    newBranch = branch + newEdge
                    if newBranch.weight < pathlengths[double[0]]:
                        pq.enqueue(newBranch)

        for x in range (len(vertices)):
            if vertices[x].label == start:
                continue
            else:
                print(start+'->'+vertices[x].label, pathlengths[x])



def leastelement(mat):
    least = mat[0][0] + 10
    for row in mat:
        for element in row:
            if element < least and element > 0:
                least = element

    return least

def main():
    #create a graph
    cities = Graph()

    #open file for reading
    inFile = open("./graph.txt",'r')

    #read the vertices
    numVertices = int((inFile.readline()).strip())

    for i in range(numVertices):
        city = (inFile.readline()).strip()
        cities.addVertex(city)

    #read the edges
    numEdges = int((inFile.readline()).strip())

    for i in range(numEdges):
        edge = (inFile.readline()).strip()

        edge = edge.split()
        start = int(edge[0])
        finish = int(edge[1])
        weight = int(edge[2])
        cities.addDirectedEdge(start,finish,weight)

    #read the starting vertex for dfs and bfs
    startVertex = (inFile.readline()).strip()

    #close file
    inFile.close()

    #get index of the start vertex
    startIndex = cities.getIndex(startVertex)

    #do a depth first search
    print("\nDFS from", startVertex+':')
    cities.dfs (startIndex)

    #do a breadth first search
    print("\nBFS from", startVertex+':' )
    cities.bfs(startIndex)

    print("\nTopological Sort:")
    cities.toposort()

    print("\nAscending Edges:")
    cities.edgeList()

    print ('\nSSSP from', startVertex+':')
    cities.shortestPath(startVertex)

main()
