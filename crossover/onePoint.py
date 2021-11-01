from chromosome import BinCromosome
from crossover.cross import CrossoverStrategy
from random import randrange


class OnePointCrossover(CrossoverStrategy):

    def __init__(self):
        super().__init__(True)

    @staticmethod
    def cross(ch1: BinCromosome, ch2: BinCromosome):
        crossoverPoint = randrange(0, ch1.length, 1)
        for i in range(crossoverPoint, ch1.length):
            tmp = ch1.value[i]
            ch1.value[i] = ch2.value[i]
            ch2.value[i] = tmp
