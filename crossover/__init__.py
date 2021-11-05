from crossover.cross import CrossoverStrategy
from crossover.onePoint import OnePointCrossover
from crossover.twoPoint import TwoPointCrossover
from crossover.threePoint import ThreePointCrossover
from crossover.uniform import UniformCrossover

__all__ = [
    'CrossoverStrategy',
    'OnePointCrossover',
    'TwoPointCrossover',
    'ThreePointCrossover',
    'UniformCrossover',
    'get_strategy',
    'binary'
]

binary = [
    'One point',
    'Two point',
    'Three point',
    'Uniform'
]

__strategies = {
    'One point': OnePointCrossover,
    'Two point': TwoPointCrossover,
    'Three point': ThreePointCrossover,
    'Uniform': UniformCrossover,
}


def get_strategy(name: str):
    return __strategies[name]
