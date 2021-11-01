from chromosome import BinCromosome
from crossover.cross import CrossoverStrategy
from random import randrange


class TwoPointCrossover(CrossoverStrategy):

    def __init__(self):
        super().__init__(True)

    @staticmethod
    def cross(ch1: BinCromosome, ch2: BinCromosome):
        crossoverPoints = []
        crossoverPoints.append(randrange(0, ch1.length/2, 1))
        crossoverPoints.append(randrange(crossoverPoints[0] + 1, ch1.length, 1))
        for i in range(crossoverPoints[0], crossoverPoints[1]):
            tmp = ch1.value[i]
            tmp2 = ch2.value[i]
            ch1.value[i] = tmp2
            ch2.value[i] = tmp