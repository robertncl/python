import unittest
from typing import Iterator
from charindex import tokenize

class TestTokenize(unittest.TestCase):
    
    def test_tokenize_empty_string(self):
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

if __name__ == "__main__":
    unittest.main()
