
from abc import ABC

import numpy as np
import matplotlib.pyplot as plt


class Function(ABC):

    dims: int

    def __init__(self, dims: int) -> None:
        super().__init__()
        self.dims = dims

    def calculate(self, *args) -> float:
        pass

    def plot(self, x_min: float, x_max: float, y_min: float, y_max: float, step: float = 0.5):
        xaxis = np.arange(x_min, x_max, step)
        yaxis = np.arange(y_min, y_max, step)
        x, y = np.meshgrid(xaxis, yaxis)

        results = []
        for xv in xaxis:
            for yv in yaxis:
                results.append(self.calculate(xv, yv))

        results = np.reshape(results, x.shape)

        figure = plt.figure()
        axis = figure.gca( projection='3d')
        axis.plot_surface(y, x, results, cmap='jet', shade= "false")
        plt.show()