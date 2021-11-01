from abc import ABC
from chromosome import Chromosome


class CrossoverStrategy(ABC):

    def __init__(self, binary: bool):
        self.binary = binary

    @staticmethod
    def cross(ch1: Chromosome, ch2: Chromosome):
        pass
