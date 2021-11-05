from genetic import Genetic
from functions import Ackley, Branin
from selection import get_strategy, binary as binarySelections, BestStrategy
from mutation import OnePointStrategy, ThreePointStrategy
from crossover import UniformCrossover, TwoPointCrossover, OnePointCrossover, ThreePointCrossover

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QGridLayout,
    QHBoxLayout,
    QLineEdit,
    QComboBox
)
from PyQt5.QtGui import QIntValidator,QDoubleValidator

binary = True

width = 500
height = 400


def main():
    gen = Genetic(Branin, BestStrategy, UniformCrossover, ThreePointStrategy, population_size=1000, chromosome_size=50)

    gen.algorithm(epochs=100, n=10)

    gen.plot_solution()

    # population_size: QLineEdit
    # chromosome_size: QLineEdit
    # selectionStrategyCombo: QComboBox
    #
    # app = QApplication(sys.argv)
    # mainWidget = QWidget()
    # mainWidget.setWindowTitle('Genetic algorithm')
    # mainLayout = QGridLayout()
    # mainWidget.setLayout(mainLayout)
    #
    # w, population_size = get_input_with_label('Population size', int, width=70)
    # mainLayout.addWidget(w, 0, 0)
    # w, chromosome_size = get_input_with_label('Chromosome size', int, width=70)
    # mainLayout.addWidget(w, 1, 0)
    #
    # selectionStrategyCombo = QComboBox()
    # selectionStrategyCombo.addItems(binarySelections)
    #
    # mainLayout.addWidget(selectionStrategyCombo, 2, 0)
    #
    # mainWidget.resize(width, height)
    # mainWidget.show()
    # sys.exit(app.exec())


def get_input_with_label(label, input_type: type = None, **kwargs):
    layout = QHBoxLayout()
    label = QLabel(label)
    inp = QLineEdit()
    if kwargs.get('width'):
        inp.setMaximumWidth(kwargs.get('width'))
    if input_type == int:
        inp.setValidator(QIntValidator())
    layout.addWidget(label)
    layout.addWidget(inp)

    widg = QWidget()
    widg.setLayout(layout)

    return widg, inp


if __name__ == '__main__':
    main()
