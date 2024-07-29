from PyQt6.QtWidgets import QMainWindow

class MenuController:
    def __init__(self, parent: QMainWindow) -> None:
        self.__parent = parent
        
        self.__find()
        self.__connect()
        
    def __find(self) -> None:
        pass
    
    def __connect(self) -> None:
        pass