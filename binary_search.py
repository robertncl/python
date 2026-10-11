# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, left, right, x):
    """
    Perform a binary search on the given sorted array to find the location
    of the target value x.

    Parameters:
    arr (list): The sorted array in which to perform the binary search.
    left (int): The leftmost index of the search range.
    right (int): The rightmost index of the search range.
    x (int): The target value to be searched in the array.

    Returns:
    int: The index of the target value x in the array if found, otherwise returns -1.
    """
    while left <= right:

        mid = left + (right - left) // 2  # extracting the middle element from the array
        mid = int(mid)  # it has to be integer

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            # move left past the middle so the next search starts from there
            left = mid + 1

        # If x is smaller, ignore right half
        elif x < arr[mid]:
            # move right before the middle so the next search stops there
            right = mid - 1

    # If we reach here, then the element was not present
    return -1


# Main Function
if __name__ == "__main__":
    # User input array
    print("Enter the array with comma separated in which element will be searched")
    # the input array is of int type, with elements separated by commas
    arr = [int(x) for x in input().split(',')]
    x = int(input("Enter the element you want to search in given array"))

    # Function call
    result = binarySearch(arr, 0, len(arr) - 1, x)

    #printing the output
    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in array")
