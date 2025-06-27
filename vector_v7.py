from array import array
from typing import Iterable

class Vector:
    """A simple vector class supporting scalar multiplication."""
    typecode = 'd'

    def __init__(self, components: Iterable[float]):
        """Initialize the vector with an iterable of floats."""
        self._components = array(self.typecode, components)

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