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
        
        self.data1 = [1,2,3,4,5,6,7,2,4,2]
        self.data2 = [2,1,2,3,1,3,2,4,2,4]
        
        self.line1, = self.canvas.axes.plot(self.data1, 'r-', label='exp')
        self.canvas.axes.set_xlabel('time (s)')
        self.canvas.axes.set_ylabel('exp', color='tab:red')
        self.canvas.axes.tick_params(axis='y', labelcolor='tab:red')

        self.ax2 = self.canvas.axes.twinx()
        self.line2, = self.ax2.plot(self.data2, 'b-', label='sin')
        self.ax2.set_ylabel('sin', color='tab:blue')
        self.ax2.tick_params(axis='y', labelcolor='tab:blue')
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()
        
    def update_plot(self):
        # Drop off the first y element, append a new one.
        self.data1 = self.data1[1:] + [random.randint(0, 10)]
        self.data2 = self.data2[1:] + [random.randint(0, 10)]

        # Update the data for the lines.
        self.line1.set_ydata(self.data1)
        self.line2.set_ydata(self.data2)

        # Rescale the y-axis.
        self.canvas.axes.relim()
        self.canvas.axes.autoscale_view()

        self.ax2.relim()
        self.ax2.autoscale_view()

        # Trigger the canvas to update and redraw.
        self.canvas.draw()

    def addSection(self, layout: QLayout) -> None:
        layout.addWidget(self.canvas)