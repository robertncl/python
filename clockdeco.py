import time
import functools
from typing import Callable, Any


def clock(func: Callable) -> Callable:
    """A decorator that prints the elapsed time and arguments of the decorated function."""
    @functools.wraps(func)
    def clocked(*args: Any, **kwargs: Any) -> Any:
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = [f'{k}={v!r}' for k, v in kwargs.items()]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
        return result
    return clocked