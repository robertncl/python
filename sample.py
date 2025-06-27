from random import shuffle
from typing import Sequence, List, TypeVar

T = TypeVar('T')

def sample(population: Sequence[T], size: int) -> List[T]:
    if size < 1:
        raise ValueError('size must be >= 1')
    result = list(population)
    shuffle(result)
    return result[:size]

def sample(items: list[int]) -> int:
    """Return the first item from a list of integers, or 0 if the list is empty."""
    return items[0] if items else 0