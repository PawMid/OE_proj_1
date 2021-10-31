
from abc import ABC

import numpy as np
import matplotlib.pyplot as plt
from typing import List


class Function(ABC):

    def __init__(self, dims: int, space: List) -> None:
        super().__init__()
        self.dims = dims
        self._space = space

    def calculate(self, *args) -> float:
        pass

    def get_space(self):
        return self._space

    def plot(self, x_min: float, x_max: float, y_min: float, y_max: float, step: float = 0.5, get_axis: bool = False):
        xaxis = np.arange(x_min, x_max, step)
        np.append(xaxis, x_max)
        yaxis = np.arange(y_min, y_max, step)
        np.append(yaxis, y_max)
        x, y = np.meshgrid(xaxis, yaxis)

        results = []
        for xv in xaxis:
            for yv in yaxis:
                results.append(self.calculate(xv, yv))

        print(results[len(results)-1])

        results = np.reshape(results, x.shape)
        
        figure = plt.figure()
        axis = figure.gca( projection='3d')
        axis.plot_surface(x, y, results,alpha=0.7, cmap='jet', shade= "false")
        
        if get_axis:
            return axis

        plt.show()