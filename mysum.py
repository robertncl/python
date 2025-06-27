def mysum(numbers: list[int]) -> int:
    """Return the sum of a list of integers."""
    total = 0
    for number in numbers:
        total += number
    return total

print(mysum())
print(mysum(10, 20, 30, 40))
print(mysum('a', 'b', 'c', 'd'))
print(mysum([10, 20, 30], [40, 50, 60], [70, 80]))