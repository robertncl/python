def demo() -> None:
    """
    Demonstrates the conversion of JSON to a dictionary and then to XML.

    This function creates a JSON string representing a non-standard book object,
    converts it to a dictionary, performs type checking (if enabled),
    prints the dictionary and a specific field, and finally converts
    the dictionary to XML and prints the result.

    Parameters:
    None

    Returns:
    None
    """
    NOT_BOOK_JSON = """
        {"title": "Andromeda Strain",
         "flavor": "pistachio",
         "authors": true}
    """
    not_book = from_json(NOT_BOOK_JSON)  
    if TYPE_CHECKING:  
        reveal_type(not_book)
        reveal_type(not_book['authors'])

    print(not_book)  
    print(not_book['flavor'])  

    xml = to_xml(not_book)  
    print(xml)