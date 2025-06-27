def sum_numbers(numbers: str) -> int:
    """Return the sum of all digit substrings in the input string."""
    return sum(int(number)
               for number in numbers.split()
               if number.isdigit())

def sum_number(numbers: list[int]) -> int:
    """Return the sum of a list of integers."""
    return sum(numbers)

print(sum_numbers('1 2 3 a b c 4'))