from PyQt6.QtWidgets import QToolBar
from PyQt6.QtGui import QAction

from window.toolbar.helpers import ActionGroup, ValueButton, StateButton

class ToolBar:
    def __init__(self, window, grabber) -> None:
        self.__window = window
        self.__grabber = grabber
        self._create()
        
    def _create(self) -> None:
        self.__toolbar = QToolBar()
        self.__window.addToolBar(self.__toolbar)
        
        self.__state_button = StateButton("Connect", "Disconnect", self.__window, self.__grabber)
        self.__state_button.addAction(self.__toolbar)
        
        self.__action_group1 = ActionGroup(self.__toolbar, self.__window, self.__grabber)
        self.__action_group1.addAction("ReadFromDevice")
        self.__action_group1.addAction("ReadFromCSV")
        
        self.__grabber["read"] = QAction("Read", self.__window)
        self.__toolbar.addAction(self.__grabber["read"])
        
        self.__value_button = ValueButton("ReadInInterval", self.__window, self.__grabber)
        self.__value_button.addAction(self.__toolbar)
        
        self.__action_group2 = ActionGroup(self.__toolbar, self.__window, self.__grabber)
        self.__action_group2.addAction("WriteToDevice")
        self.__action_group2.addAction("WriteToCSV")
        
        self.__grabber["write"] = QAction("Write", self.__window)
        self.__toolbar.addAction(self.__grabber["write"])
        

    def on_button_clicked(self):
        # Get text from the entry and update the label
        entered_text = self.entry.text()
        self.label.setText(f"Submitted text: {entered_text}")
        