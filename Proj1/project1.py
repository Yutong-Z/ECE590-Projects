"""
Math 560
Project 1
Fall 2020

Partner 1: Yutong Zhang (yz566)
Partner 2: Jiaxi Yin (jy280)
Date: 10/7/2020
"""

"""
SelectionSort
"""
def SelectionSort(listToSort):
    '''
    The function SelectionSort use selection sort algorithm to
    do in-place sort an array in ascending order
    inputs:
        listToSort: list, it is a list that needs to be sorted
    output:
        listToSort: list, the sorted list

    '''
    n = len(listToSort)
    #scan n times
    for i in range(n):  
        key = i
        for j in range(i+1, n):      
            #update the index of the smaller value
            if listToSort[j] < listToSort[key]: 
                key = j
        #change the smallest value to he index i
        listToSort[i], listToSort[key] = listToSort[key], listToSort[i]
    return listToSort

"""
InsertionSort
"""
def InsertionSort(listToSort):
    '''
    The function InsertionSort use insertion sort algorithm to
    do in-place sort an array in ascending order
    inputs:
        listToSort: list, it is a list that needs to be sorted
    output:
        listToSort: list, the sorted list

    '''
    n = len(listToSort)
    #scan n-1 times
    for i in range(1,n):
        #save the number to insert to the variable cNum
        cNum = listToSort[i]
        key = i-1
        #move numbers larger than cNum backward
        while key >= 0 and listToSort[key]>cNum:
            #move numbers larger than cNum backward
            listToSort[key+1] = listToSort[key]
            key -= 1
        #insert cNum to the correct position
        listToSort[key+1] = cNum
    return listToSort

"""
BubbleSort
"""
def BubbleSort(listToSort):
    '''
    The function BubbleSort use bubble sort algorithm to
    do in-place sort an array in ascending order
    inputs:
        listToSort: list, it is a list that needs to be sorted
    output:
        listToSort: list, the sorted list

    '''
    n = len(listToSort)
    for i in range(n):
        #boolean to check if any swaps are made in each round of iteration
        swap = 0
        for j in range(1, n-i):
            if listToSort[j-1] > listToSort[j]:
                #swap if two adjacent elements are out of order
                listToSort[j-1], listToSort[j] = listToSort[j], listToSort[j-1]
                swap = 1
        #stop iterating through the array if no swaps are made in previous round        
        if swap == 0:
            break
    return listToSort

"""
MergeSort
"""
def MergeSort(listToSort):
    '''
    The function MergeSort use merge sort algorithm to
    do in-place sort an array in ascending order
    inputs:
        listToSort: list, it is a list that needs to be sorted
    output:
        listToSort: list, the sorted list

    '''
    n = len(listToSort)
    #Arrays with length not greater than 1 are ordered
    if n <= 1:
        return listToSort
    median = int(n/2)
    #Apply MergeSort to left half and right half respectively
    left = MergeSort(listToSort[:median])
    right = MergeSort(listToSort[median:])    
    sorted_list = []
    i, j = 0, 0
    #Merge the two arrays in ascending order
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    #The remaining numbers are added directly to the end
    sorted_list += left[i:]
    sorted_list += right[j:]
    listToSort[0:len(listToSort)] = sorted_list[0:len(sorted_list)]
    return listToSort

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""

def QuickSort(listToSort, i=0, j=None):
    '''
    The function QuickSort use quick sort algorithm to
    do in-place sort an array in ascending order
    inputs:
        listToSort: list, it is a list that needs to be sorted
    output:
        listToSort: list, the sorted list

    '''
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)
    # base case
    if i >= j:
        return
    else:
        l = i
        r = j
        # set the pivot as the middle element
        pivot = listToSort[(i+j)//2]
        # partition the array based on pivot
        while l<=r-1:
            while l<=r-1 and listToSort[l]<pivot:
                l += 1
            while l<=r-1 and listToSort[r-1]>pivot:
                r -= 1
            if l<=r-1:
                # swap disorder element to make sure left part list has elements smaller than pivot
                # right part list has elements larger than pivot
                listToSort[l], listToSort[r-1] = listToSort[r-1], listToSort[l]
                # move pointers further after each swap to allow repeated elements
                l += 1
                r -= 1
        QuickSort(listToSort, i, r)
        QuickSort(listToSort, l, j)


"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('DEFAULT measureTime')
    print()
    measureTime()