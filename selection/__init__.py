from .bestStrategy import BestStrategy
from .rouletteStrategy import RouletteStrategy
from .turnamentStrategy import TournamentStrategy
from .strategy import SelectionStrategy

__all__ = [
    'BestStrategy',
    'RouletteStrategy',
    'TournamentStrategy',
    'SelectionStrategy',
    'get_strategy',
    'binary'
]

binary = [
    'Best',
    'Tournament'
]

__strategies = {
    'Best': BestStrategy,
    'Tournament': TournamentStrategy
}


def get_strategy(name: str):
    return __strategies[name]
