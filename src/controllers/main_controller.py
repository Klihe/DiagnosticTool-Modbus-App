from PyQt6.QtWidgets import QPushButton, QToolButton, QComboBox
from PyQt6.QtGui import QAction
from ui.main_window import MainWindow

class MainController:
    def __init__(self, config) -> None:
        self.__config = config
        self.__main_window = MainWindow(self.__config)
        self.__setup_connections()
    
    def __setup_connections(self) -> None:
        self.__open_file = self.__main_window.findChild(QAction, "open_file")
        self.__save = self.__main_window.findChild(QAction, "save_file")
        self.__save_as = self.__main_window.findChild(QAction, "save_as_file")
        self.__open_compare = self.__main_window.findChild(QAction, "open_compare")
        self.__open_plot = self.__main_window.findChild(QAction, "open_plot")
        
        self.__connect = self.__main_window.findChild(QToolButton, "Connect")
        self.__disconnect = self.__main_window.findChild(QToolButton, "Disconnect")
        self.__write = self.__main_window.findChild(QToolButton, "Write")
        self.__read = self.__main_window.findChild(QToolButton, "Read")
        self.__read_in_interval = self.__main_window.findChild(QToolButton, "ReadInInterval_button")
        self.__compare = self.__main_window.findChild(QToolButton, "Compare")
        self.__reset_plot = self.__main_window.findChild(QToolButton, "ResetPlot")
        
        self.__client_options_box = self.__main_window.findChild(QComboBox, "client_options_box")
        
        self.__open_file.triggered.connect(lambda: print("Open"))
        self.__save.triggered.connect(lambda: print("Save"))
        self.__save_as.triggered.connect(lambda: print("SaveAs"))
        self.__open_compare.triggered.connect(lambda: print("OpenCompare"))
        self.__open_plot.triggered.connect(lambda: print("OpenPlot"))
        
        self.__connect.clicked.connect(lambda: print("Connect"))
        self.__disconnect.clicked.connect(lambda: print("Disconnect"))
        self.__write.clicked.connect(lambda: print("Write"))
        self.__read.clicked.connect(lambda: print("Read"))
        self.__read_in_interval.toggled.connect(lambda checked: print("ReadInInterval") if checked else print("StopReadInInterval"))
        self.__compare.clicked.connect(lambda: print("Compare"))
        self.__reset_plot.clicked.connect(lambda: print("ResetPlot"))
        
        self.__client_options_box.currentTextChanged.connect(self.__change_client)
    
    def show(self) -> None:
        self.__main_window.show()
        
    def __change_client(self) -> None:
        self.__main_window.comm_section.change_client()