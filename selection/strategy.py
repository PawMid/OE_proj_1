from abc import ABC
from typing import List


class SelectionStrategy(ABC):

    @staticmethod
    def select(**kwargs) -> List[int]:
        pass

    @staticmethod
    def get_params_list():
        pass
