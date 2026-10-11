import glob
import json
from typing import Any


def print_scores():
    scores = {}
    for filename in glob.glob('*.json'):
        scores[filename] = {}
        with open(filename) as infile:
            for result in json.load(infile):
                for subject, score in result.items():
                    scores[filename].setdefault(subject, [])
                    scores[filename][subject].append(score)
    for one_class, class_scores in scores.items():
        print(one_class)
        for subject, subject_scores in class_scores.items():
            min_score = min(subject_scores)
            max_score = max(subject_scores)
            average_score = (sum(subject_scores) / len(subject_scores))
            print(f'{subject}')
            print(f'\tmin {min_score}')
            print(f'\tmax {max_score}')
            print(f'\taverage {average_score}')

def print_json(data: Any) -> None:
    """Print the given data as formatted JSON."""
    print(json.dumps(data, indent=4, sort_keys=True))

print_scores()
