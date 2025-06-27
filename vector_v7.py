from array import array

class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    # many methods omitted in book listing, see vector_v7.py
    # in https://github.com/fluentpython/example-code-2e ...

    def __mul__(self, scalar):
        try:
            factor = float(scalar)
        except TypeError:  
            return NotImplemented  
        return Vector(n * factor for n in self)

    def __rmul__(self, scalar):
        return self * scalar  