from chromosome import BinCromosome
from .mutation import MutationStrategy
from random import randrange


class OnePointStrategy(MutationStrategy):

    def __init__(self):
        super().__init__(True)

    @staticmethod
    def mutate(chromosome: BinCromosome):
        mutation_point = randrange(0, chromosome.length, 1)

        chromosome.value[mutation_point] = not chromosome.value[mutation_point]
