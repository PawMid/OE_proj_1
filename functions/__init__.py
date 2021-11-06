from .__function import Function
from .ackley import Ackley
from .branin import Branin

__all__ = [
    'Function',
    'Ackley',
    'Branin'
]

functions = [
    'Ackley',
    'Branin',
]

__functions = {
    'Ackley': Ackley,
    'Branin': Branin,
}


def functionFactory(name: str):
    return __functions[name]
