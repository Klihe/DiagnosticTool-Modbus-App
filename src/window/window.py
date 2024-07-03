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
        self.setGeometry(100, 100, 1200, 600)
        
        # self.scroll_area = QScrollArea()
        # self.scroll_area.setWidgetResizable(True)

        self.page_layout = QHBoxLayout()
        self.comm_layout = QGridLayout()
        
        # self.values_container_widget = QWidget()
        # self.values_layout = QGridLayout(self.values_container_widget)
        self.values_layout = QVBoxLayout()
        
        self.toolbar = ToolBar(self, self.grabber)
        self.menubar = MenuBar(self, self.grabber)
        self.commgroup = CommGroup(self.grabber)
        self.valuesgroup = ValuesGroup()
        
        self.commgroup.addGroup(self.comm_layout)
        self.valuesgroup.addGroup(self.values_layout)
        
        # self.scroll_area.setWidget(self.values_container_widget)
        
        self.page_layout.addLayout(self.comm_layout)
        self.page_layout.addLayout(self.values_layout)
        # self.page_layout.addWidget(self.scroll_area)
        
        self.widget = QWidget()
        self.widget.setLayout(self.page_layout)
        self.setCentralWidget(self.widget)
        
    def onMyToolBarButtonClick(self) -> None:
        print("You clicked on your button")