"""
Math 560
Project 3
Fall 2020

Partner 1: Yutong Zhang (yz566)
Partner 2: Jiaxi Yin (jy280)
Date: 22/10/2020
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
    # Set initial dist and prev
    for v in adjList:
        v.dist = math.inf
        v.prev = None
    adjList[0].dist = 0
    
    # Iterate |V|-1 times
    for iter in range(0, len(adjList)-1):
        
        # Look at each vertex
        for v in adjList:
            
            # Check each neighbor of v
            # Update predictions and previous vertex
            for neigh in v.neigh:
                # Only update id the new value is better
                if neigh.dist > v.dist + adjMat[v.rank][neigh.rank] + tol:
                    neigh.dist = v.dist + adjMat[v.rank][neigh.rank]
                    neigh.prev = v
    
    # Iterate One more time to check negative cost cycle
    changed = []
    for v in adjList:
        for neigh in v.neigh:
            if neigh.dist > v.dist + adjMat[v.rank][neigh.rank] + tol:
                neigh.dist = v.dist + adjMat[v.rank][neigh.rank]
                neigh.prev = v
                changed.append(neigh)
    
    # If there is negative cost cycle
    if len(changed)>0:
        # Find a vertex in the cycle by checking double appearance
        app = [0 for vertex in adjList]
        # Randomly select a changed vertex changed
        v = changed[0]
        # Trace back to find a vertex in cycle, name it v0
        while app[v.rank] != 2:
            app[v.rank] += 1
            v = v.prev
        v0 = v
        
        # Trace back from v0 to find the arbitrage path
        path = [v0.rank]
        while v.prev != v0:
            v  = v.prev
            path.append(v.rank)
        path.append(v.prev.rank)
        # Reverse the trace back path to get the original path
        path.reverse()
        return path
    
    # Return empty list if there is not negative cost cycle
    else:
        return []

################################################################################

"""
rates2mat
"""
def rates2mat(rates):
    # Returns the adjacency matrix with the weighted edges converted from exchange rates.
    return [[-math.log(R) for R in row] for row in rates]

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
