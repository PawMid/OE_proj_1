from chromosome import BinCromosome
from crossover.cross import CrossoverStrategy
from random import getrandbits


class UniformCrossover(CrossoverStrategy):

    def __init__(self):
        super().__init__(True)

    @staticmethod
    def cross(ch1: BinCromosome, ch2: BinCromosome):
        for i in range(ch1.length):
            swap = bool(getrandbits(1))
            if swap:
                tmp = ch1.value[1]
                ch1.value[i] = ch2.value[i]
                ch2.value[i] = tmp
