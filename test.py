import sys
import threading
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel
from PyQt6.QtCore import Qt, QThread, pyqtSignal

class WorkerThread(QThread):
    finished = pyqtSignal(int)

    def __init__(self, target=None, args=(), kwargs={}, *, daemon=None):
        super().__init__()
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._daemon = daemon

    def run(self):
        result = self._target(*self._args, **self._kwargs)
        self.finished.emit(result)

def calculate_fibonacci(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Multi-Threading Example")
        self.setGeometry(100, 100, 400, 200)
        
        layout = QVBoxLayout()
        
        self.result_label = QLabel("Result will appear here")
        layout.addWidget(self.result_label)
        
        self.start_button = QPushButton("Start Calculation")
        self.start_button.clicked.connect(self.start_calculation)
        layout.addWidget(self.start_button)
        
        self.dummy_button = QPushButton("Dummy Button")
        self.dummy_button.clicked.connect(lambda: print("Dummy button clicked"))
        layout.addWidget(self.dummy_button)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        self.n = 35
        self.worker_thread = None
    
    def start_calculation(self):
        if self.worker_thread is None or not self.worker_thread.isRunning():
            self.result_label.setText("Calculating...")
            self.start_button.setEnabled(False)
            self.worker_thread = WorkerThread(calculate_fibonacci, (35,))
            self.worker_thread.finished.connect(self.display_result)
            self.worker_thread.start()
    
    def display_result(self, result):
        self.result_label.setText(f"Result: {result}")
        self.start_button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
