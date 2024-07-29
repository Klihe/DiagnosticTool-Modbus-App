from PyQt6.QtWidgets import QMainWindow, QPushButton, QComboBox
from models.ports import find_ports

class CommController:
    def __init__(self, parent: QMainWindow) -> None:
        self.__parent = parent

        self.__find()
        self.__connect()
        
    def __find(self) -> None:
        self.__port_refresh = self.__parent.findChild(QPushButton, "port_refresh_button")
        self.__client_options_box = self.__parent.findChild(QComboBox, "client_options_box")
        
    def __connect(self) -> None:
        self.__port_refresh.clicked.connect(find_ports)
        self.__client_options_box.currentTextChanged.connect(self.__client_options_box_func)
        
    def __client_options_box_func(self) -> None:
        self.__parent.comm_section.change_client()
