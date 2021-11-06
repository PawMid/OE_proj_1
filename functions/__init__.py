from .__function import Function
from .ackley import Ackley
from .branin import Branin
from .dropwave import DropWave

__all__ = [
    'Function',
    'Ackley',
    'Branin',
    'DropWave',
]

functions = [
    'Ackley',
    'Branin',
    'DropWave',
]

__functions = {
    'Ackley': Ackley,
    'Branin': Branin,
    'DropWave': DropWave,
}


def functionFactory(name: str):
    return __functions[name]
