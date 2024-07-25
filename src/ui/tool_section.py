from PyQt6.QtWidgets import QToolBar, QToolButton, QMainWindow
from PyQt6.QtGui import QAction

class ToolSection:
    def __init__(self, parent: QMainWindow) -> None:
        self.__parent = parent
        
        self.__create()
        
    def __create(self) -> None:
        self.__toolbar = QToolBar()
        self.__parent.addToolBar(self.__toolbar)
        
        self.__add_button("Connect")
        self.__add_button("Disconnect")
        self.__add_button("Write")
        self.__add_button("Read")
        # self.__add_button("ReadInInterval")
        self.__add_button("Compare")
        self.__add_button("ResetPlot")
        
    def __add_button(self, name: str) -> QToolButton:
        action = QAction(name, self.__parent)
        button = QToolButton()
        button.setObjectName(name)
        button.setDefaultAction(action)
        
        self.__toolbar.addWidget(button)
        
        return button
        