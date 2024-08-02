import matplotlib
import random
import numpy as np
import pandas as pd

matplotlib.use("QtAgg")

from PyQt6.QtWidgets import QWidget, QLayout
from PyQt6 import QtCore

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Plot(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(Plot, self).__init__(fig)


class PlotSection(QWidget):
    def __init__(self, config: dict) -> None:
        super().__init__()

        self.__config = config

        self.__create()

    def __create(self) -> None:
        self.canvas = Plot(self, width=5, height=4, dpi=100)

        self.data1 = []
        self.data2 = []

        (self.line1,) = self.canvas.axes.plot(self.data1, "r-", label="exp")
        self.canvas.axes.set_xlabel("time (s)")
        self.canvas.axes.set_ylabel("exp", color="tab:red")
        self.canvas.axes.tick_params(axis="y", labelcolor="tab:red")

        self.ax2 = self.canvas.axes.twinx()
        (self.line2,) = self.ax2.plot(self.data2, "b-", label="sin")
        self.ax2.set_ylabel("sin", color="tab:blue")
        self.ax2.tick_params(axis="y", labelcolor="tab:blue")

        self.timer = QtCore.QTimer()
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        # Generate new data
        new_data1 = random.randint(0, 10)
        new_data2 = random.randint(30, 50)

        # Update the data for data1
        if len(self.data1) >= 100:
            self.data1 = self.data1[1:] + [new_data1]
        else:
            self.data1.append(new_data1)

        # Update the data for data2
        if len(self.data2) >= 100:
            self.data2 = self.data2[1:] + [new_data2]
        else:
            self.data2.append(new_data2)

        # Update the data for the lines.
        x_data = np.arange(
            len(self.data1)
        )  # Generate x-data based on the length of data1
        self.line1.set_data(x_data, self.data1)
        self.line2.set_data(x_data, self.data2)

        # Update the x-axis limits to fit the new data.
        self.canvas.axes.set_xlim(0, len(self.data1) - 1)
        self.ax2.set_xlim(0, len(self.data2) - 1)

        # Rescale the y-axis.
        self.canvas.axes.relim()
        self.canvas.axes.autoscale_view()

        self.ax2.relim()
        self.ax2.autoscale_view()

        # Trigger the canvas to update and redraw.
        self.canvas.draw_idle()

    def addSection(self, layout: QLayout) -> None:
        layout.addWidget(self.canvas)
