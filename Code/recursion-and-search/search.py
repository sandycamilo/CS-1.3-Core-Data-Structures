#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    pass
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    #find the middle 
    #// = integer division - no float 
    # middle_index = len(array) // 2 
    #we need two pointers (left and right or high and low) they define the boundaries of the chunck we'll go through to find the target
    # *(low)                    *(high)
    left = 0 #start of array 
    right = len(array) - 1 #end of array 
    #compare target(item) to the middle item in the array - is it what we are looking for?
    #if the middle item is the item we are looking for then we return the location or index of the item - done!
    while left <= right: #while the left side from the middle point index is less than or equal to the right side 
        middle_index = len(array) // 2 #find the middle point by dividing the array 

        if item == array[middle_index]: #if the item is located at the index in the middle of the array
            return middle_index #return the location
    #now check if the item is less than the middle item - if it is then look in the left part of the array 
        elif item < array[middle_index]:
            #repeat the steps on the left
            #move the pointers 
            #it redefines the middle 
            right = middle_index - 1 
        elif item > array[middle_index]:
            #repeat the steps on the left 
            #move pointers 
            #redefine where the middle point stands 
            left = middle_index + 1 


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    #tells us there is a left and a right pointer - more info than the iterative 
    #we are making changes to the pointers - not declaring them in the function as they are being passed in 

    middle_index = (left + right) // 2 

    if item == array[middle_index]: #base case - if it finds target - stop repeating 
        return middle_index
    if left >= right: # second base case - if the left is greater than the right  - then return None 
        return None 

    #recursive cases 
    elif item < array[middle_index]:
        #move pointers
        right = middle_index - 1 
        #pass them in 
        return binary_search_recursive(array, item, left, right)
    elif item > array[middle_index]:
        #move pointers 
        left = middle_index + 1 
        return binary_search_recursive(array, item, left, right)

