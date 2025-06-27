import time
from typing import Callable, Any

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt: str = DEFAULT_FMT) -> Callable:
    """A decorator factory that prints the elapsed time and arguments of the decorated function."""
    def decorate(func: Callable) -> Callable:
        def clocked(*_args: Any) -> Any:
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate

if __name__ == '__main__':
    @clock()
    def snooze(seconds: float) -> None:
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)