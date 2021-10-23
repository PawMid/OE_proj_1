from .__function import Function
from math import pi, cos 

class Branin(Function):

    _a: float
    _b: float
    _c: float
    _r: float
    _s: float
    _t: float

    def __init__(self, a: float = 1., b: float = (5.1/(4*pi**2)), c: float = 5 / pi, r: float = 6., s: float = 10., t: float = 1/(8*pi)) -> None:
        super().__init__(2)
        self._a = a
        self._b = b
        self._c = c
        self._r = r
        self._s = s
        self._t = t

    def calculate(self, *args) -> float:
        if len(args) != self.dims:
            raise ValueError(f'Not enough function params expected {self.dims} got {len(args)}.')
        
        return self._a * (args[1] - self._b * args[0] ** 2 + self._c * args[0] - self._r) ** 2 + self._s * (1 - self._t) * cos(args[0]) + self._s