import time
from collections.abc import Callable
from typing import Any


def clock(func: Callable) -> Callable:
    """Simple decorator that prints the elapsed time and arguments of each call."""
    def clocked(*args: Any) -> Any:
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
        return result
    return clocked
