from typing import List
from functions import Function
from population import Popultaion

class Genetic():

    _function: Function
    _populations: List[Popultaion]
    _dims: int

    def __init__(self, function: Function, space: List[List[float]], chromosome_size = 10,  population_size: int = 10, binary=True) -> None:
        self._function = function
        self._dims = len(space)
        cnt = 0
        while cnt < self._dims:
            pop = Popultaion(space[cnt], population_size)
            pop.init_individuals(binary=binary, size=chromosome_size)
            self._populations.append(pop)
            cnt += 1

    def algorithm():
        pass