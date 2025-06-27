import bisect
import sys
from typing import Callable, List

HAYSTACK: List[int] = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES: List[int] = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn: Callable[[List[int], int], int]) -> None:
    """Demonstrate bisect function with NEEDLES and HAYSTACK."""
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))

def insert_sorted(a: List[int], x: int) -> None:
    """Insert x into list a, keeping it sorted."""
    bisect.insort(a, x)

if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join(f'{n:2}' for n in HAYSTACK))
    demo(bisect_fn)