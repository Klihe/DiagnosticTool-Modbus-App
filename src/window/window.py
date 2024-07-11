from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QGridLayout, QWidget

from window.toolbar.toolbar import ToolBar
from window.menubar.menubar import MenuBar
from window.commgroup.commgroup import CommGroup
from window.valuesgroup.valuesgroup import ValuesGroup

import window.constants as c

class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.grabber = {}
        
        self.setWindowTitle(c.WINDOW_TITLE)
        self.setGeometry(*c.WINDOW_GEOMETRY)

        self.__page_layout = QHBoxLayout()
        self.__comm_layout = QVBoxLayout()
        self.__values_layout = QVBoxLayout()
        
        self.toolbar = ToolBar(self.grabber, self)
        self.menubar = MenuBar(self.grabber, self)
        self.commgroup = CommGroup(self.grabber)
        self.valuesgroup = ValuesGroup(self.grabber)
        
        self.commgroup.addGroup(self.__comm_layout)
        self.valuesgroup.addGroup(self.__values_layout)
        
        self.__page_layout.addLayout(self.__comm_layout)
        self.__page_layout.addLayout(self.__values_layout)
        
        self.__widget = QWidget()
        self.__widget.setLayout(self.__page_layout)
        self.setCentralWidget(self.__widget)