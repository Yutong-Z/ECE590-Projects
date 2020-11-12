
"""
Math 560
Project 5
Fall 2020

Partner 1: Yutong Zhang(yz566)
Partner 2: Jiaxi Yin(jy280)
Date: 11/13/2020
"""

# Import math, itertools, and time.
import math
import itertools
import time

# Import the Priority Queue.
from p5priorityQueue import *

################################################################################

"""
Prim's Algorithm
"""


def prim(adjList, adjMat):
   
    # Initialize all costs to infinity and prev to null
    for v in adjList:
        v.prev = None
        v.cost = math.inf
        v.visited = False
        
    #Pick an arbitrary start vertex(here pick the first one) and set cost to 0
    start = adjList[0]
    start.cost = 0
    
    #Make the priority queue using cost for sorting
    Q = PriorityQueue(adjList)
    while not Q.isEmpty():
        #Get the next unvisited vertex and visit it
        v = Q.deleteMin()
        v.visited = True
        #For each edge out of v
        for neighbor in v.neigh:
            #If the edge leads out, update
            if not neighbor.visited:
                if neighbor.cost > adjMat[v.rank][neighbor.rank]:
                    neighbor.cost = adjMat[v.rank][neighbor.rank]
                    neighbor.prev = v
    
    return


################################################################################

"""
Kruskal's Algorithm
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.
"""
def kruskal(adjList, edgeList):
    # Initialize all singleton sets for each vertex
    for v in adjList:
        makeset(v)
    #Initialize the empty MST    
    X = []
    
    # Loop through the sorted edges in increasing order
    for e in edgeList:
        #If the min edge crosses a cut, add it to our MST
        u, v =  e.vertices
        if not find(u).isEqual(find(v)):
            X.append(e)
            union(u, v)
     
    return X

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.
"""
def makeset(v):
    
    v.pi = v
    v.height = 0
    
    return

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.

"""
def find(v):
    
    while not v.isEqual(v.pi):
        v = v.pi
    
    return v.pi

"""
union: this function will union the sets of vertices v and u.
"""
def union(u,v):
    #Find the root of u and root of v
    ru = find(u)
    rv = find(v)
    
    #If the sets are the same, return
    if ru.isEqual(rv):
        return 
    
    #Let shorter one point to the other
    if ru.height > rv.height:
        rv.pi = ru
    elif ru.height < rv.height:
        ru.pi = rv
        
    #Same height
    else:
        ru.pi = rv
        
        #Increse rv.height by 1
        rv.height += 1
    
    return

################################################################################

"""
TSP
"""
def tsp(adjList, start):
    #Initialize empty tour list
    tour = []
    #Falg all vertices as unvisited
    for v in adjList:
        v.visited = False
    
    #Initialize a stack list for DFS
    stack = []
    #Arbitrarily select a start vertex
    stack.append(adjList[0])
    
    #While there are vertices left to visit
    while len(stack)!=0:
        #Pop the last vertex in stck list, and put it in tour list
        curr = stack.pop(-1)
        curr.visited = True
        tour.append(curr.rank)
        
        #For each MST neighbor of curr
        for neigh in curr.mstN:
            #Push only unvisited neigbor into stack
            if neigh.visited == False:
                stack.append(neigh)
    
    #Append start vertex into tour
    tour.append(adjList[0].rank)
    
    return tour

################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p5tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
