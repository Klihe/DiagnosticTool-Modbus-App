import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from config.settings import load_settings

class Application:
    """Application class.
    """
    def __init__(self):
        """Initialize the application.
        """
        # Create the application
        self.app = QApplication(sys.argv)
        
        # Configuration settings
        self.__config = load_settings()
        
        # Create the main window
        self.__window = MainWindow(self.__config)
        
        # Show the main window
        self.__window.show()
        
    def run(self):
        """Run the application.
        """
        # Run the application
        self.app.exec()

# Run the main function
if __name__ == "__main__":
    # Create the application
    app = Application()
    
    # Run the application
    app.run()