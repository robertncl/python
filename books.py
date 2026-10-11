import json
from typing import TypedDict


class BookDict(TypedDict):
    """A dictionary type for representing a book."""
    isbn: str
    title: str
    authors: list[str]
    pagecount: int

AUTHOR_ELEMENT = '<AUTHOR>{}</AUTHOR>'


def to_xml(book: BookDict) -> str:
    """Return an XML representation of a book."""
    elements: list[str] = []
    for key, value in book.items():
        if isinstance(value, list):
            elements.extend(AUTHOR_ELEMENT.format(n) for n in value)
        else:
            tag = key.upper()
            elements.append(f'<{tag}>{value}</{tag}>')
    xml = '\n\t'.join(elements)
    return f'<BOOK>\n\t{xml}\n</BOOK>'


def from_json(data: str) -> BookDict:
    """Parse a JSON string into a BookDict."""
    whatever: BookDict = json.loads(data)
    return whatever

def book_titles(books: list[dict[str, str]]) -> list[str]:
    """Return a list of book titles from a list of book dictionaries."""
    return [book['title'] for book in books if 'title' in book]
