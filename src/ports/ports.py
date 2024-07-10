import serial.tools.list_ports as lp
import ports.constants as c

class Ports:
    def __init__(self) -> None:
        self.available_ports = self.find_ports()
    
    def find_ports(self) -> None:
        inputs = lp.comports()
        self.available_ports = []
        
        for input in inputs:
            if input.device.startswith(c.PREFIX_PORT_MACOS):
                self.available_ports.append(input.device)