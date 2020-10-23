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
    
    # trace back to find the arbitrage path
    # remove any vertices that are not part of the cycle (HOW???)
    v = changed[0] # randomly select a changed vertex???
    path = []
    while v.prev != changed[0]:
        path.append(v)
    path.reverse()
    return path

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
