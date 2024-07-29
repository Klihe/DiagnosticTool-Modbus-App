from PyQt6.QtWidgets import QMainWindow, QMenuBar
from PyQt6.QtGui import QAction

class MenuTab:
    def __init__(self, parent: QMenuBar, name: str) -> None:
        self.__parent = parent
        self.__name = name
        
        self.__menu = self.__parent.addMenu(self.__name)
        
    def add_action(self, name: str, id: str) -> QAction:
        action = QAction(name, self.__parent)
        action.setObjectName(id)
        
        self.__menu.addAction(action)
        
        return action
    

class MenuSection:
    def __init__(self, parent: QMainWindow) -> None:
        self.__parent = parent
        
        self.__create()
        
    def __create(self) -> None:
        self.__menu = self.__parent.menuBar()
        
        file = MenuTab(self.__menu, "File")
        file.add_action("Open", "open_file")
        file.add_action("Save", "save_file")
        file.add_action("Save As", "save_as_file")
        
        compare = MenuTab(self.__menu, "Compare")
        compare.add_action("Open", "open_compare")
        
        plot = MenuTab(self.__menu, "Plot")
        plot.add_action("Open", "open_plot")
        