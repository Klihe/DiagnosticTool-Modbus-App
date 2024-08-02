from PyQt6.QtWidgets import QToolButton
from ui.main_window import MainWindow
from utils.custom_thread import CustomThread
from models.device import Device


class ToolController:
    def __init__(self, parent: MainWindow, device: Device) -> None:
        self.__parent = parent
        self.__device = device

        self.__find()
        self.__connect()

    def __find(self) -> None:
        self.__connect_ = self.__parent.findChild(QToolButton, "Connect")
        self.__disconnect = self.__parent.findChild(QToolButton, "Disconnect")
        self.__write = self.__parent.findChild(QToolButton, "Write")
        self.__read = self.__parent.findChild(QToolButton, "Read")
        self.__read_in_interval = self.__parent.findChild(
            QToolButton, "ReadInInterval_button"
        )
        self.__compare = self.__parent.findChild(QToolButton, "Compare")
        self.__reset_plot = self.__parent.findChild(QToolButton, "ResetPlot")

    def __connect(self) -> None:
        self.__connect_.clicked.connect(self.__connect_func)
        self.__disconnect.clicked.connect(self.__disconnect_func)
        self.__write.clicked.connect(lambda: print("Write"))
        self.__read.clicked.connect(lambda: print("Read"))
        self.__read_in_interval.clicked.connect(lambda: print("ReadInInterval"))
        self.__compare.clicked.connect(lambda: print("Compare"))
        self.__reset_plot.clicked.connect(lambda: print("ResetPlot"))

    def __connect_func(self) -> None:
        data = self.__parent.comm_section.get_data()

        def thread_func() -> None:
            if data["client"] == "Serial":
                method = data["method"]
                port = data["port"]
                baudrate = data["baudrate"]
                byte_size = data["bytesize"]
                parity = data["parity"]
                stop_bits = data["stopbits"]
                
            self.__device.connect(method, port, baudrate, byte_size, parity, stop_bits)
            
        def after_thread_func() -> None:
            self.__parent.table_section.prepareTable(self.__device.data)

        self.__connect_device_thread = CustomThread()
        self.__connect_device_thread.set_function(thread_func)
        self.__connect_device_thread.finished.connect(after_thread_func)
        self.__connect_device_thread.start()

    def __disconnect_func(self) -> None:
        def thread_func() -> None:
            self.__device.disconnect()

        self.__disconnect_device_thread = CustomThread()
        self.__disconnect_device_thread.set_function(thread_func)
        self.__disconnect_device_thread.start()

    def __read_func(self) -> None:
        def thread_func() -> None:
            self.__device.read()
            self.__parent.table_section.updateValues(self.__device.data["value"])

        self.__read_device_thread = CustomThread()
        self.__read_device_thread.set_function(thread_func)
        self.__read_device_thread.start()
