import operator

PEOPLE = [{'first': 'Reuven', 'last': 'Lerner',
           'email': 'reuven@lerner.co.il'},
          {'first': 'Donald', 'last': 'Trump',
           'email': 'president@whitehouse.gov'},
          {'first': 'Vladimir', 'last': 'Putin',
           'email': 'president@kremvax.ru'}
          ]

def alphabetize_names(list_of_dicts: list[dict[str, str]]) -> list[dict[str, str]]:
    """Return a list of dictionaries sorted by last, then first name."""
    return sorted(list_of_dicts,
        key=operator.itemgetter('last', 'first'))

print(alphabetize_names(PEOPLE))

def alphabetize(words: list[str]) -> list[str]:
    """Return a sorted list of words in alphabetical order."""
    return sorted(words)
