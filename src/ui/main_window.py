from PyQt6.QtWidgets import QMainWindow

from ui.menu_section import MenuSection

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
        self.setWindowTitle(config.get("window_title", "Default Title"))
        # Set the window icon
        self.setGeometry(
            config.get("window_x_position", 100),
            config.get("window_y_position", 100),
            config.get("window_width", 800),
            config.get("window_height", 600)
        )
        
        
        self.__menu_section = MenuSection(self)