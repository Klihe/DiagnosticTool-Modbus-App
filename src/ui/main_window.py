from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QComboBox

from ui.menu_section import MenuSection
from ui.tool_section import ToolSection
from ui.comm_section import CommSection
from ui.table_section import TableSection

class MainWindow(QMainWindow):
    """Main window class.

    Args:
        QMainWindow (QMainWindow): The base class for all main window objects.
    """
    def __init__(self, config: dict):
        """Initialize the main window.

        Args:
            config (dict): The configuration settings.
        """
        super().__init__()
        
        # Set the window title
        self.setWindowTitle(config["window"]["title"])
        # Set the window icon
        self.setGeometry(
            config["window"]["x_position"],
            config["window"]["y_position"],
            config["window"]["width"],
            config["window"]["height"]
        )
        
        self.__page_layout = QHBoxLayout()
        self.__comm_layout = QVBoxLayout()
        self.__table_layout = QVBoxLayout()
        
        self.menu_section = MenuSection(self)
        self.tool_section = ToolSection(self)
        self.comm_section = CommSection(config)
        self.table_section = TableSection(config)
        
        self.comm_section.addSection(self.__comm_layout)
        self.table_section.addSection(self.__table_layout)
        
        self.__page_layout.addLayout(self.__comm_layout)
        self.__page_layout.addLayout(self.__table_layout)
        
        self.__widget = QWidget()
        self.__widget.setLayout(self.__page_layout)
        self.setCentralWidget(self.__widget)