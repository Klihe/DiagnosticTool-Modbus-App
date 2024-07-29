import serial.tools.list_ports as lp
from config.settings import load_settings


def find_ports() -> list:
    config = load_settings()
    
    inputs = lp.comports()
    available_ports = []
    
    for input in inputs:
        if input.device.startswith(config["port_prefix"]["macOS"] or config["port_prefix"]["windows"] or config["port_prefix"]["linux"]):
            available_ports.append(input.device)
    
    print(available_ports)
    return available_ports
