import time
from clockdeco import clock


def snooze(seconds: float) -> None:
    """Sleep for the given number of seconds."""
    time.sleep(seconds)


@clock
def factorial(n: int) -> int:
    """Return the factorial of n."""
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))