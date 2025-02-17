def calc(to_solve):
    """
    Perform a mathematical operation on two numbers.

    This function takes a string input representing a mathematical operation
    and returns the result of that operation.

    Parameters:
    to_solve (str): A string in the format "operator num1 num2"
                    where operator is one of +, -, *, /, **, or %,
                    and num1 and num2 are integers.

    Returns:
    float: The result of the mathematical operation.

    """
    operations = {'+': operator.add,            
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,        
                  '**': operator.pow,
                  '%': operator.mod}

    op, first_s, second_s = to_solve.split()    
    first = int(first_s)
    second = int(second_s)

    return operations[op](first, second)