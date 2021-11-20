from chromosome import RealChromosome
from crossover.cross import CrossoverStrategy


class ArithmeticCrossover(CrossoverStrategy):

    def __init__(self):
        super().__init__(False)

    @staticmethod
    def cross(ch1: RealChromosome, ch2: RealChromosome):
        k = 0.3
        ch1.value = k * ch1.value + (1 - k) * ch2.value
        ch2.value = k * ch2.value + (1 - k) * ch1.value
