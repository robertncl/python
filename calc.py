import operator

def calc(a: float, b: float, op: str) -> float:
    """Perform a calculation with two numbers and an operator (+, -, *, /)."""
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ValueError('Division by zero')
        return a / b
    else:
        raise ValueError(f'Unknown operator: {op}')