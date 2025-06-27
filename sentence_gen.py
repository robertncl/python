import re
import reprlib
from typing import Iterator

RE_WORD = re.compile(r'\w+')


class Sentence:
    """A sequence of words extracted from a text, supporting iteration."""

    def __init__(self, text: str) -> None:
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self) -> str:
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self) -> Iterator[str]:
        for word in self.words:  
            yield word  
        return  

def sentence_gen(words: list[str]) -> Iterator[str]:
    """Yield each word in the list as a sentence (capitalized and with a period)."""
    for word in words:
        yield word.capitalize() + '.'

# done! 
