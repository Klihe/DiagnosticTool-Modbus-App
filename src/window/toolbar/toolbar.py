from PyQt6.QtWidgets import QToolBar, QMainWindow
from PyQt6.QtGui import QAction

from window.toolbar.helpers import ValueButton

class ToolBar:
    def __init__(self, grabber: dict, window: QMainWindow) -> None:
        self.__grabber = grabber
        self.__window = window
        
        self._create()
        
    def _create(self) -> None:
        self.__toolbar = QToolBar()
        self.__window.addToolBar(self.__toolbar)
        
        self.__grabber["connect"] = QAction("Connect", self.__window)
        self.__toolbar.addAction(self.__grabber["connect"])
        
        self.__grabber["disconnect"] = QAction("Disconnect", self.__window)
        self.__toolbar.addAction(self.__grabber["disconnect"])
        
        self.__grabber["write"] = QAction("Write", self.__window)
        self.__toolbar.addAction(self.__grabber["write"])
        
        self.__grabber["read"] = QAction("Read", self.__window)
        self.__toolbar.addAction(self.__grabber["read"])
        
        self.__value_button = ValueButton(self.__grabber, "readInInterval", self.__window)
        self.__value_button.addAction(self.__toolbar)
        
        

    def on_button_clicked(self):
        # Get text from the entry and update the label
        entered_text = self.entry.text()
        self.label.setText(f"Submitted text: {entered_text}")
        