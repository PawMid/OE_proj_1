from .strategy import SelectionStrategy
from typing import List
from math import inf


class BestStrategy(SelectionStrategy):

    @staticmethod
    def select(**kwargs) -> List[int]:
        """

        :param kwargs: Required params: percentage (0, 1), calculated_values (List)
        :return: List of indexes of chromosomes selected from population
        """
        if not kwargs.get('percentage') or not kwargs.get('calculated_values'):
            raise ValueError('Missing param, Required params: percentage, calculated_values.')

        vals = kwargs.get('calculated_values')
        percent = kwargs.get('percentage')
        elite_indexes = kwargs.get('elite_indexes')

        toSelect = int(len(vals) * percent)
        isSelected = [False] * len(vals)
        for index in elite_indexes:
            isSelected[index] = True
        selected = []
        for k in range(toSelect):
            minVal = inf
            index = 0
            for i in range(len(vals)):
                if vals[i] < minVal and not isSelected[i]:
                    index = i
                    minVal = vals[i]
            isSelected[index] = True
            selected.append(index)

        return selected

    @staticmethod
    def get_params_list():
        return {'percentage': float}
