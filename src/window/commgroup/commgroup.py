from PyQt6.QtWidgets import QLabel, QComboBox, QLineEdit, QPushButton, QLayout, QGridLayout, QHBoxLayout
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt

import window.commgroup.constants as c

class StateIndicator:
    def __init__(self, grabber: dict) -> None:
        self.__grabber = grabber
        
        self.__create()
        
    def __create(self) -> None:
        self.__grabber["state_indicator"] = QLabel("Disconnected")
        self.__grabber["state_indicator"].setStyleSheet("background-color: red;")
        self.__grabber["state_indicator"].setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__grabber["state_indicator"].setFixedHeight(30)
        
    def _update(self, state: str, color: str) -> None:
        self.__grabber["state_indicator"].setText(state)
        self.__grabber["state_indicator"].setStyleSheet(f"background-color: {color};")
        
    def _addStateIndicator(self, layout: QLayout) -> None:
        layout.addWidget(self.__grabber["state_indicator"])

class CommLine:
    def __init__(self, grabber, descr: str, options: list=[None], custom: bool=True, refresh: bool=False) -> None:
        self.__grabber = grabber
        self.__mark = descr.lower()
        self.__label = descr
        self.__options = options
        self.__custom = custom
        self.__refresh = refresh
        
        self.__create()
        
    def __create(self) -> None:
        self.__items_layout = QHBoxLayout()   
        self.__grabber[f"{self.__mark}_descr"] = QLabel(self.__label)
        
        self.__grabber[f"{self.__mark}_option"] = QComboBox()
        self.__grabber[f"{self.__mark}_option"].addItems(self.__options)
        
        self.__grabber[f"{self.__mark}_custom_opt"] = QLineEdit()
        self.__grabber[f"{self.__mark}_custom_opt"].hide()
        
        if self.__custom:
            self.__grabber[f"{self.__mark}_custom_swt"] = QPushButton("Custom")
            self.__grabber[f"{self.__mark}_custom_swt"].setCheckable(True)

            self.__grabber[f"{self.__mark}_custom_swt"].toggled.connect(self.__toggle)

        if self.__refresh:
            self.__grabber[f"{self.__mark}_refresh"] = QPushButton("Refresh")
    
    def _get(self) -> str:
        data = ""
        
        if self.__custom:
            if self.__grabber[f"{self.__mark}_custom_swt"].isChecked():
                data = self.__grabber[f"{self.__mark}_custom_opt"].text()
            else:
                data = self.__grabber[f"{self.__mark}_option"].currentText()
        else: 
            data = self.__grabber[f"{self.__mark}_option"].currentText()
            
        return data
            
    def _addLine(self, layout: QLayout) -> None:
        self.__layout = layout

        self.__items_layout.addWidget(self.__grabber[f"{self.__mark}_descr"]),
        self.__items_layout.addWidget(self.__grabber[f"{self.__mark}_option"])
        self.__items_layout.addWidget(self.__grabber[f"{self.__mark}_custom_opt"])
        
        if self.__custom:
            self.__items_layout.addWidget(self.__grabber[f"{self.__mark}_custom_swt"])
            
        if self.__refresh:
            self.__items_layout.addWidget(self.__grabber[f"{self.__mark}_refresh"])
            
        self.__layout.addLayout(self.__items_layout)
            
    def __toggle(self, checked: bool) -> None:
        if checked:
            print("Custom switch checked")
            self.__grabber[f"{self.__mark}_custom_opt"].show()
            self.__grabber[f"{self.__mark}_option"].hide()
        else:
            print("Custom switch unchecked")
            self.__grabber[f"{self.__mark}_option"].show()
            self.__grabber[f"{self.__mark}_custom_opt"].hide()
    
class CommGroup:
    def __init__(self, grabber: dict) -> None:
        self.__method = CommLine(grabber, descr="Method", options=c.METHOD_OPTIONS)
        self.__port = CommLine(grabber, descr="Port", custom=False, refresh=True)
        self.__baudrate = CommLine(grabber, descr="Baudrate", options=c.BAUDRATE_OPTIONS)
        self.__bytesize = CommLine(grabber, descr="Byte Size", options=c.BYTESIZE_OPTIONS)
        self.__parity = CommLine(grabber, descr="Parity", options=c.PARITY_OPTIONS)
        self.__stopbits = CommLine(grabber, descr="Stop Bits", options=c.STOPBITS_OPTIONS)
        self.__state_indicator = StateIndicator(grabber)
        
    def get(self) -> dict:
        data = {
            "method": self.__method._get(),
            "port": self.__port._get(),
            "baudrate": self.__baudrate._get(),
            "bytesize": self.__bytesize._get(),
            "parity": self.__parity._get(),
            "stopbits": self.__stopbits._get()
        }
        
        return data
    
    def update_state(self, state: str, color: str) -> None:
        self.__state_indicator._update(state, color)
        
    def addGroup(self, layout: QLayout) -> None:
        self.__layout = layout
        
        self.__state_indicator._addStateIndicator(self.__layout)
        
        self.__method._addLine(layout=self.__layout)
        self.__port._addLine(layout=self.__layout)
        self.__baudrate._addLine(layout=self.__layout)
        self.__bytesize._addLine(layout=self.__layout)
        self.__parity._addLine(layout=self.__layout)
        self.__stopbits._addLine(layout=self.__layout)