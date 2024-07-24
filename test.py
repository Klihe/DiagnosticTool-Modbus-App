from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QVBoxLayout, QPushButton, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Confirm Quit Example")
        self.setGeometry(300, 300, 400, 200)

        # Create a simple button in the main window
        self.button = QPushButton("Click me", self)
        self.button.clicked.connect(self.on_button_clicked)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)

        # Create a container widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_button_clicked(self):
        print("Button clicked")

    def closeEvent(self, event):
        # Show a message box to confirm exit
        reply = QMessageBox.question(self, 'Quit Confirmation',
                                     "Are you sure you want to quit?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()  # Close the window
        else:
            event.ignore()  # Ignore the close event

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
