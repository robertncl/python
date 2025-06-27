def mysum(*items: int) -> int:
    """Return the sum of all arguments."""
    if not items:
        return 0
    output = items[0]
    for item in items[1:]:
        output += item
    return output

print(mysum())
print(mysum(10, 20, 30, 40))
print(mysum('a', 'b', 'c', 'd'))
print(mysum([10, 20, 30], [40, 50, 60], [70, 80]))