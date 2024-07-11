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
    
    def port_refresh() -> None:
        ports.find_ports()
        window.grabber["port_option"].clear()
        window.grabber["port_option"].addItems(ports.available_ports)
            
    def connect() -> None:
        if not device.is_connected:
            data = window.commgroup.get()
            
            device.connect(
                method=str(data["method"]),
                port=str(data["port"]),
                baudrate=int(data["baudrate"]),
                bytesize=int(data["bytesize"]),
                parity=str(data["parity"]),
                stopbits=int(data["stopbits"])
            )
        
    def disconnect() -> None:
        if device.is_connected:
            device.disconnect()
        
    def read() -> None:
        if device.is_connected:
            device.read()
            window.valuesgroup.update(device.data)
        
    def readInInterval(checked) -> None:
        if not device.is_connected:
            return None
        
        if checked:
            window.grabber["ReadInInterval_timer"].start()
            window.grabber["ReadInInterval_timer"].setInterval(int(window.grabber["ReadInInterval_edit"].text()))
            window.grabber["ReadInInterval_timer"].timeout.connect(read)
        else:
            window.grabber["ReadInInterval_timer"].stop()
            window.grabber["ReadInInterval_timer"].timeout.disconnect(read)
        return None
    
    def write() -> None:
        if device.is_connected:
            temp = window.valuesgroup.get()
            device.write(temp)
        
    def save() -> None:
        temp = window.valuesgroup.get()
        data.save(temp, window)
        
    def saveas() -> None:
        temp = window.valuesgroup.get()
        data.saveas(temp, window)
        
    def open() -> None:
        data.load(window)
        window.valuesgroup.update(data.data)
    
    window.grabber["port_refresh"].clicked.connect(port_refresh)
    window.grabber["connect"].triggered.connect(connect)
    window.grabber["disconnect"].triggered.connect(disconnect)
    window.grabber["read"].triggered.connect(read)
    window.grabber["readInInterval_action"].toggled.connect(readInInterval)
    window.grabber["write"].triggered.connect(write)
    window.grabber["save"].triggered.connect(save)
    window.grabber["saveas"].triggered.connect(saveas)
    window.grabber["open"].triggered.connect(open)
    
    window.show()
    app.exec()

if __name__ == '__main__':
    main()