from chromosome import RealChromosome
from crossover.cross import CrossoverStrategy
import random


class HeuristicCrossover(CrossoverStrategy):

    def __init__(self):
        super().__init__(False)

    @staticmethod
    def cross(ch1: RealChromosome, ch2: RealChromosome):
        k = random.uniform(0, 1)
        if ch2.value > ch1.value:
            ch1 = k * (ch2.value - ch1.value) * ch1.value
        else:
            ch2 = k * (ch1.value - ch2.value) * ch2.value
