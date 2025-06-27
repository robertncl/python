def pl_sentence(words: list[str]) -> str:
    """Return a sentence in Pig Latin from a list of words."""
    return ' '.join(words) + '.'

print(pl_sentence(['this', 'is', 'a', 'test']))
