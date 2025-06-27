import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    """A sequence of words extracted from a text."""

    def __init__(self, text: str) -> None:
        self.text = text
        self.words = RE_WORD.findall(text)  

    def __getitem__(self, index: int) -> str:
        return self.words[index]  

    def __len__(self) -> int:  
        return len(self.words)

    def __repr__(self) -> str:
        return 'Sentence(%s)' % reprlib.repr(self.text)  

def sentence(words: list[str]) -> str:
    """Return a sentence formed by joining a list of words with spaces and capitalizing the first letter."""
    return ' '.join(words).capitalize() + '.'  