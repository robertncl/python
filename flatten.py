from typing import List, Any

def flatten(mylist: List[List[Any]]) -> List[Any]:
    """Flatten a list of lists into a single list."""
    return [one_element
            for one_sublist in mylist
            for one_element in one_sublist]

print(flatten([[1, 2], [3, 4]]))