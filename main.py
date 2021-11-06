from genetic import Genetic
from utils.plot import *
from functions import functions, functionFactory, Function
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
    QComboBox,
    QPushButton
)
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt

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

function: Function

epochs: QLineEdit

elite_count: QLineEdit

genetic: Genetic

computation_time: QLabel
result: QLabel

solution_layout: QHBoxLayout
solution_epochs_layout: QHBoxLayout
mean_layout: QHBoxLayout
std_layout: QHBoxLayout


def main():
    global population_size
    global chromosome_size
    global epochs
    global elite_count
    global computation_time
    global result
    global solution_layout
    global solution_epochs_layout
    global mean_layout
    global std_layout

    selectionStrategyCombo: QComboBox

    app = QApplication(sys.argv)
    mainWidget = QWidget()
    mainWidget.setWindowTitle('Genetic algorithm')
    mainLayout = QGridLayout()
    mainWidget.setLayout(mainLayout)
    # mainWidget.setStyleSheet("border:1px solid rgb(0, 0, 0); ")

    col1 = []

    w, population_size = get_input_with_label('Population size', int, width=50, default='1000')
    col1.append(w)
    w, chromosome_size = get_input_with_label('Chromosome size', int, width=50, default='10')
    col1.append(w)
    w, epochs = get_input_with_label('Epochs', int, width=50, default='100')
    col1.append(w)
    w, elite_count = get_input_with_label('Elites', int, width=50, default='1')
    col1.append(w)
    col1.append(get_selection_strategy_widget())
    col1.append(get_crossover_strategy_widget())
    col1.append(get_mutation_strategy_widget())
    col1.append(get_function_widget())
    col1.append(get_button_with_side_effect('Run', run_algorithm))
    w = get_column_widget(*col1)
    w.setMaximumWidth(500)
    mainLayout.addWidget(w, 0, 0, 8, 1)

    w, computation_time = get_label_with_hook('Computation time [s]:')
    w1, solution_layout = get_plot_widget('Solution in function space')
    w2, solution_epochs_layout = get_plot_widget('Solution over epochs')
    w = get_column_widget(w, w1, w2)
    mainLayout.addWidget(w, 0, 1, 8, 1)

    w, result = get_label_with_hook('Algorithm result:')
    w1, mean_layout = get_plot_widget('Mean over epochs')
    w2, std_layout = get_plot_widget('Standard deviation over epochs')
    w = get_column_widget(w, w1, w2)
    mainLayout.addWidget(w, 0, 2, 8, 1)

    # mainWidget.resize(width, height)
    mainWidget.showMaximized()
    sys.exit(app.exec())


def get_column_widget(*args):
    columnWidget = QWidget()
    columnLayout = QVBoxLayout()
    columnWidget.setLayout(columnLayout)

    for arg in args:
        columnLayout.addWidget(arg)

    return columnWidget


def get_plot_widget(title: str):
    widget = QWidget()
    layout = QVBoxLayout()
    widget.setLayout(layout)
    layout.addWidget(QLabel(title))
    fig = plt.figure()
    fig.set_figwidth(3)
    canvas = FigureCanvasQTAgg(fig)
    plot_widget = QWidget()
    plot_layout = QHBoxLayout()
    plot_widget.setLayout(plot_layout)
    plot_layout.addWidget(canvas)
    plot_layout.setContentsMargins(0, 0, 0, 0)
    layout.addWidget(plot_widget)
    plot_widget.setMaximumHeight(400)

    return widget, plot_layout


