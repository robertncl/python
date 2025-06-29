# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
    """
    This function performs a binary search on the given sorted array to find the location of the target value x.

    Parameters:
    arr (list): The sorted array in which to perform the binary search.
    l (int): The leftmost index of the search range.
    r (int): The rightmost index of the search range.
    x (int): The target value to be searched in the array.

    Returns:
    int: The index of the target value x in the array if found, otherwise returns -1.
    """
    while l <= r:

        mid = l + (r - l) // 2  # extracting the middle element from the array
        mid = int(mid)  # it has to be integer

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1  # l is initialized to the rightmost element of the middle so that the search could be started from there the next time

        # If x is smaller, ignore right half
        elif x < arr[mid]:
            r = mid - 1  # r is initialized to the leftmost element of the middle so that the search goes till there only the next time

    # If we reach here, then the element was not present
    return -1


# Main Function
if __name__ == "__main__":
    # User input array
    print("Enter the array with comma separated in which element will be searched")
    arr =[int(x) for x in input().split(',')] #the input array will of int type with each element seperated with a comma due to the split fucntion
                                       #map function returns a list of results after applying the given function to each item
    x = int(input("Enter the element you want to search in given array"))

    # Function call
    result = binarySearch(arr, 0, len(arr) - 1, x)
     
    #printing the output
    if result != -1:
        print("Element is present at index {}".format(result))
    else:
        print("Element is not present in array")