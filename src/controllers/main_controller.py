from PyQt6.QtWidgets import QPushButton, QToolButton, QComboBox
from PyQt6.QtGui import QAction
from ui.main_window import MainWindow

from controllers.menu_controller import MenuController
from controllers.tool_controller import ToolController
from controllers.comm_controller import CommController
from controllers.table_controller import TableController

from models.ports import find_ports

class MainController:
    def __init__(self, config) -> None:
        self.__config = config
        self.__main_window = MainWindow(self.__config)
        
        self.__menu_controller = MenuController(self.__main_window)
        self.__tool_controller = ToolController(self.__main_window)
        self.__comm_controller = CommController(self.__main_window)
        self.__table_controller = TableController(self.__main_window)
    
    def show(self) -> None:
        self.__main_window.show()
