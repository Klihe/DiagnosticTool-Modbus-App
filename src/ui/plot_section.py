import matplotlib
import pandas as pd
matplotlib.use("QtAgg")

from PyQt6.QtWidgets import QWidget, QLayout

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
        self.sc = Plot(self, width=5, height=4, dpi=100)

        data = pd.DataFrame([
           [0, 10], [5, 15], [2, 20], [15, 25], [4, 10],
        ], columns=['A', 'B'])

        data.plot(ax=self.sc.axes)

    def addSection(self, layout: QLayout) -> None:
        layout.addWidget(self.sc)