from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QMessageBox
from PyQt6.QtGui import QIcon

from window.toolbar.toolbar import ToolBar
from window.menubar.menubar import MenuBar
from window.commgroup.commgroup import CommGroup
from window.valuesgroup.valuesgroup import ValuesGroup

import window.constants as c

# Window class - handle the GUI
class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.grabber = {}
        
        # Set the window properties
        self.setWindowTitle(c.WINDOW_TITLE)
        self.setGeometry(*c.WINDOW_GEOMETRY)
        self.setWindowIcon(QIcon("image/peg.png"))
        
        # Create the layout
        self.__page_layout = QHBoxLayout()
        self.__comm_layout = QVBoxLayout()
        self.__values_layout = QVBoxLayout()
        
        # Create the toolbar, menubar, commgroup and valuesgroup
        self.toolbar = ToolBar(self.grabber, self)
        self.menubar = MenuBar(self.grabber, self)
        self.commgroup = CommGroup(self.grabber)
        self.valuesgroup = ValuesGroup(self.grabber)
        
        # Add the groups to the layout
        self.commgroup.addGroup(self.__comm_layout)
        self.valuesgroup.addGroup(self.__values_layout)
        
        # Add the layouts to the page layout
        self.__page_layout.addLayout(self.__comm_layout)
        self.__page_layout.addLayout(self.__values_layout)

        # Set the central widget
        self.__widget = QWidget()
        self.__widget.setLayout(self.__page_layout)
        self.setCentralWidget(self.__widget)
        
    def closeEvent(self, event):
        # Show a message box to confirm exit
        reply = QMessageBox.question(self, 'Quit Confirmation',
                                     "Are you sure you want to quit?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.Yes)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()  # Close the window
        else:
            event.ignore()  # Ignore the close event