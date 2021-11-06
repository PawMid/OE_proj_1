from typing import List
from functions import Function
from population import Popultaion
from selection import SelectionStrategy
from crossover import CrossoverStrategy
from mutation import MutationStrategy
from random import randrange, random
from copy import deepcopy
import matplotlib.pyplot as plt
import time


class Genetic:
    _function: Function
    _populations: List[Popultaion]
    _dims: int

    def __init__(
            self,
            function: Function.__class__,
            selection_strategy: SelectionStrategy.__class__,
            crossover_strategy: CrossoverStrategy.__class__,
            mutation_strategy: MutationStrategy.__class__,
            space: List[List[float]] = None,
            chromosome_size=10,
            crossover_prob: float = 0.9,
            mutation_prob: float = 0.1,
            population_size: int = 100,
            binary=True,
            max_repetition=100
    ) -> None:
        self.function = function(space=space)
        self.space = self.function.space
        self._dims = len(self.function.space)
        self._population_size = population_size
        self.selection_strategy = selection_strategy()
        self.crossover_strategy = crossover_strategy()
        self.mutation_strategy = mutation_strategy()
        self._populations = []
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob
        cnt = 0
        while cnt < self._dims:
            pop = Popultaion(self.space[cnt], population_size)
            pop.init_individuals(
                binary=binary,
                crossover_prob=crossover_prob,
                mutation_prob=mutation_prob,
                size=chromosome_size
            )
            self._populations.append(pop)
            cnt += 1
        self.best_fit = None
        self.best_fit_index = None
        self.epoch = 0
        self.solutions_in_epochs = []
        self.max_repetition = max_repetition
        self.computation_time = None
        self.filename = 'solution_in_epochs.csv'

    def algorithm(self, epochs: int, minimum=True, elites_quan=1, **kwargs):
        self.epoch = 0
        repeated = 0
        t_begin = time.time()
        while self._evaluate(epochs, repeated):
            print('epoch', self.epoch)
            fitness = self._get_fitness()
            fitness_sorted = deepcopy(fitness)
            fitness_sorted.sort(reverse=not minimum)
            # print('fitness', fitness)
            best_fit = fitness_sorted[0]
            if best_fit == self.best_fit:
                repeated += 1
            else:
                self.best_fit = best_fit
            self.best_fit_index = fitness.index(self.best_fit)
            self.solutions_in_epochs.append(self.best_fit)
            elites = self._get_elites_indexes(fitness_sorted, fitness, elites_quan)
            selection_params = {
                'calculated_values': fitness,
                'population_len': self._population_size,
                'k': kwargs.get('k'),
                'percentage': kwargs.get('percentage'),
                'elite_indexes': elites
            }
            indexes = self.selection_strategy.select(**selection_params)
            crossover, mutation = self._calculate_probabilities(indexes)
            # print('selected indexes', indexes)
            paired = self._pair(indexes, crossover)
            # print('paired indexes', paired)
            for i in range(self._dims):
                for pair in paired[i]:
                    self.crossover_strategy.cross(
                        self._populations[i].get_chromosome(pair[0]),
                        self._populations[i].get_chromosome(pair[1])
                    )
                for j in range(len(indexes)):
                    if mutation[i][j]:
                        self.mutation_strategy.mutate(self._populations[i].get_chromosome(indexes[j]))
            self.epoch += 1
            # print('best', self.best_fit)
        self.computation_time = time.time() - t_begin
        self._write_to_file()

    def get_calculation_time(self):
        return self.computation_time

    def get_solution_history(self):
        return self.solutions_in_epochs

    def plot_solution(self, path: str = None):
        ax = self.function.plot(get_axis=True)
        x = self._populations[0].get_chromosome(self.best_fit_index).get_value(solution_space=self.space[0])
        y = self._populations[1].get_chromosome(self.best_fit_index).get_value(solution_space=self.space[1])
        axes = ax.axes
        axes[0].scatter(x, y, self.best_fit, c='r')
        if not path:
            return ax
        else:
            plt.savefig('solution_in_function.png')

    def _evaluate(self, epochs, repetition) -> bool:
        return self.epoch < epochs

    def _get_elites_indexes(self, sorted_fit: List, original_fit: List, n: int):
        cut = sorted_fit[:n]
        indexes = []
        for result in cut:
            indexes.append(original_fit.index(result))
        return indexes

    def _get_fitness(self):
        fit = []

        for i in range(self._population_size):
            args = []
            for k in range(self._dims):
                args.append(self._populations[k].get_chromosome(i).get_value(solution_space=self.function.space[k]))
            fit.append(self.function.calculate(*args))

        return fit

    def _calculate_probabilities(self, indexes):
        crossover = []
        mutation = []

        for i in range(self._dims):
            crossover_dim = []
            mutation_dim = []
            for index in indexes:
                if random() < self.crossover_prob:
                    crossover_dim.append(True)
                else:
                    crossover_dim.append(False)
                if random() < self.mutation_prob:
                    mutation_dim.append(True)
                else:
                    mutation_dim.append(False)
            crossover.append(crossover_dim)
            mutation.append(mutation_dim)
        return crossover, mutation

    def _write_to_file(self):
        with open(self.filename, 'w+') as file:
            lines = ['epoch, fitness\n']
            for i in range(len(self.solutions_in_epochs)):
                lines.append(f'{i+1}, {self.solutions_in_epochs[i]}\n')
            file.writelines(lines)

    def _pair(self, indexes, crossover):
        paired = []
        pairs = []

        for dim in crossover:
            indexes_copy = deepcopy(indexes)
            dim_copy = deepcopy(dim)
            pairs_in_dim = []
            cnt = 0
            for is_crossing in dim:
                if is_crossing:
                    cnt += 1
            number_of_pairs = int(cnt / 2)
            nop = list(range(number_of_pairs))
            for i in nop:
                pair = []
                index_1 = randrange(0, len(indexes_copy), 1)
                pairing = dim_copy[index_1]
                while not pairing:
                    index_1 = randrange(0, len(indexes_copy), 1)
                    pairing = dim_copy[index_1]
                pair.append(indexes_copy[index_1])
                indexes_copy.pop(index_1)
                dim_copy.pop(index_1)

                index_2 = randrange(0, len(indexes_copy), 1)
                pairing = dim[index_2]
                while not pairing:
                    index_2 = randrange(0, len(indexes_copy), 1)
                    pairing = dim[index_2]
                pair.append(indexes_copy[index_2])
                indexes_copy.pop(index_2)
                dim_copy.pop(index_2)

                pairs_in_dim.append(pair)
            pairs.append(pairs_in_dim)
        return pairs
