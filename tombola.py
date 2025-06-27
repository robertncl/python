import abc
from typing import Any

class Tombola(abc.ABC):  

    @abc.abstractmethod
    def load(self, iterable):  
        """Add items from an iterable."""

    @abc.abstractmethod
    def pick(self):  
        """Remove item at random, returning it.

        This method should raise `LookupError` when the instance is empty.
        """

    def loaded(self):  
        """Return `True` if there's at least 1 item, `False` otherwise."""
        return bool(self.inspect())  


    def inspect(self):
        """Return a sorted tuple with the items currently inside."""
        items = []
        while True:  
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)  
        return tuple(sorted(items))

def tombola_draw(items: list[Any]) -> Any:
    """Draw and return a random item from the tombola (placeholder logic)."""
    if not items:
        return None
    return items[0]