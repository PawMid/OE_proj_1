
from population import Popultaion

binary = True

def main():

    popultaion_X: Popultaion = Popultaion([20., 41.5], 30)
    population_Y: Popultaion = Popultaion([11.3, 40.2], 30)

    population_Y.init_individuals(binary, size=10)
    popultaion_X.init_individuals(binary, size=10)
    
    popultaion_X.print_population(real=True)


if __name__ == '__main__':
    main()

