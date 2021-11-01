from chromosome import BinCromosome
from crossover.cross import CrossoverStrategy
from random import randrange


class ThreePointCrossover(CrossoverStrategy):

    def __init__(self):
        super().__init__(True)

    @staticmethod
    def cross(ch1: BinCromosome, ch2: BinCromosome):
        crossoverPoints = []
        crossoverPoints.append(randrange(0, int(ch1.length/3), 1))
        crossoverPoints.append(randrange(crossoverPoints[0] + 1, int(2*ch1.length/3), 1))
        crossoverPoints.append(randrange(crossoverPoints[1] + 1, ch1.length, 1))
        for i in range(crossoverPoints[0], crossoverPoints[1]):
            tmp = ch1.value[i]
            ch1.value[i] = ch2.value[i]
            ch2.value[i] = tmp

        for i in range(crossoverPoints[2], ch1.length):
            tmp = ch1.value[i]
            ch1.value[i] = ch2.value[i]
            ch2.value[i] = tmp