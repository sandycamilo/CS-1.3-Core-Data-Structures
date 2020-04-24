
def binary_search_iterative(array, item):
    # PSEUDO:
    # [5,6,7,10,12]  target 6 
    # find the middle position/item
    # check if middle item is the target, if so return 
    # else compare the target to the item at the middle
    # if target is less than item at the middle we ignore the right half
    # if the target is greater we ignore the left half
    # repeat until target is found or looked through everything

    left_index = 0
    right_index = len(array) - 1 
    mid_index = (right_index + left_index) // 2

    if array[mid_index] == item:
        return mid_index
    # if item < array[mid_index] 
    elif item < array[mid_index]:
        right_index = mid_index - 1 # ignore the right by reassigning the right index 
    # if item > array[mid_index
    elif item > array[mid_index]:  
        left_index = mid_index + 1  # ignore left

     