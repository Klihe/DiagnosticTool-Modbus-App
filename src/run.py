from PyQt6.QtWidgets import QApplication

from window.window import Window
from device.device import Device
from ports.ports import Ports
from data.data import Data

import sys

def main() -> None:
    app  = QApplication(sys.argv)
    
    window = Window()
    device = Device()
    ports = Ports()
    data = Data()
    
    read_from = "device"     
    
    def port_refresh() -> None:
        ports.find_ports()
        window.grabber["port_option"].clear()
        window.grabber["port_option"].addItems(ports.available_ports)
            
    def connect() -> None:
        if not device.is_connected:
            device.connect(
                method=window.grabber["method_option"].currentText(),
                port=window.grabber["port_option"].currentText(),
                baudrate=int(window.grabber["baudrate_option"].currentText()),
                bytesize=int(window.grabber["byte size_option"].currentText()),
                parity=window.grabber["parity_option"].currentText(),
                stopbits=int(window.grabber["stop bits_option"].currentText())
            )
        
    def disconnect() -> None:
        if device.is_connected:
            device.disconnect()
        
    def read() -> None:
        if window.grabber["ReadFromDevice"].isChecked():
            device.read()
            window.valuesgroup.update(device.data)
        elif window.grabber["ReadFromCSV"].isChecked():
            data.read("bin/data0.csv")
            window.valuesgroup.update(data.data)
        else:
            return
        

    window.grabber["port_refresh"].clicked.connect(port_refresh)
    window.grabber["Connect"].triggered.connect(connect)
    window.grabber["Disconnect"].triggered.connect(disconnect)
    window.grabber["read"].triggered.connect(read)
    
    window.show()
    app.exec()

if __name__ == '__main__':
    main()