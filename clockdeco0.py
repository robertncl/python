import time
from typing import Callable, Any

def clock(func: Callable) -> Callable:
    """A simple decorator that prints the elapsed time and arguments of the decorated function."""
    def clocked(*args: Any) -> Any:
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
        return result
    return clocked  