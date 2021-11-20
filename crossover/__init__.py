from crossover.cross import CrossoverStrategy
from crossover.onePoint import OnePointCrossover
from crossover.twoPoint import TwoPointCrossover
from crossover.threePoint import ThreePointCrossover
from crossover.uniform import UniformCrossover
from crossover.Arthmetic import ArithmeticCrossover
from crossover.heuristic import HeuristicCrossover

__all__ = [
    'CrossoverStrategy',
    'OnePointCrossover',
    'TwoPointCrossover',
    'ThreePointCrossover',
    'UniformCrossover',
    'get_strategy',
    'binary',
    'real',
    'ArithmeticCrossover',
    'HeuristicCrossover'
]

binary = [
    'One point',
    'Two point',
    'Three point',
    'Uniform'
]

real = [
    'Arithmetic',
    'Heuristic'
]

__strategies = {
    'One point': OnePointCrossover,
    'Two point': TwoPointCrossover,
    'Three point': ThreePointCrossover,
    'Uniform': UniformCrossover,
    'Arithmetic': ArithmeticCrossover,
    'Heuristic': HeuristicCrossover
}


def get_strategy(name: str):
    return __strategies[name]
