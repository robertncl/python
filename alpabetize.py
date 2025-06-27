import operator
from typing import List, Dict

PEOPLE = [{'first': 'Reuven', 'last': 'Lerner',
           'email': 'reuven@lerner.co.il'},
          {'first': 'Donald', 'last': 'Trump',
           'email': 'president@whitehouse.gov'},
          {'first': 'Vladimir', 'last': 'Putin',
           'email': 'president@kremvax.ru'}
          ]

def alphabetize_names(list_of_dicts: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Return a list of dictionaries sorted by last, then first name."""
    return sorted(list_of_dicts,
        key=operator.itemgetter('last', 'first'))

print(alphabetize_names(PEOPLE))