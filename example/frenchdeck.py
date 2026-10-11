import collections
from typing import ClassVar

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks: ClassVar[list[str]] = [str(n) for n in range(2, 11)] + list('JQKA')
    suits: ClassVar[list[str]] = ['spades', 'diamonds', 'clubs', 'hearts']

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
