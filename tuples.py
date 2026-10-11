import operator

PEOPLE = [
    ('Donald', 'Trump', 7.85),
    ('Vladimir', 'Putin', 3.626),
    ('Jinping', 'Xi', 10.603)
]

def format_sort_records(list_of_tuples: list[tuple[str, str, float]]) -> list[str]:
    """Return a list of formatted strings sorted by last, then first name."""
    output = []
    template = '{1:10} {0:10} {2:5.2f}'
    for person in sorted(list_of_tuples, key=operator.itemgetter(1, 0)):
        output.append(template.format(*person))
    return output

print('\n'.join(format_sort_records(PEOPLE)))