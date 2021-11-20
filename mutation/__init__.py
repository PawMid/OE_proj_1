from .edge import EdgeStrategy
from .mutation import MutationStrategy
from .onePoint import OnePointStrategy
from .twoPoint import TwoPointStrategy
from .threePoint import ThreePointStrategy
from .gaussian import GaussianStrategy
from .even import EvenStrategy

__all__ = [
    'MutationStrategy',
    'EdgeStrategy',
    'OnePointStrategy',
    'TwoPointStrategy',
    'ThreePointStrategy',
    'get_strategy',
    'binary',
    'real',
    'GaussianStrategy',
    'EvenStrategy'
]

binary = [
    'One point',
    'Two point',
    'Three point',
    'Edge'
]

real = [
    'Gaussian',
    'Even'
]

__strategies = {
    'One point': OnePointStrategy,
    'Two point': TwoPointStrategy,
    'Three point': ThreePointStrategy,
    'Edge': EdgeStrategy,
    'Gaussian': GaussianStrategy,
    'Even': EvenStrategy
}


def get_strategy(name: str):
    return __strategies[name]
