import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Application with Icon")
        self.setGeometry(300, 300, 400, 200)

        # Set the window icon
        icon_path = os.path.join(os.path.dirname(__file__), 'src/peg.png')
        self.setWindowIcon(QIcon(icon_path))

        # Create a QLabel
        self.label = QLabel("This is a sample application with an icon.", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        # Create a container widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
