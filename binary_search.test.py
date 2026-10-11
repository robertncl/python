from binary_search import binarySearch


def test_binary_search_positive_case():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    left = 0
    right = len(arr) - 1
    x = 5
    assert binarySearch(arr, left, right, x) == 4

    arr = [1, 1, 2, 3, 5, 8, 13, 14, 15, 17]
    left = 0
    right = len(arr) - 1
    x = 8
    assert binarySearch(arr, left, right, x) == 5

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    left = 0
    right = len(arr) - 1
    x = 10
    assert binarySearch(arr, left, right, x) == 9

def test_binary_search_negative_case():
    arr = [1, 2, 3, 4, 5]
    left = 0
    right = len(arr) - 1
    x = 0
    assert binarySearch(arr, left, right, x) == -1
