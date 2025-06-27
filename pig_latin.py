def pig_latin(word: str) -> str:
    """Convert a word to Pig Latin."""
    if word[0] in 'aeiou':
        return word + 'way'
    return word[1:] + word[0] + 'ay'
 
 
print(pig_latin('eat'))
