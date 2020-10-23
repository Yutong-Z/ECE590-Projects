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
    ##### Your implementation goes here. #####
    return []
    ##### Your implementation goes here. #####

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
