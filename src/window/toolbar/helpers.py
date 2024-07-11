from PyQt6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QWidgetAction, QToolBar, QMainWindow
from PyQt6.QtGui import QAction, QActionGroup, QIcon
from PyQt6.QtCore import QTimer

class ValueButton:
    def __init__(self, grabber: dict, name: str, window: QMainWindow) -> None:
        self.__name = name
        self.__window = window
        self.__grabber = grabber
        
        self.__widget_action= QWidgetAction(window)
        self.__container = QWidget()
        self.__layout = QHBoxLayout()
        
        self.__grabber[f"{self.__name}_action"] = QAction(self.__name, self.__window)
        self.__grabber[f"{self.__name}_action"].setCheckable(True)
        self.__grabber[f"{self.__name}_edit"] = QLineEdit()
        self.__grabber[f"{self.__name}_edit"].setText("1000")
        self.__grabber[f"{self.__name}_edit"].setPlaceholderText("Enter time in ms")
        self.__grabber[f"{self.__name}_timer"] = QTimer(self.__window)
        self.__grabber[f"{self.__name}_timer"].setInterval(1000)
        
        self.__layout.addWidget(self.__grabber[f"{self.__name}_edit"])
        
        self.__container.setLayout(self.__layout)
        self.__widget_action.setDefaultWidget(self.__container)
        
    def addAction(self, toolbar: QToolBar) -> None:
        self.__toolbar = toolbar
        
        self.__toolbar.addAction(self.__grabber[f"{self.__name}_action"])
        self.__toolbar.addAction(self.__widget_action)
        