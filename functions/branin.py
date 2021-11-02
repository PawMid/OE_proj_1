from .__function import Function
from math import pi, cos
from typing import List


class Branin(Function):
    _a: float
    _b: float
    _c: float
    _r: float
    _s: float
    _t: float

    def __init__(self, space: List = None, a: float = None, b: float = None, c: float = None,
                 r: float = None, s: float = None, t: float = None) -> None:
        if space is None:
            space = [[-5, 10], [0, 15]]
        super().__init__(2, space)
        self._a = 1. if not a else a
        self._b = (5.1 / (4 * (pi ** 2))) if not b else b
        self._c = 5/pi if not c else c
        self._r = 6. if not r else r
        self._s = 10. if not s else s
        self._t = 1/(8*pi) if not t else t

    def calculate(self, *args) -> float:
        if len(args) != self.dims:
            raise ValueError(f'Not enough function params expected {self.dims} got {len(args)}.')

        return self._a * (args[1] - self._b * args[0] ** 2 + self._c * args[0] - self._r) ** 2 + self._s * (
                    1 - self._t) * cos(args[0]) + self._s
