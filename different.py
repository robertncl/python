from typing import List

def how_many_different_numbers(numbers: List[int]) -> int:
    """Return the number of unique numbers in the list."""
    unique_numbers = set(numbers)
    return len(unique_numbers)

print(how_many_different_numbers([1, 2, 3, 1, 2, 3, 4, 1]))