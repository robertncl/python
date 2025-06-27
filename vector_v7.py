from array import array
from typing import Iterable, Any

class Vector:
    """A simple 2D vector class."""
    typecode = 'd'

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other: Any) -> 'Vector':
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __mul__(self, scalar: float) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> 'Vector':
        return self * scalar

    # many methods omitted in book listing, see vector_v7.py
    # in https://github.com/fluentpython/example-code-2e ...

    def __mul__(self, scalar: float) -> 'Vector':
        """Multiply the vector by a scalar."""
        try:
            factor = float(scalar)
        except TypeError:
            return NotImplemented
        return Vector(n * factor for n in self._components)

    def __rmul__(self, scalar: float) -> 'Vector':
        """Right-multiply the vector by a scalar."""
        return self * scalar  