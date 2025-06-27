import itertools
from typing import Any
from tombola import Tombola
from bingo import BingoCage


class AddableBingoCage(BingoCage):  
    """A BingoCage that supports addition and in-place addition with other Tombola or iterables."""

    def __add__(self, other: Any) -> 'AddableBingoCage':
        if isinstance(other, Tombola):  
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other: Any) -> 'AddableBingoCage':
        if isinstance(other, Tombola):
            other_iterable = other.inspect()  
        else:
            try:
                other_iterable = iter(other)  
            except TypeError:  6
                self_cls = type(self).__name__
                msg = "right operand in += must be {!r} or an iterable"
                raise TypeError(msg.format(self_cls))
        self.load(other_iterable)  
        return self  