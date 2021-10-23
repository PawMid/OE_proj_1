from ._chromosome import Chromosome
from typing import (
    List,
)
import random

from utils import bin_to_dec

class BinCromosome(Chromosome):

    value: List[bool]
    length: int

    def __init__(self, length: int) -> None:
        super().__init__()
        self.length = length
        self.value = []
        self.__randomize_value(length)

    def __randomize_value(self, length: int) -> None:
        cnt = 0
        while cnt < length:
            self.value.append(random.randint(0, 1))
            cnt += 1
    
    def get_real(self, solution_space: List[float]) -> float:
        return solution_space[0] + bin_to_dec(self.value) * (solution_space[1] - solution_space[0]) / (2**self.length - 1)