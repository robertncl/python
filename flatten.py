from typing import Any

def flatten(nested_list: list[Any]) -> list[Any]:
    """Flatten a nested list into a single list."""
    result = []
    for sublist in nested_list:
        if isinstance(sublist, list):
            result.extend(flatten(sublist))
        else:
            result.append(sublist)
    return result

print(flatten([[1, 2], [3, 4]]))