from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit, QHBoxLayout, QWidgetAction
from PyQt6.QtGui import QAction, QActionGroup, QIcon

class ActionGroup:
    def __init__(self, toolbar, parent) -> None:
        self.__toolbar = toolbar
        self.__parent = parent
        self.__action_dict = {}
        
        self.__action_group = QActionGroup(parent)
        self.__action_group.setExclusive(True)
        
    def addAction(self, name: str, icon: QIcon=None) -> None:
        if icon is None:
            self.__action_dict[name] = QAction(name, self.__parent)
        else:
            self.__action_dict[name] = QAction(icon, name, self.__parent)
            
        self.__action_dict[name].setCheckable(True)
        self.__action_group.addAction(self.__action_dict[name])
        self.__toolbar.addAction(self.__action_dict[name])
        
    def triggered_connect(self, name: str, function) -> None:
        self.__action_dict[name].triggered.connect(function)
        
class ValueButton:
    def __init__(self, name: str, toolbar, parent):
        self.__widget_action= QWidgetAction(parent)
        self.__container = QWidget()
        self.__layout = QHBoxLayout()
        
        self.__action = QAction(name, parent)
        self.__edit = QLineEdit()
        
        toolbar.addAction(self.__action)
        self.__layout.addWidget(self.__edit)
        
        self.__container.setLayout(self.__layout)
        self.__widget_action.setDefaultWidget(self.__container)
        toolbar.addAction(self.__widget_action)