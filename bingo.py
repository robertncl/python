import random
from collections.abc import Iterable
from typing import Any

from tombola import Tombola


class BingoCage(Tombola):
    """A bingo cage that shuffles and picks items."""
    def __init__(self, items: Iterable[Any]) -> None:
        self._items: list[Any] = []
        self.load(items)

    def load(self, items: Iterable[Any]) -> None:
        """Add items to the cage and reshuffle."""
        self._items.extend(items)
        random.shuffle(self._items)

    def pick(self) -> Any:
        """Pick an item from the cage, raising LookupError if empty."""
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self) -> Any:
        """Allow the cage to be called to pick an item."""
        return self.pick()

def bingo_numbers(numbers: list[int]) -> list[int]:
    """Return a sorted list of bingo numbers (1-75) from the input list."""
    return sorted([n for n in numbers if 1 <= n <= 75])
