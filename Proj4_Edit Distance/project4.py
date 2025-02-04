"""
Math 560
Project 4
Fall 2020

Partner 1: Yutong Zhang(yz566)
Partner 2: Jiaxi Yin(jy280)
Date: 10/27/2020
"""

# Import p4tests.
from p4tests import *

################################################################################

"""
ED: the edit distance function
Inputs:
    src: the original string
    dest: the string to convert to
"""
def ED(src, dest):

    edits = []
    
    M = len(src)
    N = len(dest)
    
    #Initialize the DP table
    D = [[0 for x in range(0,N+1)] for x in range(0,M+1)]
    
    #Base case: set the values of first row and first column as index number
    for i in range(M+1):
        D[i][0] = i
    for j in range(N+1):
        D[0][j] = j
    
    
    for i in range(1, M+1):
        for j in range(1,N+1):
            #If the two comparing symbols are the same,
            #there's no operation.
            if src[i-1] == dest[j-1]:
                D[i][j] = D[i-1][j-1]
            else:
                #Update D[i][j] from three previous cases
                min_value = min(D[i][j-1], D[i-1][j], D[i-1][j-1])
                D[i][j] = 1 + min_value

# Track the path of edits implemented                
    i = M
    j = N
    while i > 0 and j > 0:
        if src[i-1] == dest[j-1]: 
            #Last symbols match, trace bcak to diagonal
            edits.append(('match', str(src[i-1]), i-1))
            i -= 1
            j -= 1
        else: 
            #Find where the minimum came from and trace back
            if D[i][j-1] + 1 == D[i][j]:
                #Minimum came from left cell
                edits.append(('insert', str(dest[j-1]), i))
                j -= 1
            elif D[i-1][j] + 1 == D[i][j]:
                #Minimum came from upper cell
                edits.append(('delete', str(src[i-1]), i-1))
                i -=1
            else:
                #Minimum came from diagonal cell
                edits.append(('sub', str(dest[j-1]), i-1))
                i -= 1
                j -= 1
    #The operations are all in first row
    while j > 0:
        edits.append(('insert', str(dest[j-1]), i))
        j -= 1
    #The operations are all in first column
    while i > 0:
        edits.append(('delete', str(src[i-1]), i-1))
        i -= 1
       
    dist = D[M][N]
    
    return dist, edits

################################################################################

"""
Main function.
"""
if __name__ == "__main__":
    edTests(False)
    print()
    compareGenomes(True, 30, 300)
    print()
    compareRandStrings(True, 30, 300)
