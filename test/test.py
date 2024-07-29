import sys
import matplotlib
import pandas as pd
matplotlib.use("QtAgg")

from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

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
        self.__sc = Plot(self, width=5, height=4, dpi=100)

        data = pd.DataFrame([
           [0, 10], [5, 15], [2, 20], [15, 25], [4, 10],
        ], columns=['A', 'B'])

        data.plot(ax=self.__sc.axes)

    def addSection(self, layout: QVBoxLayout) -> None:
        layout.addWidget(self.__sc)

class MainWindow(QMainWindow):
    def __init__(self, config):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Matplotlib with PyQt6")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.plot_section = PlotSection(config)
        self.plot_section.addSection(layout)

if __name__ == "__main__":
    config = {
        "example_key": "example_value"
    }

    app = QApplication(sys.argv)
    main_window = MainWindow(config)
    main_window.show()
    sys.exit(app.exec())
