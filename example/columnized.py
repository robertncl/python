from typing import Sequence, List, Tuple

def columnize(sequence: Sequence[str], num_columns: int = 0) -> List[Tuple[str, ...]]:
    if num_columns == 0:
        num_columns = round(len(sequence) ** .5)
    num_rows, reminder = divmod(len(sequence), num_columns)
    num_rows += bool(reminder)
    return [tuple(sequence[i::num_rows]) for i in range(num_rows)]