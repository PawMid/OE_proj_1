from genetic import Genetic
from functions import Ackley, Branin
from selection import BestStrategy, TournamentStrategy
from mutation import OnePointStrategy, ThreePointStrategy
from crossover import UniformCrossover, TwoPointCrossover, OnePointCrossover, ThreePointCrossover

binary = True


def main():
    gen = Genetic(Branin, TournamentStrategy, UniformCrossover, ThreePointStrategy, population_size=1000, chromosome_size=50)
    gen.algorithm(1000, percentage=0.5, k=100)

    gen.plot_solution()


if __name__ == '__main__':
    main()
