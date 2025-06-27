from collections import Counter
import operator

WORDS = ['this', 'is', 'an',
         'elementary', 'test', 'example']

def most_repeating_letter_count(word):            
    return Counter(word).most_common(1)[0][1]                


def most_repeating_word(words):
    return max(words, key=most_repeating_letter_count)

print(most_repeating_word(WORDS))

def is_word_palindrome(word: str) -> bool:
    """Return True if the word is a palindrome."""
    return word == word[::-1]