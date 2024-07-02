from PyQt6.QtWidgets import QToolBar, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QHBoxLayout
from PyQt6.QtGui import QAction, QActionGroup, QIcon

from window.toolbar.helpers import ActionGroup, ValueButton

class ToolBar:
    def __init__(self, window) -> None:
        self.__window = window
        self._create()
        
    def onMyToolBarButtonClick(self) -> None:
        print("You clicked on your button")
        
    def _create(self) -> None:
        self.__toolbar = QToolBar("Main Toolbar")
        self.__window.addToolBar(self.__toolbar)
        
        self.__action_group1 = ActionGroup(self.__toolbar, self.__window)
        self.__action_group1.addAction("ReadFromDevice")
        self.__action_group1.addAction("ReadFromCSV")
        
        self.__action_group1.triggered_connect("ReadFromDevice", self.__window.onMyToolBarButtonClick)
        self.__action_group1.triggered_connect("ReadFromCSV", self.__window.onMyToolBarButtonClick)
        
        self.__button_action = QAction("Read", self.__window)
        
        self.__button_action.setStatusTip("This is your button")
        self.__button_action.triggered.connect(self.__window.onMyToolBarButtonClick)
        self.__toolbar.addAction(self.__button_action)
        
        self.valuebutton = ValueButton("ReadInInterval", self.__toolbar, self.__window)  
        
        self.__action_group2 = ActionGroup(self.__toolbar, self.__window)
        self.__action_group2.addAction("WriteToDevice")
        self.__action_group2.addAction("WriteToCSV")
        
        self.__action_group2.triggered_connect("WriteToDevice", self.__window.onMyToolBarButtonClick)
        self.__action_group2.triggered_connect("WriteToCSV", self.__window.onMyToolBarButtonClick)
        
        self.__write_button_action = QAction("Write", self.__window)
        
        self.__write_button_action.setStatusTip("This is your button")
        self.__write_button_action.triggered.connect(self.__window.onMyToolBarButtonClick)
        self.__toolbar.addAction(self.__write_button_action)
        

    def on_button_clicked(self):
        # Get text from the entry and update the label
        entered_text = self.entry.text()
        self.label.setText(f"Submitted text: {entered_text}")
        