import random
from collections.abc import Sequence
from typing import Protocol, TypeVar, runtime_checkable

from randompick import RandomPicker


@runtime_checkable
class LoadableRandomPicker(RandomPicker, Protocol):
    def load(self, items) -> None: ...

T = TypeVar('T')

def random_pick_load(seq: Sequence[T]) -> T:
    """Return a random element from a non-empty sequence (load version)."""
    return random.choice(seq)
