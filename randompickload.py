from typing import Protocol, runtime_checkable
from randompick import RandomPicker
import random
from typing import TypeVar
from collections.abc import Sequence

@runtime_checkable
class LoadableRandomPicker(RandomPicker, Protocol):
    def load(self, items) -> None: ... 

T = TypeVar('T')

def random_pick_load(seq: Sequence[T]) -> T:
    """Return a random element from a non-empty sequence (load version)."""
    return random.choice(seq) 