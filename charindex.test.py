import unittest
from typing import Iterator
from charindex import tokenize

class TestTokenize(unittest.TestCase):
    
    def test_tokenize_empty_string(self):
        """
        Test the tokenize function with an empty string input.

        This test case verifies that the tokenize function returns an empty list
        when given an empty string as input.

        Returns:
        None

        Raises:
        AssertionError: If the result is not an empty list.
        """
        result = list(tokenize(""))
        self.assertEqual(result, [], "Expected an empty list for an empty input string")
    
    
    def test_tokenize_single_word(self):
        result = list(tokenize("hello"))
        self.assertEqual(result, ["HELLO"])
    
    def test_tokenize_multiple_words(self):
        result = list(tokenize("Hello World"))
        self.assertEqual(result, ["HELLO", "WORLD"], "Expected two uppercased words")
    
    def test_tokenize_with_punctuation(self):
        result = list(tokenize("Hello, World!"))
        self.assertEqual(result, ["HELLO", "WORLD"], "Expected two uppercased words, ignoring punctuation")
    
    def test_tokenize_with_numbers(self):
        result = list(tokenize("Hello123 World456"))
        self.assertEqual(result, ["HELLO123", "WORLD456"], "Expected two uppercased words with numbers")

def test_name_index_default_end_value(self):
    """
    Test the name_index function with a default end value.

    This test case verifies that the name_index function produces a non-empty result
    when called with only a start value, and that the result includes characters
    beyond the ASCII range.

    Parameters:
    self (TestCase): The test case instance.

    Returns:
    None

    Raises:
    AssertionError: If the result is empty or doesn't contain Unicode characters.
    """
    result = name_index(start=32)
    self.assertGreater(len(result), 0, "Expected non-empty result")

    # Check if the result contains characters beyond ASCII range
    unicode_chars = set()
    for char_set in result.values():
        unicode_chars.update(char for char in char_set if ord(char) > 127)

    self.assertGreater(len(unicode_chars), 0, "Expected characters beyond ASCII range")

if __name__ == "__main__":
    unittest.main()
