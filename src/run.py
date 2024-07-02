from PyQt6.QtWidgets import QApplication

from window.window import Window

import sys

def main() -> None:
    app  = QApplication(sys.argv)
    
    window = Window()
    window.show()
    
    app.exec()

if __name__ == '__main__':
    main()