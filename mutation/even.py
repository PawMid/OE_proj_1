from chromosome import RealChromosome
from .mutation import MutationStrategy
import random


class EvenStrategy(MutationStrategy):

    def __init__(self):
        super().__init__(True)

    @staticmethod
    def mutate(chromosome: RealChromosome, **kwargs):
        chromosome.value = random.uniform(kwargs.get('min'), kwargs.get('max'))
