from PyQt6.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QLayout, QHBoxLayout
from PyQt6.QtCore import Qt

class CommState:
    def __init__(self) -> None:
        self.__create()
        
    def __create(self) -> None:
        pass

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
        self.__options_box.addItems(self.__options)
        self.__options_box.setCurrentText(self.__default_option)
        self.__options_box.setObjectName(self.__id + "_options_box")
        print(self.__id + "_options_box")
        
        self.__edit = QLineEdit()
        self.__edit.hide()
        
        if self.__custom:
            self.__custom_switch = QPushButton("Custom")
            self.__custom_switch.setCheckable(True)
            self.__custom_switch.setObjectName(self.__id + "_custom_switch")
            
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
                data = self.__options.currentText()
        else:
            data = self.__options.currentText()
            
        return data
    
    def _hide(self) -> None:
        self.__item_layout.hide()
        
    def _show(self) -> None:
        self.__item_layout.show()
    
class CommSection(QWidget):
    def __init__(self, config: dict) -> None:
        super().__init__()
        self.__config = config
        
        self.__create()
        
    def __create(self) -> None:
        
        self.__client = CommLine(descr="Client", options=self.__config["communication"]["client_options"],  default_option=self.__config["communication"]["client_default"], custom=False, refresh=False)
        self.__method = CommLine(descr="Method", options=self.__config["communication"]["method_options"],  default_option=self.__config["communication"]["client_default"], custom=True, refresh=False)
        self.__port = CommLine(descr="Port", options=self.__config["communication"]["port_options"],  default_option=self.__config["communication"]["client_default"], custom=False, refresh=True)
        self.__bytesize = CommLine(descr="Byte Size", options=self.__config["communication"]["bytesize_options"],  default_option=self.__config["communication"]["client_default"], custom=True, refresh=False)
        self.__parity = CommLine(descr="Parity", options=self.__config["communication"]["parity_options"],  default_option=self.__config["communication"]["client_default"], custom=True, refresh=False)
        self.__stopbits = CommLine(descr="Stop Bits", options=self.__config["communication"]["stopbits_options"],  default_option=self.__config["communication"]["client_default"], custom=True, refresh=False)
        
    def addSection(self, layout: QLayout) -> None:
        self.__layout = layout
        
        self.__client._addLine(self.__layout)
        self.__method._addLine(self.__layout)
        self.__port._addLine(self.__layout)
        self.__bytesize._addLine(self.__layout)
        self.__parity._addLine(self.__layout)
        self.__stopbits._addLine(self.__layout)

    def __update_client(self) -> None:
        if self.__client._get() == "Serial":
            self.__method._show()
            self.__port._show()
            self.__bytesize._show()
            self.__parity._show()
            self.__stopbits._show()
        elif self.__client._get() == "TCP":
            self.__method._hide()
            self.__port._hide()
            self.__bytesize._hide()
            self.__parity._hide()
            self.__stopbits._hide()