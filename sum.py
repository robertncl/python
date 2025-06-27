def mysum(*numbers: int) -> int:
    """Return the sum of all arguments."""
    output = 0
    for number in numbers:
        output += number
    return output

print(mysum(10, 20, 30, 40))