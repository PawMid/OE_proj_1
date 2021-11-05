from .strategy import SelectionStrategy
from typing import List
from random import randrange


class TournamentStrategy(SelectionStrategy):

    @staticmethod
    def select(**kwargs) -> List[int]:
        if not kwargs.get('k') and not kwargs.get('population_len'):
            raise ValueError('Missing required param k or population_len')
        k = kwargs.get('k')
        population_len = kwargs.get('population_len') - 1
        n = int(population_len / k)
        selected = []
        groups = TournamentStrategy.__make_groups(n, k, population_len, kwargs.get('elite_index') )
        for group in groups:
            index = randrange(0, len(group), 1)
            selected.append(group[index])
        return selected

    @staticmethod
    def __make_groups(group_count: int, group_amount: int, population_len: int, elite_indexes: List) -> List[List]:
        groups = []
        selected = [False] * population_len
        for index in elite_indexes:
            selected[index] = True
        while len(groups) < group_amount:
            group = []
            while len(group) < group_count:
                index = randrange(0, population_len, 1)
                if selected[index]:
                    continue
                group.append(index)
                selected[index] = True
            groups.append(group)
        return groups

    @staticmethod
    def get_params_list():
        return {'k': int}
