from PyQt6.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QLayout, QHBoxLayout
from PyQt6.QtCore import Qt, pyqtSlot

class CommState:
    def __init__(self) -> None:
        self.__create()
        
    def __create(self) -> None:
        self.__label = QLabel("State")
        self.__label.setStyleSheet("background-color: white;")
        self.__label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__label.setFixedHeight(30)
        
        self.__label.setObjectName("state_label")
        
    def change_state(self, text: str, color: str) -> None:
        self.__label.setText(text)
        self.__label.setStyleSheet(f"background-color: {color};")
        
    def addState(self, layout: QLayout) -> None:
        layout.addWidget(self.__label)

class CommLine(QWidget):
    def __init__(self, descr: str, options: list[None], default_option: str, custom: bool, refresh: bool) -> None:
        
        super().__init__()
        self.__id = descr.lower()
        self.__descr = descr
        self.__options = options
        self.__default_option = default_option
        self.__custom = custom
        self.__refresh = refresh
        
        self.__create()
        
    def __create(self) -> None:
        self.__item_layout = QHBoxLayout()
        
        self.__label = QLabel(self.__descr)
        
        self.__options_box = QComboBox()
        self.__options_box.setObjectName(self.__id + "_options_box")
        self.__options_box.addItems(self.__options)
        self.__options_box.setCurrentText(self.__default_option)
        
        self.__edit = QLineEdit()
        self.__edit.setObjectName(self.__id + "_edit")
        self.__edit.hide()
        
        self.__custom_switch = None
        if self.__custom:
            self.__custom_switch = QPushButton("Custom")
            self.__custom_switch.setObjectName(self.__id + "_custom_switch")
            self.__custom_switch.setCheckable(True)
            self.__custom_switch.toggled.connect(self.__toggle)
            
        self.__refresh_button = None
        if self.__refresh:
            self.__refresh_button = QPushButton("Refresh")
            self.__refresh_button.setObjectName(self.__id + "_refresh_button")
            
    def _addLine(self, layout: QLayout) -> None:
        self.__layout = layout
        
        self.__item_layout.addWidget(self.__label)
        self.__item_layout.addWidget(self.__options_box)
        self.__item_layout.addWidget(self.__edit)
        
        if self.__custom:
            self.__item_layout.addWidget(self.__custom_switch)
            
        if self.__refresh:
            self.__item_layout.addWidget(self.__refresh_button)
            
        self.__layout.addLayout(self.__item_layout)
            
    def _get(self) -> str:
        data = ""
        
        if self.__custom:
            if self.__custom_switch.isChecked():
                data = self.__edit.text()
            else:
                data = self.__options_box.currentText()
        else:
            data = self.__options_box.currentText()
            
        return data
    
    def _hide(self) -> None:
        self.__label.hide()
        self.__options_box.hide()
        self.__edit.hide()
        
        if self.__custom:
            self.__custom_switch.hide()
        if self.__refresh:
            self.__refresh_button.hide()
        
    def _show(self) -> None:
        self.__label.show()
        
        if self.__custom_switch is not None:
            if self.__custom_switch.isChecked():
                self.__edit.show()
            else:
                self.__options_box.show()
        elif self.__options_box is not None:
            self.__options_box.show()
        
        if self.__custom:
            self.__custom_switch.show()
        if self.__refresh:
            self.__refresh_button.show()
    
    @pyqtSlot()     
    def __toggle(self) -> None:
        if self.__custom_switch.isChecked():
            self.__options_box.hide()
            self.__edit.show()
        else:
            self.__edit.hide()
            self.__options_box.show()
    
class CommSection(QWidget):
    def __init__(self, config: dict) -> None:
        super().__init__()
        
        self.__config = config
        
        self.__create()
        
    def __create(self) -> None:
        
        self.__state = CommState()
        
        self.__client = CommLine(descr="Client", options=self.__config["communication"]["client_options"],  default_option=self.__config["communication"]["client_default"], custom=False, refresh=False)
        self.__method = CommLine(descr="Method", options=self.__config["communication"]["method_options"],  default_option=self.__config["communication"]["client_default"], custom=True, refresh=False)
        self.__port = CommLine(descr="Port", options=self.__config["communication"]["port_options"],  default_option=self.__config["communication"]["client_default"], custom=False, refresh=True)
        self.__baudrate = CommLine(descr="Baudrate", options=self.__config["communication"]["baudrate_options"],  default_option=self.__config["communication"]["client_default"], custom=True, refresh=False)
        self.__bytesize = CommLine(descr="Byte Size", options=self.__config["communication"]["bytesize_options"],  default_option=self.__config["communication"]["client_default"], custom=True, refresh=False)
        self.__parity = CommLine(descr="Parity", options=self.__config["communication"]["parity_options"],  default_option=self.__config["communication"]["client_default"], custom=True, refresh=False)
        self.__stopbits = CommLine(descr="Stop Bits", options=self.__config["communication"]["stopbits_options"],  default_option=self.__config["communication"]["client_default"], custom=True, refresh=False)
        
        self.__ip = CommLine(descr="IP", options=self.__config["communication"]["ip_options"],  default_option=self.__config["communication"]["client_default"], custom=True, refresh=False)
        self.__server = CommLine(descr="Server", options=self.__config["communication"]["server_options"],  default_option=self.__config["communication"]["client_default"], custom=False, refresh=False)
        
    def addSection(self, layout: QLayout) -> None:
        self.__layout = layout
        
        self.__state.addState(self.__layout)
        
        self.__client._addLine(self.__layout)
        self.__method._addLine(self.__layout)
        self.__port._addLine(self.__layout)
        self.__baudrate._addLine(self.__layout)
        self.__bytesize._addLine(self.__layout)
        self.__parity._addLine(self.__layout)
        self.__stopbits._addLine(self.__layout)
        
        self.__ip._addLine(self.__layout)
        self.__server._addLine(self.__layout)
        
        self.__ip._hide()
        self.__server._hide()

    def change_client(self) -> None:
        if self.__client._get() == "Serial":
            # TCP
            self.__ip._hide()
            self.__server._hide()
            # Serial
            self.__method._show()
            self.__port._show()
            self.__baudrate._show()
            self.__bytesize._show()
            self.__parity._show()
            self.__stopbits._show()
        elif self.__client._get() == "TCP":
            # Serial
            self.__method._hide()
            self.__port._hide()
            self.__baudrate._hide()
            self.__bytesize._hide()
            self.__parity._hide()
            self.__stopbits._hide()
            # TCP
            self.__ip._show()
            self.__server._show()
    
    def get_data(self) -> dict:
        data = {
            "client": self.__client._get(),
            "method": self.__method._get(),
            "port": self.__port._get(),
            "baudrate": self.__baudrate._get(),
            "bytesize": self.__bytesize._get(),
            "parity": self.__parity._get(),
            "stopbits": self.__stopbits._get(),
            "ip": self.__ip._get(),
            "server": self.__server._get()
        }
        
        return data