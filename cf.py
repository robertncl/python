#!/usr/bin/env python3
import sys
import unicodedata
from typing import Set

FIRST, LAST = ord(' '), sys.maxunicode

def find(*query_words: str, first: int = FIRST, last: int = LAST) -> None:
    """Find and print Unicode characters whose names contain all query words."""
    query: Set[str] = {w.upper() for w in query_words}
    count = 0
    for code in range(first, last + 1):
        char = chr(code)
        name = unicodedata.name(char, None)
        if name and query.issubset(name.split()):
            print(f'U+{code:04X}\t{char}\t{name}')
            count += 1
    print(f'({count} found)')

def main(words: list[str]) -> None:
    """Main entry point for the Unicode character finder."""
    if words:
        find(*words)
    else:
        print('Please provide words to find.')

def cf(a: int, b: int) -> int:
    """Return the continued fraction of a and b (greatest common divisor)."""
    while b:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    main(sys.argv[1:])