def get_function_widget():
    global function
    widget = QWidget()
    layout = QGridLayout()
    widget.setLayout(layout)
    combo = QComboBox()
    combo.addItems(functions)
    function = functionFactory(functions[0])
    plot = function().plot(get_axis=True)
    plot.tight_layout()
    plot.set_figwidth(3)
    plot.set_dpi(100)
    canvas = FigureCanvasQTAgg(plot)
    canvas.resize(100, 100)

    canvas_w = QWidget()
    canvas_layout = QGridLayout()
    canvas_w.setLayout(canvas_layout)
    canvas_layout.addWidget(canvas)

    def onchange():
        global function
        function = functionFactory(combo.currentText())
        plot = function().plot(get_axis=True)
        plot.tight_layout()
        plot.set_figwidth(3)
        plot.set_dpi(100)
        canvas = FigureCanvasQTAgg(plot)
        clearLayout(canvas_layout)
        canvas_layout.addWidget(canvas)
        print(function)

    combo.currentIndexChanged.connect(onchange)

    layout.addWidget(QLabel('Function'))
    layout.addWidget(combo)
    layout.addWidget(canvas_w)

    return widget


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
        'Mutation probability',
        float,
        content_margins=[0, 0, 0, 0],
        width=50,
        range=[0., 1.],
        default='0,1'
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
        width=50,
        range=[0., 1.],
        default='0.9'
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
            w, hook = get_input_with_label(key, val[0], content_margins=[0, 0, 0, 0], width=50, default=val[1])
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
    btn = QPushButton(label)
    btn.clicked.connect(effect)
    return btn


def get_label_with_hook(label: str):
    layout = QHBoxLayout()
    lab = QLabel(label)
    lab.setAlignment(Qt.AlignRight)
    layout.addWidget(lab)
    hook = QLabel('-')
    hook.setAlignment(Qt.AlignLeft)
    layout.addWidget(hook)

    widget = QWidget()
    widget.setLayout(layout)

    return widget, hook


def get_input_with_label(label, input_type: type = None, **kwargs):
    layout = QHBoxLayout()
    label = QLabel(label)
    inp = QLineEdit()
    if kwargs.get('width'):
        inp.setMaximumWidth(kwargs.get('width'))
    if input_type == int:
        inp.setValidator(QIntValidator())
    if input_type == float:
        if kwargs.get('range'):
            print(kwargs.get('range'))
            inp.setValidator(QDoubleValidator(kwargs.get('range')[0], kwargs.get('range')[1], 2))
        else:
            inp.setValidator(QDoubleValidator(0., 1., 2.))
    inp.setText(kwargs.get('default'))
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


def run_algorithm():
    global population_size
    global chromosome_size
    global selectionStrategy
    global selectionParams
    global crossoverStrategy
    global crossoverProbability
    global mutationStrategy
    global mutationProbability
    global function
    global epochs
    global elite_count
    global genetic
    global computation_time
    global result
    global solution_layout

    if \
            population_size.text() \
                    and chromosome_size.text() \
                    and selectionParams \
                    and crossoverProbability.text() \
                    and mutationProbability.text() \
                    and epochs.text() \
                    and elite_count.text():
        pop = int(population_size.text())
        chr = int(chromosome_size.text())
        sp = {}
        for key, val in selectionParams.items():
            try:
                sp[key] = float(val.text().replace(',', '.'))
            except:
                continue
        cp = float(crossoverProbability.text().replace(',', '.'))
        mp = float(mutationProbability.text().replace(',', '.'))
        ep = int(epochs.text())
        ec = int(elite_count.text())
        genetic = Genetic(
            function,
            selectionStrategy,
            crossoverStrategy,
            mutationStrategy,
            chromosome_size=chr,
            crossover_prob=cp,
            mutation_prob=mp,
            population_size=pop,
            binary=binary
        )
        genetic.algorithm(ep, elites_quan=ec, **sp)

        result_list = genetic.get_solution_history()

        time = str(genetic.get_calculation_time())
        time = time.split('.')
        computation_time.setText(f'{time[0]},{time[1][:3]}')

        res = str(genetic.best_fit)
        res = res.split('.')
        result.setText(f'{res[0]},{res[1][:3]}')

        clearLayout(solution_layout)
        fig = genetic.plot_solution()
        fig.set_figwidth(3)
        solution_layout.addWidget(FigureCanvasQTAgg(fig))

        clearLayout(solution_epochs_layout)
        fig = plot_solution_in_epochs(result_list)
        solution_epochs_layout.addWidget(FigureCanvasQTAgg(fig))

        clearLayout(mean_layout)
        fig = plot_mean_in_epochs(result_list)
        mean_layout.addWidget(FigureCanvasQTAgg(fig))

        clearLayout(std_layout)
        fig = plot_std_in_epochs(result_list)
        std_layout.addWidget(FigureCanvasQTAgg(fig))


if __name__ == '__main__':
    main()
