from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QAction

class MenuBar:
    def __init__(self, grabber: dict, window: QMainWindow) -> None:
        self.__grabber = grabber
        self.__window = window
        
        self._create()
        
    def _create(self) -> None:
        self.__menu = self.__window.menuBar()
        
        self.__grabber["save"] = QAction("Save", self.__window)
        self.__grabber["saveas"] = QAction("Save As", self.__window)
        self.__grabber["export"] = QAction("Export", self.__window)
        self.__grabber["import"] = QAction("Import", self.__window)
        
        self.__save_menu = self.__menu.addMenu("Save")
        self.__save_menu.addAction(self.__grabber["save"])
        self.__save_menu.addAction(self.__grabber["saveas"])
    
        self.__import_menu = self.__menu.addMenu("Import")
        self.__import_menu.addAction(self.__grabber["import"])
        
        self.__export_menu = self.__menu.addMenu("Export")
        self.__export_menu.addAction(self.__grabber["export"])