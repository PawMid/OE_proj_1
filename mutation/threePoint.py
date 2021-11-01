from chromosome import BinCromosome
from .mutation import MutationStrategy
from random import randrange


class ThreePointStrategy(MutationStrategy):

    def __init__(self):
        super().__init__(True)

    @staticmethod
    def mutate(chromosome: BinCromosome):
        points = []
        for i in range(3):
            mutation_point = randrange(0, chromosome.length, 1)
            while mutation_point in points:
                mutation_point = randrange(0, chromosome.length, 1)
            points.append(mutation_point)
            chromosome.value[mutation_point] = not chromosome.value[mutation_point]
