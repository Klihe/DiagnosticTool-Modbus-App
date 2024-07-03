from PyQt6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QWidgetAction, QToolBar, QMainWindow
from PyQt6.QtGui import QAction, QActionGroup, QIcon

class ActionGroup:
    def __init__(self, grabber: dict, toolbar: QToolBar, window: QMainWindow) -> None:
        self.__toolbar = toolbar
        self.__window = window
        self.__grabber = grabber
        
        self.__action_group = QActionGroup(window)
        self.__action_group.setExclusive(True)
        
    def addAction(self, name: str, icon: QIcon=None) -> None:
        if icon is None:
            self.__grabber[name] = QAction(name, self.__window)
        else:
            self.__grabber[name] = QAction(icon, name, self.__window)
            
        self.__grabber[name].setCheckable(True)
        self.__action_group.addAction(self.__grabber[name])
        self.__toolbar.addAction(self.__grabber[name])
        
    def triggered_connect(self, name: str, function) -> None:
        self.__grabber[name].triggered.connect(function)
        
class ValueButton:
    def __init__(self, grabber: dict, name: str, window: QMainWindow) -> None:
        self.__name = name
        self.__window = window
        self.__grabber = grabber
        
        self.__widget_action= QWidgetAction(window)
        self.__container = QWidget()
        self.__layout = QHBoxLayout()
        
        self.__grabber[f"{self.__name}_action"] = QAction(self.__name, self.__window)
        self.__grabber[f"{self.__name}_edit"] = QLineEdit()
        
        self.__layout.addWidget(self.__grabber[f"{self.__name}_edit"])
        
        self.__container.setLayout(self.__layout)
        self.__widget_action.setDefaultWidget(self.__container)
        
    def addAction(self, toolbar: QToolBar) -> None:
        self.__toolbar = toolbar
        
        self.__toolbar.addAction(self.__grabber[f"{self.__name}_action"])
        self.__toolbar.addAction(self.__widget_action)
        
class StateButton:
    def __init__(self, grabber: dict, name1: str, name2: str, window: QMainWindow) -> None:
        self.__grabber = grabber
        self.__name1 = name1
        self.__name2 = name2
        self.__window = window
        
        self.__grabber[f"{self.__name1}_{self.__name2}"] = QAction(self.__name1, self.__window)
        self.__grabber[f"{self.__name1}_{self.__name2}"].setCheckable(True)
        self.__grabber[f"{self.__name1}_{self.__name2}"].toggled.connect(self.__toggle)
        
    def addAction(self, toolbar) -> None:
        self.__toolbar = toolbar
        
        self.__toolbar.addAction(self.__grabber[f"{self.__name1}_{self.__name2}"])
        
    def __toggle(self, checked) -> None:
        if checked:
            self.__grabber[f"{self.__name1}_{self.__name2}"].setText(self.__name2)
        else:
            self.__grabber[f"{self.__name1}_{self.__name2}"].setText(self.__name1)
        