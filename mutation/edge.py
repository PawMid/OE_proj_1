from chromosome import BinCromosome
from .mutation import MutationStrategy
from random import getrandbits


class EdgeStrategy(MutationStrategy):

    def __init__(self):
        super().__init__(True)

    @staticmethod
    def mutate(chromosome: BinCromosome):
        left = getrandbits(1)
        if left:
            chromosome.value[chromosome.length - 1] = not chromosome.value[chromosome.length - 1]
        else:
            chromosome.value[0] = not chromosome.value[0]
