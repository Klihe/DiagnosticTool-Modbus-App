from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Example")
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Create buttons and assign IDs
        self.buttons = {}
        for i in range(5):
            button = QPushButton(f"Button {i+1}")
            button.clicked.connect(self.create_button_handler(i))
            self.layout.addWidget(button)
            self.buttons[i] = button

    def create_button_handler(self, button_id):
        def handler():
            print(f"Button {button_id + 1} clicked")
        return handler

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
