from genetic import Genetic
from functions import Ackley, Branin
from selection import get_strategy as get_selection, binary as binarySelections, SelectionStrategy
from mutation import get_strategy as get_mutation, binary as binaryMutations, MutationStrategy
from crossover import get_strategy as get_crossover, binary as binaryCrossovers, CrossoverStrategy

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

population_size: QLineEdit
chromosome_size: QLineEdit

selectionStrategy: SelectionStrategy
selectionParams: Dict = {}

crossoverStrategy: CrossoverStrategy
crossoverProbability: QLineEdit

mutationStrategy: MutationStrategy
mutationProbability: QLineEdit


def main():
    # gen = Genetic(Branin, BestStrategy, UniformCrossover, ThreePointStrategy, population_size=1000, chromosome_size=50)
    #
    # gen.algorithm(epochs=100, n=10)
    #
    # gen.plot_solution()

    global population_size
    global chromosome_size

    selectionStrategyCombo: QComboBox

    app = QApplication(sys.argv)
    mainWidget = QWidget()
    mainWidget.setWindowTitle('Genetic algorithm')
    mainLayout = QGridLayout()
    mainWidget.setLayout(mainLayout)
    mainWidget.setStyleSheet("border:1px solid rgb(0, 0, 0); ")

    w, population_size = get_input_with_label('Population size', int, width=50)
    mainLayout.addWidget(w, 0, 0)
    w, chromosome_size = get_input_with_label('Chromosome size', int, width=50)
    mainLayout.addWidget(w, 1, 0)

    mainLayout.addWidget(get_selection_strategy_widget(), 2, 0)
    mainLayout.addWidget(get_crossover_strategy_widget(), 3, 0)
    mainLayout.addWidget(get_mutation_strategy_widget(), 4, 0)

    # mainWidget.resize(width, height)
    mainWidget.show()
    sys.exit(app.exec())


def get_mutation_strategy_widget():
    global mutationStrategy
    global mutationProbability
    widget = QWidget()
    layout = QGridLayout()
    widget.setLayout(layout)
    combo = QComboBox()
    if binary:
        combo.addItems(binaryMutations)
        mutationStrategy = get_mutation(binaryMutations[0])
    else:
        raise NotImplemented

    def onchange():
        global mutationStrategy
        mutationStrategy = get_mutation(combo.currentText())
        print(mutationStrategy)

    combo.currentIndexChanged.connect(onchange)
    layout.addWidget(QLabel('Mutation strategy'), 0, 0)
    layout.addWidget(combo, 0, 1)
    w, mutationProbability = get_input_with_label(
        'Crossover probability',
        float,
        content_margins=[0, 0, 0, 0],
        width=50
    )
    layout.addWidget(w, 1, 0, 1, 2)
    return widget



def get_crossover_strategy_widget():
    global crossoverStrategy
    global crossoverProbability
    crossoverWidget = QWidget()
    crossoverLayout = QGridLayout()
    crossoverWidget.setLayout(crossoverLayout)
    combo = QComboBox()
    if binary:
        combo.addItems(binaryCrossovers)
        crossoverStrategy = get_crossover(binaryCrossovers[0])
    else:
        raise NotImplemented

    def onchange():
        global crossoverStrategy
        crossoverStrategy = get_crossover(combo.currentText())
        print(crossoverStrategy)

    combo.currentIndexChanged.connect(onchange)

    crossoverLayout.addWidget(QLabel('Crossover strategy'), 0, 0)
    crossoverLayout.addWidget(combo, 0, 1)
    w, crossoverProbability = get_input_with_label(
        'Crossover probability',
        float,
        content_margins=[0, 0, 0, 0],
        width=50
    )
    crossoverLayout.addWidget(w, 1, 0, 1, 2)

    return crossoverWidget


def get_selection_strategy_widget():
    global selectionStrategy
    global selectionParams
    selectionStrategyCombo = QComboBox()
    if binary:
        selectionStrategyCombo.addItems(binarySelections)
        selectionStrategy = get_selection(binarySelections[0])
    else:
        raise NotImplemented

    def change_selection_params():
        params = selectionStrategy.get_params_list()
        clearLayout(paramsWidget.layout())
        for key, val in params.items():
            w, hook = get_input_with_label(key, val, content_margins=[0, 0, 0, 0], width=50)
            selectionParams[key] = hook
            paramsWidget.layout().addWidget(w)

    def onchange():
        global selectionStrategy
        selectionStrategy = get_selection(selectionStrategyCombo.currentText())
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
    paramsLayout.setContentsMargins(0, 0, 0, 0)
    paramsWidget.setLayout(paramsLayout)
    selectionLayout.addWidget(paramsWidget, 2, 0, 1, 2)
    change_selection_params()
    return selectionWidget


def get_button_with_side_effect(label: str, effect):
    pass


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
    if kwargs.get('content_margins') and isinstance(kwargs.get('content_margins'), list):
        layout.setContentsMargins(*kwargs.get('content_margins'))

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
