from PyQt6.QtWidgets import QLabel, QComboBox, QLineEdit, QPushButton

import window.commgroup.constants as c

class CommLine:
    def __init__(self, descr: str, options: list=[None], custom: bool=True, refresh: bool=False) -> None:
        self.__label = descr
        self.__options = options
        self.__custom = custom
        self.__refresh = refresh
        
        self.__create()
        
    def __create(self) -> None:   
        self.__descr_label = QLabel(self.__label)
        self.__option_combobox = QComboBox()
        self.__option_combobox.addItems(self.__options)
        self.__option_custom = QLineEdit()
        self.__option_custom.hide()
        
        if self.__custom:
            self.__custom_switch = QPushButton("Custom")
            self.__custom_switch.setCheckable(True)

            self.__custom_switch.toggled.connect(self.__toggle)

        if self.__refresh:
            self.__refresh_button = QPushButton("Refresh")
            self.__refresh_button.clicked.connect(self.__click)
            
    def _addLine(self, layout, row: int) -> None:
        self.__layout = layout
        self.__row = row
        
        self.__layout.addWidget(self.__descr_label, self.__row, 0),
        self.__layout.addWidget(self.__option_combobox, self.__row, 1)
        self.__layout.addWidget(self.__option_custom, self.__row, 1)
        
        if self.__custom:
            self.__layout.addWidget(self.__custom_switch, self.__row, 2)
            
        if self.__refresh:
            self.__layout.addWidget(self.__refresh_button, self.__row, 3)
            
    def __toggle(self, checked) -> None:
        if checked:
            print("Custom switch checked")
            self.__option_custom.show()
            self.__option_combobox.hide()
        else:
            print("Custom switch unchecked")
            self.__option_combobox.show()
            self.__option_custom.hide()
            
            
    def __click(self) -> None:
        print("Refresh button clicked")
    
class CommGroup:
    def __init__(self) -> None:
        self.__line = {
            "method" : CommLine(descr="Method", options=c.METHOD_OPTIONS),
            "port" : CommLine(descr="Port", refresh=True),
            "baudrate" : CommLine(descr="Baudrate", options=c.BAUDRATE_OPTIONS),
            "parity" : CommLine(descr="Parity", options=c.PARITY_OPTIONS),
            "stopbits" : CommLine(descr="Stop Bits", options=c.STOPBITS_OPTIONS)
        }
        
    def addGroup(self, layout) -> None:
        self.__line["method"]._addLine(layout=layout, row=0)
        self.__line["port"]._addLine(layout=layout, row=1)
        self.__line["baudrate"]._addLine(layout=layout, row=2)
        self.__line["parity"]._addLine(layout=layout, row=3)
        self.__line["stopbits"]._addLine(layout, row=4)