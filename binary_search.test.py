def test_binary_search_positive_case():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l = 0
    r = len(arr) - 1
    x = 5
    assert binarySearch(arr, l, r, x) == 5

    arr = [1, 1, 2, 3, 5, 8, 13, 14, 15, 17]
    l = 0
    r = len(arr) - 1
    x = 8
    assert binarySearch(arr, l, r, x) == 6

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    l = 0
    r = len(arr) - 1
    x = 10
    assert binarySearch(arr, l, r, x) == 9
    
def test_binary_search_negative_case():
    arr = [1, 2, 3, 4, 5]
    l = 0
    r = len(arr) - 1
    x = 0
    assert binarySearch(arr, l, r, x) == -1