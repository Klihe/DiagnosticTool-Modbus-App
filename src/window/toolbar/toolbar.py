from PyQt6.QtWidgets import QToolBar, QToolButton, QMainWindow
from PyQt6.QtGui import QAction

from window.toolbar.helpers import ValueButton

# ToolBar class
class ToolBar:
    def __init__(self, grabber: dict, window: QMainWindow) -> None:
        self.__grabber = grabber
        self.__window = window
        
        self._create()
    
    # Create the toolbar
    def _create(self) -> None:
        # Create the toolbar
        self.__toolbar = QToolBar()
        self.__window.addToolBar(self.__toolbar)
        
        # Create the actions - connect and disconnect
        self.__grabber["connect"] = QAction("Connect", self.__window)
        self.__grabber["connect_btn"] = QToolButton()
        self.__grabber["connect_btn"].setDefaultAction(self.__grabber["connect"])
        self.__grabber["connect_btn"].setStyleSheet("background-color: #0D825D;")
        self.__toolbar.addWidget(self.__grabber["connect_btn"])
        
        self.__grabber["disconnect"] = QAction("Disconnect", self.__window)
        self.__grabber["disconnect_btn"] = QToolButton()
        self.__grabber["disconnect_btn"].setDefaultAction(self.__grabber["disconnect"])
        self.__grabber["disconnect_btn"].setStyleSheet("background-color: #D53734;")
        self.__toolbar.addWidget(self.__grabber["disconnect_btn"])
        
        # Create the actions - write and read
        self.__grabber["write"] = QAction("Write", self.__window)
        self.__grabber["write_btn"] = QToolButton()
        self.__grabber["write_btn"].setDefaultAction(self.__grabber["write"])
        self.__grabber["write_btn"].setStyleSheet("background-color: #D53734;")
        self.__toolbar.addWidget(self.__grabber["write_btn"])
        
        self.__grabber["read"] = QAction("Read", self.__window)
        self.__grabber["read_btn"] = QToolButton()
        self.__grabber["read_btn"].setDefaultAction(self.__grabber["read"])
        self.__grabber["read_btn"].setStyleSheet("background-color: #D53734;")
        self.__toolbar.addWidget(self.__grabber["read_btn"])
        
        # Create the value button = read in interval
        self.__value_button = ValueButton(self.__grabber, "readInInterval", self.__window)
        self.__value_button.addAction(self.__toolbar)
        
    def on_button_clicked(self):
        # Get text from the entry and update the label
        entered_text = self.entry.text()
        self.label.setText(f"Submitted text: {entered_text}")
        