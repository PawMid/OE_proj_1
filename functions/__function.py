
from abc import ABC

import numpy as np
import matplotlib.pyplot as plt
from typing import List


class Function(ABC):

    dims: int

    def __init__(self, dims: int) -> None:
        super().__init__()
        self.dims = dims

    def calculate(self, *args) -> float:
        pass

    def plot(self, x_space: List[float], y_space: List[float], step: float = 0.5, get_axis: bool = False):
        xaxis = np.arange(x_space[0], x_space[1], step)
        np.append(xaxis, x_space[1])
        yaxis = np.arange(y_space[0], y_space[1], step)
        np.append(yaxis, y_space[1])
        x, y = np.meshgrid(xaxis, yaxis)
        results = []
        for xv in xaxis:
            for yv in yaxis:
                results.append(self.calculate(xv, yv))

        results = np.reshape(results, x.shape)
               
        figure = plt.figure()
        axis = figure.gca( projection='3d')
        axis.plot_surface(x, y, results,alpha=0.7, cmap='jet', shade= "false")
        
        if get_axis:
            return axis

        plt.show()