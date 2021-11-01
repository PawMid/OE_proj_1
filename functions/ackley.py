from .__function import Function
from math import pi, exp, sqrt, cos
from typing import List


class Ackley(Function):
    _a: int
    _b: float
    _c: float

    def __init__(self, dims: int = 2, space=None, a: int = 20, b: float = 0.2, c: float = 2 * pi) -> None:
        if space is None:
            space = [[-32.768, 32.768], [-32.768, 32.768]]
        super().__init__(dims, space)
        self._a = a
        self._b = b
        self._c = c

    def calculate(self, *args) -> float:
        if len(args) != self.dims:
            raise ValueError(f'Not enough function params expected {self.dims} got {len(args)}.')

        return - self._a * exp(- self._b * sqrt(1 / self.dims * sum([arg ** 2 for arg in args]))) - exp(
            1 / self.dims * sum([cos(arg * self._c) for arg in args])) + self._a + exp(1)
