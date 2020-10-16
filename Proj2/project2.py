"""
Math 560
Project 2
Fall 2020

project2.py

Partner 1: Yutong Zhang (yz566)
Partner 2: Jiaxi Yin (jy280)
Date:
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The shortest path from maze.start to maze.exit.
"""
def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')
    
    if alg == 'DFS':
        
        #Initalize all values
        for v in maze.adjList:
            v.visited = False
            v.prev = None
        
        #Create an empty stack
        stack = Stack()
        
        #Mark the start vertex as visited 
        maze.start.visited = True
        stack.push(maze.start)
        while not stack.isEmpty():
            current = stack.pop()
            
            #Push neighbors of current vertex to stack if not visited
            for v in current.neigh:
                if not v.visited:
                    v.visted = True
                    stack.push(v)
                    v.prev = current
                    
    else:
        
        #Initalize all values
        for v in maze.adjList:
            v.dist = math.inf
            v.prev = None
            
        #Create an empty queue
        queue = Queue()
        
        #Set the distance of the start vertex as 0
        maze.start.dist = 0
        queue.push(maze.start)
        while not queue.isEmpty():
            current = queue.pop()
            
            #Push neighbors of current vertex to queue if not visited
            for v in current.neigh:
                if v.dist == math.inf:
                    v.dist = current.dist + 1
                    queue.push(v)
                    v.prev = current
    path=[]
    v = maze.exit
    
    #Go backward to find the path until reaching the start vertex
    while v != None:
        
        path.append(v.rank)
        v = v.prev
    
        
        
    #Reverse the path to get the correct order from start to exit
    return path.reverse()
    

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)
