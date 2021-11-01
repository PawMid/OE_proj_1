from typing import (
    List,
    Optional
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

    def init_individuals(self, binary: bool = True, crossover_prob: float = 0.9, mutation_prob: float = 0.1, **kwargs) -> None:
        '''
        @param binary - determnes if chromosomes in population should be binary (True) or real (False)
        @param crossover_prob: probability of crossover for single chromosome
        @param mutation_prob: probability of mutation for single chromosome
        @param kwargs.size - size of binary chromosome required for binary representation

        '''
        cnt = 0

        if binary:
            def factory() -> BinCromosome:
                if not kwargs.get('size'):
                    raise argparse.ArgumentError(message="No size argument passed add 'size=<int>' to call args.")
                return BinCromosome(kwargs.get('size'), crossover_prob, mutation_prob)
        else:
            raise NotImplemented

        while cnt < self.population_size:
            self.individuals.append(factory())
            cnt += 1
    
    def get_chromosome(self, index: int) -> Chromosome:
        return self.individuals[index]

    def set_chromosome(self, index: int, value: Chromosome) -> None:
        self.individuals[index] = value

    def set_probability(self, crossover_prob: Optional[float] = None, mutation_prob: Optional[float] = None):
        if crossover_prob or mutation_prob:
            for chromosome in self.individuals:
                if crossover_prob:
                    chromosome.crossover_prob = crossover_prob
                if mutation_prob:
                    chromosome.mutation_prob = mutation_prob

    def print_population(self, **kwargs) -> None:
        if isinstance(self.individuals[0], BinCromosome):
            if kwargs.get('real'):
                for chrom in self.individuals:
                    print(chrom.get_value(solution_space=self.solution_space))
            else:
                for chrom in self.individuals:
                    print(chrom.value)   
        else:
            pass
