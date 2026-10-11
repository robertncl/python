import operator

OPERATIONS = {'+': operator.add,
              '-': operator.sub,
              '*': operator.mul,
              '/': operator.truediv,
              '**': operator.pow,
              '%': operator.mod}


def calc(to_solve: str) -> float:
    """
    Perform a mathematical operation on two numbers.

    Parameters:
    to_solve (str): A string in the format "operator num1 num2"
                    where operator is one of +, -, *, /, **, or %,
                    and num1 and num2 are integers.

    Returns:
    float: The result of the mathematical operation.
    """
    op, first_s, second_s = to_solve.split()
    return OPERATIONS[op](int(first_s), int(second_s))
