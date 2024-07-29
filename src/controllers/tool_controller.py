from PyQt6.QtWidgets import QMainWindow, QToolButton

class ToolController:
    def __init__(self, parent: QMainWindow) -> None:
        self.__parent = parent

        self.__find()
        self.__connect()
        
    def __find(self) -> None:
        self.__connect_ = self.__parent.findChild(QToolButton, "Connect")
        self.__disconnect = self.__parent.findChild(QToolButton, "Disconnect")
        self.__write = self.__parent.findChild(QToolButton, "Write")
        self.__read = self.__parent.findChild(QToolButton, "Read")
        self.__read_in_interval = self.__parent.findChild(QToolButton, "ReadInInterval_button")
        self.__compare = self.__parent.findChild(QToolButton, "Compare")
        self.__reset_plot = self.__parent.findChild(QToolButton, "ResetPlot")
        
    def __connect(self) -> None:
        self.__connect_.clicked.connect(lambda: print("Connect"))
        self.__disconnect.clicked.connect(lambda: print("Disconnect"))
        self.__write.clicked.connect(lambda: print("Write"))
        self.__read.clicked.connect(lambda: print("Read"))
        self.__read_in_interval.clicked.connect(lambda: print("ReadInInterval"))
        self.__compare.clicked.connect(lambda: print("Compare"))
        self.__reset_plot.clicked.connect(lambda: print("ResetPlot"))