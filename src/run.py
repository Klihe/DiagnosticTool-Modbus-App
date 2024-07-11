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
        window.commgroup.update_state("Searching for ports...", "yellow")
        
        ports.find_ports()
        window.grabber["port_option"].clear()
        window.grabber["port_option"].addItems(ports.available_ports)
        
        window.commgroup.update_state("Ports refreshed", "green")
            
    def connect() -> None:
        window.commgroup.update_state("Connecting...", "yellow")
        
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
        
        if device.is_connected:
            window.commgroup.update_state("Connected", "green")
        else: 
            window.commgroup.update_state("Disconnected", "red")
        
    def disconnect() -> None:
        window.commgroup.update_state("Disconnecting...", "yellow")
        
        if device.is_connected:
            device.disconnect()
            
        window.commgroup.update_state("Disconnected", "red")
        
    def read() -> None:
        window.commgroup.update_state("Reading...", "yellow")
        
        if device.is_connected:
            device.read()
            window.valuesgroup.update(device.data, True)
            
        window.commgroup.update_state("Read", "green")
        
    def readInInterval(checked) -> None:
        if not device.is_connected:
            return None
        
        if checked:
            window.grabber["readInInterval_timer"].start()
            window.grabber["readInInterval_timer"].setInterval(int(window.grabber["readInInterval_edit"].text()))
            window.grabber["readInInterval_timer"].timeout.connect(read)
        else:
            window.grabber["readInInterval_timer"].stop()
            window.grabber["readInInterval_timer"].timeout.disconnect(read)
        return None
    
    def write() -> None:
        window.commgroup.update_state("Writing...", "yellow")
        
        if device.is_connected:
            temp = window.valuesgroup.get()
            device.write(temp)
            
        window.commgroup.update_state("Write", "green")
        
    def save() -> None:
        window.commgroup.update_state("Saving...", "yellow")
        
        temp = window.valuesgroup.get()
        data.save(temp, window)
        
        window.commgroup.update_state("Saved", "green")
        
    def saveas() -> None:
        window.commgroup.update_state("Saving as...", "yellow")
        
        temp = window.valuesgroup.get()
        data.saveas(temp, window)
        
        window.commgroup.update_state("Saved as", "green")
        
    def open() -> None:
        window.commgroup.update_state("Opening...", "yellow")
        
        data.load(window)
        window.valuesgroup.update(data.data, False)
        
        window.commgroup.update_state("Opened", "green")
    
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