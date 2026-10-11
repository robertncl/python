import time
from collections.abc import Callable
from typing import Any

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

class clock:
    """Class-based decorator that prints elapsed time and arguments of each call."""
    def __init__(self, fmt: str = DEFAULT_FMT) -> None:
        self.fmt = fmt

    def __call__(self, func: Callable) -> Callable:
        def clocked(*_args: Any) -> Any:
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(self.fmt.format(**locals()))
            return _result
        return clocked
