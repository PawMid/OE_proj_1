
from abc import ABC

import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import sort


class Function(ABC):

    dims: int

    def __init__(self, dims: int) -> None:
        super().__init__()
        self.dims = dims

    def calculate(self, *args) -> float:
        pass

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

        results = np.reshape(results, x.shape)
               
        figure = plt.figure()
        axis = figure.gca( projection='3d')
        axis.plot_surface(x, y, results,alpha=0.7, cmap='jet', shade= "false")
        
        if get_axis:
            return axis

        plt.show()