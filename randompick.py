import random
from typing import Any, Iterable, Sequence, TypeVar

from randompick import RandomPicker

T = TypeVar('T')

class SimplePicker():
    def __init__(self, items: Iterable) -> None:
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self) -> Any:
        return self._items.pop()


def test_isinstance() -> None:
    popper = SimplePicker([1])
    assert isinstance(popper, RandomPicker)


def test_item_type() -> None:
    items = [1, 2]
    popper = SimplePicker(items)
    item = popper.pick()
    assert item in items
    assert isinstance(item, int)


def random_pick(seq: Sequence[T]) -> T:
    """Return a random element from a non-empty sequence."""
    return random.choice(seq)