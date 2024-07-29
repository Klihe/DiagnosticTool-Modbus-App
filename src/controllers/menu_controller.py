from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QAction
class MenuController:
    def __init__(self, parent: QMainWindow) -> None:
        self.__parent = parent
        
        self.__find()
        self.__connect()
        
    def __find(self) -> None:
        self.__open_file = self.__parent.findChild(QAction, "open_file")
        self.__save = self.__parent.findChild(QAction, "save_file")
        self.__save_as = self.__parent.findChild(QAction, "save_as_file")
        self.__open_compare = self.__parent.findChild(QAction, "open_compare")
        self.__open_plot = self.__parent.findChild(QAction, "open_plot")
    
    def __connect(self) -> None:
        self.__open_file.triggered.connect(lambda: print("Open"))
        self.__save.triggered.connect(lambda: print("Save"))
        self.__save_as.triggered.connect(lambda: print("SaveAs"))
        self.__open_compare.triggered.connect(lambda: print("OpenCompare"))
        self.__open_plot.triggered.connect(lambda: print("OpenPlot"))