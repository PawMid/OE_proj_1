from abc import ABC
from chromosome import Chromosome


class MutationStrategy(ABC):

    def __init__(self, binary: bool):
        self.binary = binary

    @staticmethod
    def mutate(chromosome: Chromosome, **kwargs):
        pass
