from array import array
import reprlib
import math
from typing import Any


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)  

    def __iter__(self):
        return iter(self._components)  

    def __repr__(self):
        components = reprlib.repr(self._components)  
        components = components[components.find('['):-1]  
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))  

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))  

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)  

class Vector_v1:
    """A simple 2D vector class (version 1)."""
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vector_v1({self.x}, {self.y})'

    def __add__(self, other: Any) -> 'Vector_v1':
        if isinstance(other, Vector_v1):
            return Vector_v1(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __mul__(self, scalar: float) -> 'Vector_v1':
        return Vector_v1(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> 'Vector_v1':
        return self * scalar  