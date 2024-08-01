from PyQt6.QtWidgets import QToolBar, QToolButton, QMainWindow, QLineEdit, QWidgetAction, QWidget, QHBoxLayout
from PyQt6.QtGui import QAction

class MyToolButton:
    def __init__(self, name: str, parent: QToolBar) -> None:
        self.__name = name
        self.__parent = parent
        
        self.__create()
        
    def __create(self) -> None:
        self.__action = QAction(self.__name, self.__parent)
        self.__button = QToolButton()
        self.__button.setObjectName(self.__name)
        self.__button.setDefaultAction(self.__action)
        
        self.__parent.addWidget(self.__button)
        
class MyToolValueButton:
    def __init__(self, name: str, window: QMainWindow, parent: QToolBar) -> None:
        self.__name = name
        self.__window = window
        self.__parent = parent
        
        self.__create()
    
    def __create(self) -> None:
        self.__widget_action = QWidgetAction(self.__window)
        self.__container = QWidget()
        self.__layout = QHBoxLayout()
        
        self.__action = QAction(self.__name, self.__window)
        self.__action.setCheckable(True)
        self.__button = QToolButton()
        self.__button.setDefaultAction(self.__action)
        self.__button.setObjectName(self.__name + "_button")
        self.__edit = QLineEdit()
        self.__edit.setText("1000")
        self.__edit.setPlaceholderText("Enter time in ms")
        self.__edit.setObjectName(self.__name + "_edit")
        
        self.__layout.addWidget(self.__button)
        self.__layout.addWidget(self.__edit)
        
        self.__container.setLayout(self.__layout)
        self.__widget_action.setDefaultWidget(self.__container)
        self.__parent.addAction(self.__widget_action)

class ToolSection:
    def __init__(self, window: QMainWindow) -> None:
        self.__window = window
        
        self.__create()
        
    def __create(self) -> None:
        self.__toolbar = QToolBar()
        self.__window.addToolBar(self.__toolbar)
        
        MyToolButton("Connect", self.__toolbar)
        MyToolButton("Disconnect", self.__toolbar)
        MyToolButton("Write", self.__toolbar)
        MyToolButton("Read", self.__toolbar)
        MyToolValueButton("ReadInInterval", self.__window, self.__toolbar)
        MyToolValueButton("NumberOfDataPoints", self.__window, self.__toolbar)
        MyToolButton("Compare", self.__toolbar)
        MyToolButton("ResetPlot", self.__toolbar)
        