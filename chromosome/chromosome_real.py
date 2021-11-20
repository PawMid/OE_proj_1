from ._chromosome import Chromosome
from typing import (
    List,
)
import random

from utils import bin_to_dec


class RealChromosome(Chromosome):
    value: float
    length: int

    def __init__(self, min, max, crossover_prob: float = 0.9, mutation_prob: float = 0.1) -> None:
        super().__init__()
        self.value = random.uniform(min, max)
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob

    def get_value(self, **kwargs) -> float:
        return self.value
