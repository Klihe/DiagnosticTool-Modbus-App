from PyQt6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Main Window")      # Get the values from config/settings.py
        self.setGeometry(100, 100, 800, 600)    # Get the values from config/settings.py
        