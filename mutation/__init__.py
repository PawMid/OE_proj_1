from .edge import EdgeStrategy
from .mutation import MutationStrategy
from .onePoint import OnePointStrategy
from .twoPoint import TwoPointStrategy
from .threePoint import ThreePointStrategy

__all__ = [
    'MutationStrategy',
    'EdgeStrategy',
    'OnePointStrategy',
    'TwoPointStrategy',
    'ThreePointStrategy',
    'get_strategy',
    'binary'
]

binary = [
    'One point',
    'Two point',
    'Three point',
    'Edge'
]

__strategies = {
    'One point': OnePointStrategy,
    'Two point': TwoPointStrategy,
    'Three point': ThreePointStrategy,
    'Edge': EdgeStrategy,
}


def get_strategy(name: str):
    return __strategies[name]
