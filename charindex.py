import sys
import re
import unicodedata
from typing import Dict, Set, Iterator

RE_WORD = re.compile(r'\w+')
STOP_CODE = sys.maxunicode + 1

def tokenize(text: str) -> Iterator[str]:
    """Return iterable of uppercased words from the input text."""
    for match in RE_WORD.finditer(text):
        yield match.group().upper()

def name_index(start: int = 32, end: int = STOP_CODE) -> Dict[str, Set[str]]:
    """Return a dictionary mapping words to sets of Unicode characters."""
    index: Dict[str, Set[str]] = {}
    for char in (chr(i) for i in range(start, end)):
        if name := unicodedata.name(char, ''):
            for word in tokenize(name):
                index.setdefault(word, set()).add(char)
    return index

def char_index(s: str, char: str) -> int:
    """Return the index of the first occurrence of char in s, or -1 if not found."""
    return s.find(char)