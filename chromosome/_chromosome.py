
from abc import ABC

from typing import (
    Any
)


class Chromosome(ABC):

    value: Any
    crossover_prob: float
    mutation_prob: float

    def get_value(self, **kwargs):
        pass
