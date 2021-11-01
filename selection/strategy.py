from abc import ABC
from typing import List


class SelectionStrategy(ABC):

    @staticmethod
    def select(**kwargs) -> List[int]:
        pass

    def get_params_list(self):
        pass
