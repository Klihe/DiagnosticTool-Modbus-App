from PyQt6.QtWidgets import QLabel, QComboBox, QLineEdit, QPushButton

import window.commgroup.constants as c

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
            
    def _addLine(self, layout, row: int) -> None:
        self.__layout = layout
        self.__row = row
        
        self.__layout.addWidget(self.__grabber[f"{self.__mark}_descr"], self.__row, 0),
        self.__layout.addWidget(self.__grabber[f"{self.__mark}_option"], self.__row, 1)
        self.__layout.addWidget(self.__grabber[f"{self.__mark}_custom_opt"], self.__row, 1)
        
        if self.__custom:
            self.__layout.addWidget(self.__grabber[f"{self.__mark}_custom_swt"], self.__row, 2)
            
        if self.__refresh:
            self.__layout.addWidget(self.__grabber[f"{self.__mark}_refresh"], self.__row, 3)
            
    def __toggle(self, checked) -> None:
        if checked:
            print("Custom switch checked")
            self.__grabber[f"{self.__mark}_custom_opt"].show()
            self.__grabber[f"{self.__mark}_option"].hide()
        else:
            print("Custom switch unchecked")
            self.__grabber[f"{self.__mark}_option"].show()
            self.__grabber[f"{self.__mark}_custom_opt"].hide()
    
class CommGroup:
    def __init__(self, grabber) -> None:
        self.__method = CommLine(grabber, descr="Method", options=c.METHOD_OPTIONS)
        self.__port = CommLine(grabber, descr="Port", refresh=True)
        self.__baudrate = CommLine(grabber, descr="Baudrate", options=c.BAUDRATE_OPTIONS)
        self.__parity = CommLine(grabber, descr="Parity", options=c.PARITY_OPTIONS)
        self.__stopbits = CommLine(grabber, descr="Stop Bits", options=c.STOPBITS_OPTIONS)
        
    def addGroup(self, layout) -> None:
        self.__method._addLine(layout=layout, row=0)
        self.__port._addLine(layout=layout, row=1)
        self.__baudrate._addLine(layout=layout, row=2)
        self.__parity._addLine(layout=layout, row=3)
        self.__stopbits._addLine(layout, row=4)