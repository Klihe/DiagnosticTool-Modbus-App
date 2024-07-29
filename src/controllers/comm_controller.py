from PyQt6.QtWidgets import QMainWindow, QPushButton
from models.ports import find_ports

class CommController:
    def __init__(self, parent: QMainWindow) -> None:
        self.__parent = parent

        self.__find()
        self.__connect()
        
    def __find(self) -> None:
        self.__port_refresh = self.__parent.findChild(QPushButton, "port_refresh_button")
        
    def __connect(self) -> None:
        self.__port_refresh.clicked.connect(find_ports())