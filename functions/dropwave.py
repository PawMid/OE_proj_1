from .__function import Function
from math import cos, sqrt
from typing import List


class DropWave(Function):

    def __init__(self, space: List = None) -> None:
        if space is None:
            space = [[-5.12, 5.12], [-5.12, 5.12]]
        super().__init__(2, space)

    def calculate(self, *args) -> float:
        if len(args) != self.dims:
            raise ValueError(f'Not enough function params expected {self.dims} got {len(args)}.')

        return -(1 + cos(12 * sqrt(args[0] ** 2 + args[1] ** 2))) / (0.5 * (args[0] ** 2 + args[1] ** 2) + 2)
