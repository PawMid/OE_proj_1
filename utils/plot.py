import matplotlib.pyplot as plt
from typing import List
import numpy as np


def plot_solution_in_epochs(solutions: List, path: str = None):
    plt.plot(range(len(solutions)), solutions)
    plt.title('Solution in epochs')
    if path:
        plt.savefig(path)
    else:
        plt.show()


def plot_mean_in_epochs(solutions: List, path: str = None):
    means = []
    for i in range(len(solutions)):
        means.append(np.mean(solutions[:i]))
    plt.plot(range(len(means)), means)
    plt.title('Mean in epochs')
    if path:
        plt.savefig(path)
    else:
        plt.show()


def plot_std_in_epochs(solutions: List, path: str = None):
    deviations = []
    for i in range(len(solutions)):
        deviations.append(np.std(solutions[:i]))
    plt.plot(range(len(deviations)), deviations)
    plt.title('Standard deviation in epochs')
    if path:
        plt.savefig(path)
    else:
        plt.show()
