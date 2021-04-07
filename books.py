from typing import TypedDict, List
import json

class BookDict(TypedDict):
    isbn: str
    title: str
    authors: List[str]
    pagecount: int