from typing import (
    List
)
import argparse

from chromosome import Chromosome, BinCromosome

class Popultaion():

    solution_space: List[float]
    individuals: List[Chromosome]
    population_size: int

    def __init__(self, solution_space: List[float], population_size: int) -> None:
        self.solution_space = solution_space
        self.individuals = []
        self.population_size = population_size

    def init_individuals(self, binary: bool = True, **kwargs) -> None:
        '''
        @param binary - determnes if chromosomes in population should be binary (True) or real (False)
        @param kewargs.size - size of binary chromosome required for binary representation
        '''
        cnt = 0

        if binary:
            def factory() -> BinCromosome:
                if not kwargs.get('size'):
                    raise argparse.ArgumentError(message="No size argument passed add 'size=<int>' to call args.")
                return BinCromosome(kwargs.get('size'))
        else:
            raise NotImplemented

        while cnt < self.population_size:
            self.individuals.append(factory())
            cnt += 1
    
    def get_chromosome(self, index: int) -> Chromosome:
        return self.individuals[index]

    def set_chromosome(self, index: int, value: Chromosome) -> None:
        self.individuals[index] = value

    def print_population(self, **kwargs) -> None:
        if isinstance(self.individuals[0], BinCromosome):
            if kwargs.get('real'):
                for chrom in self.individuals:
                    print(chrom.get_real(self.solution_space)) 
            else:
                for chrom in self.individuals:
                    print(chrom.value)   
        else:
            pass
