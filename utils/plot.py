import matplotlib.pyplot as plt
from typing import List
import numpy as np


def plot_solution_in_epochs(solutions: List, path: str = None):
    fig = plt.figure()
    axis = fig.gca()
    axis.plot(range(len(solutions)), solutions)
    if path:
        plt.savefig(path)
    else:
        return fig


def plot_mean_in_epochs(solutions: List, path: str = None):
    means = []
    for i in range(len(solutions)):
        means.append(np.mean(solutions[:i]))
    fig = plt.figure()
    axis = fig.gca()
    axis.plot(range(len(means)), means)
    if path:
        plt.savefig(path)
    else:
        return fig


def plot_std_in_epochs(solutions: List, path: str = None):
    deviations = []
    for i in range(len(solutions)):
        deviations.append(np.std(solutions[:i]))
    fig = plt.figure()
    axis = fig.gca()
    axis.plot(range(len(deviations)), deviations)
    if path:
        plt.savefig(path)
    else:
        return fig
