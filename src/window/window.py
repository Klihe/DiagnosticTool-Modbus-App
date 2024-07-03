from PyQt6.QtWidgets import QMainWindow, QScrollArea, QHBoxLayout, QVBoxLayout, QGridLayout, QWidget, QPushButton

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

        self.page_layout = QHBoxLayout()
        self.comm_layout = QGridLayout()
        self.values_layout = QVBoxLayout()
        
        self.toolbar = ToolBar(self.grabber, self)
        self.menubar = MenuBar(self.grabber, self)
        self.commgroup = CommGroup(self.grabber)
        self.valuesgroup = ValuesGroup(self.grabber)
        
        self.commgroup.addGroup(self.comm_layout)
        self.valuesgroup.addGroup(self.values_layout)
        
        self.page_layout.addLayout(self.comm_layout)
        self.page_layout.addLayout(self.values_layout)
        
        self.widget = QWidget()
        self.widget.setLayout(self.page_layout)
        self.setCentralWidget(self.widget)