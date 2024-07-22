from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QAction

# Class for menu bar
class MenuBar:
    def __init__(self, grabber: dict, window: QMainWindow) -> None:
        self.__grabber = grabber
        self.__window = window
        
        self._create()
        
    def _create(self) -> None:
        # Create the menu bar
        self.__menu = self.__window.menuBar()
        
        # Create the actions
        self.__grabber["open"] = QAction("Open", self.__window)
        self.__grabber["save"] = QAction("Save", self.__window)
        self.__grabber["saveas"] = QAction("Save As", self.__window)
        
        # Add the actions to the menu
        self.__save_menu = self.__menu.addMenu("File")
        self.__save_menu.addAction(self.__grabber["open"])
        self.__save_menu.addAction(self.__grabber["save"])
        self.__save_menu.addAction(self.__grabber["saveas"])
        