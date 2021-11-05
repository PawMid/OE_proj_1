from genetic import Genetic
from functions import Ackley, Branin
from selection import get_strategy, binary as binarySelections, SelectionStrategy
from mutation import OnePointStrategy, ThreePointStrategy
from crossover import UniformCrossover, TwoPointCrossover, OnePointCrossover, ThreePointCrossover

import sys
from typing import Dict
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,
    QLineEdit,
    QComboBox
)
from PyQt5.QtGui import QIntValidator, QDoubleValidator

binary = True

width = 500
height = 400

selectionStrategy: SelectionStrategy
selectionParams: Dict = {}


def main():
    # gen = Genetic(Branin, BestStrategy, UniformCrossover, ThreePointStrategy, population_size=1000, chromosome_size=50)
    #
    # gen.algorithm(epochs=100, n=10)
    #
    # gen.plot_solution()

    population_size: QLineEdit
    chromosome_size: QLineEdit
    selectionStrategyCombo: QComboBox

    app = QApplication(sys.argv)
    mainWidget = QWidget()
    mainWidget.setWindowTitle('Genetic algorithm')
    mainLayout = QGridLayout()
    mainWidget.setLayout(mainLayout)

    w, population_size = get_input_with_label('Population size', int, width=70)
    mainLayout.addWidget(w, 0, 0)
    w, chromosome_size = get_input_with_label('Chromosome size', int, width=70)
    mainLayout.addWidget(w, 1, 0)

    selectionWidget = get_selection_strategy_widget()

    mainLayout.addWidget(selectionWidget, 2, 0)

    mainWidget.resize(width, height)
    mainWidget.show()
    sys.exit(app.exec())


def get_selection_strategy_widget():
    global selectionStrategy
    global selectionParams
    selectionStrategyCombo = QComboBox()
    selectionStrategyCombo.addItems(binarySelections)
    selectionStrategy = get_strategy(binarySelections[0])

    def change_selection_params():
        params = selectionStrategy.get_params_list()
        clearLayout(paramsWidget.layout())
        for key, val in params.items():
            w, hook = get_input_with_label(key, val)
            selectionParams[key] = hook
            paramsWidget.layout().addWidget(w)

    def onchange():
        global selectionStrategy
        selectionStrategy = get_strategy(selectionStrategyCombo.currentText())
        change_selection_params()
        print(selectionStrategy, selectionParams)

    selectionStrategyCombo.currentIndexChanged.connect(onchange)
    selectionWidget = QWidget()
    selectionLayout = QGridLayout()
    selectionWidget.setLayout(selectionLayout)
    selectionLayout.addWidget(QLabel('Selection strategy'), 0, 0)
    selectionLayout.addWidget(selectionStrategyCombo, 0, 1)
    selectionLayout.addWidget(QLabel('Selection params'), 1, 0)
    paramsWidget = QWidget()
    paramsLayout = QVBoxLayout()
    paramsWidget.setLayout(paramsLayout)
    selectionLayout.addWidget(paramsWidget, 2, 0)
    change_selection_params()
    return selectionWidget


def get_input_with_label(label, input_type: type = None, **kwargs):
    layout = QHBoxLayout()
    label = QLabel(label)
    inp = QLineEdit()
    if kwargs.get('width'):
        inp.setMaximumWidth(kwargs.get('width'))
    if input_type == int:
        inp.setValidator(QIntValidator())
    if input_type == float:
        inp.setValidator(QDoubleValidator())
    layout.addWidget(label)
    layout.addWidget(inp)

    widg = QWidget()
    widg.setLayout(layout)

    return widg, inp


def clearLayout(layout):
    if layout is not None:
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clearLayout(child.layout())


if __name__ == '__main__':
    main()
