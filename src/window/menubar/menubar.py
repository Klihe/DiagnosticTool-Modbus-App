from PyQt6.QtGui import QAction

class MenuBar:
    def __init__(self, window) -> None:
        self.__window = window
        self._create()
        
    def onMyToolBarButtonClick(self) -> None:
        print("You clicked on your button")
        
    def _create(self) -> None:
        self.__menu = self.__window.menuBar()

        # buttons
        self.__button_action = QAction("Your button", self.__window)
        self.__button_action.setStatusTip("This is your button")
        self.__button_action.triggered.connect(self.__window.onMyToolBarButtonClick)
        
        self.__button2_action = QAction("Your button", self.__window)
        self.__button2_action.setStatusTip("This is your button")
        self.__button2_action.triggered.connect(self.__window.onMyToolBarButtonClick)
        
        self.__save_menu = self.__menu.addMenu("Save")
        self.__save_menu.addAction(self.__button_action)
        self.__save_menu.addAction(self.__button2_action)
    
        self.__export_menu = self.__menu.addMenu("Export")
        self.__export_menu.addAction(self.__button_action)
        
        self.__import_menu = self.__menu.addMenu("Import")
        self.__import_menu.addAction(self.__button_action)
        
        