from chromosome import RealChromosome
from .mutation import MutationStrategy
import numpy.random


class GaussianStrategy(MutationStrategy):

    def __init__(self):
        super().__init__(True)

    @staticmethod
    def mutate(chromosome: RealChromosome, **kwargs):
        chromosome.value = chromosome.value + numpy.random.normal()
