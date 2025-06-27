from typing import TypedDict, List
import json

class BookDict(TypedDict):
    """A dictionary type for representing a book."""
    isbn: str
    title: str
    authors: List[str]
    pagecount: int

def book_titles(books: list[dict[str, str]]) -> list[str]:
    """Return a list of book titles from a list of book dictionaries."""
    return [book['title'] for book in books if 'title' in book]