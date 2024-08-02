import sys
from PyQt6.QtWidgets import QApplication
from controllers.main_controller import MainController
from models.device import Device
from config.settings import load_settings


class Application:
    """Application class."""

    def __init__(self):
        """Initialize the application."""
        # Create the application
        self.app = QApplication(sys.argv)

        # Configuration settings
        self.__config = load_settings()
        # Stylesheet
        # self.__stylesheet = load_stylesheet()

        # Set the stylesheet
        # self.app.setStyleSheet(self.__stylesheet)

        # Create the device
        self.__device = Device(self.__config)
        # Create the main window
        self.__controller = MainController(self.__config, self.__device)

        # Show the main window
        self.__controller.show()

    def run(self):
        """Run the application."""
        # Run the application
        self.app.exec()


# Run the main function
if __name__ == "__main__":
    # Create the application
    app = Application()

    # Run the application
    app.run()
