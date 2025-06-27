from array import array
import math
from typing import Any


class Vector2d:
    """A simple 2D vector class."""
    typecode = 'd'  

    def __init__(self, x: float, y: float) -> None:
        self.x = float(x)    
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))  

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)  

    def __str__(self):
        return str(tuple(self))  

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +  
                bytes(array(self.typecode, self)))  

    def __eq__(self, other):
        return tuple(self) == tuple(other)  

    def __abs__(self):
        return math.hypot(self.x, self.y)  

    def __bool__(self):
        return bool(abs(self))  

    def __add__(self, other: Any) -> 'Vector2d':
        if isinstance(other, Vector2d):
            return Vector2d(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __mul__(self, scalar: float) -> 'Vector2d':
        return Vector2d(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> 'Vector2d':
        return self * scalar  