from .strategy import SelectionStrategy
from typing import List
from random import randrange


class TournamentStrategy(SelectionStrategy):

    @staticmethod
    def select(**kwargs) -> List[int]:
        if not kwargs.get('k') and not kwargs.get('population_len'):
            raise ValueError('Missing required param k or population_len')
        k = kwargs.get('k')
        population_len = kwargs.get('population_len')
        elites = kwargs.get('elite_indexes')
        n = int((population_len- len(elites)) / k)
        selected = []
        groups = TournamentStrategy.__make_groups(n, k, population_len, elites)
        for group in groups:
            index = randrange(0, len(group), 1)
            selected.append(group[index])
        return selected

    @staticmethod
    def __make_groups(group_count: int, group_amount: int, population_len: int, elite_indexes: List) -> List[List]:
        groups = []
        indexes = list(range(population_len))
        selected = [False] * (population_len)
        for index in elite_indexes:
            selected[index] = True
            indexes.pop(index)
        while len(groups) < group_amount:
            group = []
            while len(group) < group_count:
                index = randrange(0, len(indexes), 1)
                group.append(indexes[index])
                indexes.pop(index)
            groups.append(group)
        return groups

    @staticmethod
    def get_params_list():
        return {'k': [int, '4']}
