from PyQt6.QtWidgets import QMainWindow, QPushButton, QComboBox
from utils.custom_thread import CustomThread

from ui.main_window import MainWindow

from models.ports import find_ports

class CommController:
    def __init__(self, parent: MainWindow) -> None:
        self.__parent = parent

        self.__find()
        self.__connect()
        
    def __find(self) -> None:
        self.__port_refresh = self.__parent.findChild(QPushButton, "port_refresh_button")
        self.__client_options_box = self.__parent.findChild(QComboBox, "client_options_box")
        
    def __connect(self) -> None:
        self.__port_refresh.clicked.connect(self.__port_refresh_func)
        self.__client_options_box.currentTextChanged.connect(self.__client_options_box_func)
    
    def __port_refresh_func(self) -> None:
        
        def thread_func() -> None:
            find_ports()
            
        def after_thread_func() -> None:
            self.__parent.findChild(QComboBox, "port_options_box").clear()
            self.__parent.findChild(QComboBox, "port_options_box").addItems(find_ports())
        
        self.__port_refresh_thread = CustomThread()
        self.__port_refresh_thread.set_function(thread_func)
        self.__port_refresh_thread.finished.connect(after_thread_func)
        self.__port_refresh_thread.start()
        
    def __client_options_box_func(self) -> None:
        self.__parent.comm_section.change_client()
