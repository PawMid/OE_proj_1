from .strategy import SelectionStrategy
from typing import List


class RouletteStrategy(SelectionStrategy):

    @staticmethod
    def select(**kwargs) -> List[int]:
        raise NotImplemented
        selected = []

        return selected