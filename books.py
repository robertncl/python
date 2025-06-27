from typing import TypedDict, List
import json

class BookDict(TypedDict):
    """A dictionary type for representing a book."""
    isbn: str
    title: str
    authors: List[str]
    pagecount: int