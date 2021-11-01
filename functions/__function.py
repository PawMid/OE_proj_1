
from abc import ABC

import numpy as np
import matplotlib.pyplot as plt
from typing import List


class Function(ABC):

    def __init__(self, dims: int, space: List) -> None:
        super().__init__()
        self.dims = dims
        self.space = space

    def calculate(self, *args) -> float:
        pass

    def plot(self, x_space: List[float]=None, y_space: List[float]=None, step: float = 0.5, get_axis: bool = False):
        if x_space:
            xaxis = np.arange(x_space[0], x_space[1], step)
            np.append(xaxis, x_space[1])
        else:
            xaxis = np.arange(self.space[0][0], self.space[0][1], step)
            np.append(xaxis, self.space[0][1])

        if y_space:
            yaxis = np.arange(y_space[0], y_space[1], step)
            np.append(xaxis, y_space[1])
        else:
            yaxis = np.arange(self.space[1][0], self.space[1][1], step)
            np.append(xaxis, self.space[1][1])
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