from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QThread, pyqtSignal

from window.window import Window
from device.device import Device
from ports.ports import Ports
from data.data import Data

import sys

# Create thread class 
"""_summary_
main thread - GUI
calc thread - (WorkerThread) - reading, writing, etc.
"""
class WorkerThread(QThread):
    finished = pyqtSignal(int)

    def __init__(self, target=None, args=(), kwargs={}, *, daemon=None):
        super().__init__()
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._daemon = daemon

    def run(self):
        result = self._target(*self._args, **self._kwargs)
        self.finished.emit(result)
        
    def set_function(self, target, args=(), kwargs={}):
        self._target = target
        self._args = args
        self._kwargs = kwargs

def main() -> None:
    # Create the application - PyQt6
    app  = QApplication(sys.argv)
    
    # Create the objects
    """_summary_
    window - (Window) - GUI
    device - (Device) - connection, reading, writing, etc.
    ports - (Ports) - searching for ports
    data - (Data) - saving, opening, etc.
    """
    
    window = Window()
    device = Device()
    ports = Ports()
    data = Data()
    
    calc_thread = WorkerThread()
    
    global is_readingInInterval
    is_readingInInterval = False
    
    def state_indicator(color: str) -> None:
        window.grabber["connect_btn"].setStyleSheet(f"background-color: {color};")
        window.grabber["disconnect_btn"].setStyleSheet(f"background-color: {color};")
        window.grabber["read_btn"].setStyleSheet(f"background-color: {color};")
        window.grabber["write_btn"].setStyleSheet(f"background-color: {color};")
        window.grabber["readInInterval_action_btn"].setStyleSheet(f"background-color: {color};")
    
    # For refresh button in the port line
    def port_refresh() -> None:
        # When function is in progress
        window.commgroup.update_state("Searching for ports...", "#2D4EB0")
        
        # Function for refreshing the ports
        def refresh_ports():
            # Check the available ports
            ports.find_ports()
            # Clear the port options and add the available ports
            window.grabber["port_option"].clear()
            window.grabber["port_option"].addItems(ports.available_ports)
        
        # Function for updating the state
        def refresh_ports_update_state():
            # If there are no available ports
            if ports.available_ports == []:
                window.commgroup.update_state("Error: No ports found", "#FA9938")
                return None
            # If there are available ports
            else:
                window.commgroup.update_state("Ports: Ready", "#0D825D")
                return None
        
        # Set the function for the thread
        calc_thread.set_function(refresh_ports)
        calc_thread.finished.connect(refresh_ports_update_state)
        calc_thread.start()
            
    # Function for connect button
    def connect() -> None:
        global is_readingInInterval
        
        if is_readingInInterval or device.is_connected:
            return None
        
        state_indicator("#D53734")
        window.grabber["connect_btn"].setStyleSheet("background-color: #FA9938;")
        
        # When function is in progress
        window.commgroup.update_state("Connecting...", "#2D4EB0")
        
        # Get the data from the commgroup
        if not device.is_connected:
            data = window.commgroup.get()

            # Check if the port is selected
            if data["port"] == '':
                window.commgroup.update_state("Error: Port isn't selected", "#FA9938")
                return None
        
        # Function for connecting the device
        def connect_thread():
            if not device.is_connected:
                device.connect(
                    method=str(data["method"]),
                    port=str(data["port"]),
                    baudrate=int(data["baudrate"]),
                    bytesize=int(data["bytesize"]),
                    parity=str(data["parity"]),
                    stopbits=int(data["stopbits"])
                )
        
        # Function for updating the state
        def connect_update_state():
            if not is_readingInInterval:
                state_indicator("#0D825D")
            window.grabber["connect_btn"].setStyleSheet("background-color: #D53734;")
            
            if device.is_connected:
                window.commgroup.update_state("Device: Ready", "#0D825D")
            else: 
                window.commgroup.update_state("Device: Disconnected", "#D53734")
        
        # Set the function for the thread
        calc_thread.set_function(connect_thread)
        calc_thread.finished.connect(connect_update_state)
        calc_thread.finished.connect(lambda: window.valuesgroup.update(device.data, True))
        calc_thread.start()
    
    # Function for disconnect button   
    def disconnect() -> None:
        global is_readingInInterval
        
        if is_readingInInterval or device.is_connecting:
            return None
        
        state_indicator("#D53734")
        window.grabber["disconnect_btn"].setStyleSheet("background-color: #FA9938;")
        
        # When function is in progress
        window.commgroup.update_state("Disconnecting...", "#2D4EB0")
        
        # If the device is connected - disconnect
        if device.is_connected:
            device.disconnect()
            window.valuesgroup.clear()
        else:
            window.commgroup.update_state("Error: Non-connected device", "#FA9938")
            return None
        
        state_indicator("#D53734")
        window.grabber["connect_btn"].setStyleSheet("background-color: #0D825D;")
        
        window.commgroup.update_state("Device: Disconnected", "#D53734")
    
    # Function for read button    
    def read() -> None:
        global is_readingInInterval
        # When function is in progress
        if not is_readingInInterval or device.is_connecting:
            state_indicator("#D53734")
            window.grabber["read_btn"].setStyleSheet("background-color: #FA9938;")
        
        window.commgroup.update_state("Reading...", "#2D4EB0")
        
        # If the device isn't connected - Error
        if not device.is_connected:
            window.commgroup.update_state("Error: Non-connected device", "#FA9938")
            return None
        
        # Function for reading the data from the device
        def read_thread():
            if device.is_connected:
                device.read()
                
        def read_update_state():
            if not is_readingInInterval:
                state_indicator("#0D825D")
                window.grabber["connect_btn"].setStyleSheet("background-color: #D53734;")
        
            window.commgroup.update_state("Ready", "#0D825D")
                
        calc_thread.set_function(read_thread)
        calc_thread.finished.connect(lambda: window.valuesgroup.update(device.data, True))
        calc_thread.finished.connect(read_update_state)
        calc_thread.start()
        
    # Function for read in interval action
    def readInInterval(checked) -> None:
        global is_readingInInterval
        # When device isn't connected - Error
        if device.is_connecting:
            return None
        if not device.is_connected:
            window.commgroup.update_state("Error: Non-connected device", "#FA9938")
            return None
        
        # If button is checked - start the timer
        if checked:
            is_readingInInterval = True
            state_indicator("#D53734")
            window.grabber["readInInterval_action_btn"].setStyleSheet("background-color: #FA9938;")
            window.grabber["readInInterval_timer"].start()
            # Set the interval - get time from the edit
            window.grabber["readInInterval_timer"].setInterval(int(window.grabber["readInInterval_edit"].text()))
            window.grabber["readInInterval_timer"].timeout.connect(read)
            window.grabber["read_btn"].disconnect()
        else:
            is_readingInInterval = False
            state_indicator("#0D825D")
            window.grabber["connect_btn"].setStyleSheet("background-color: #D53734;")
            window.grabber["readInInterval_timer"].stop()
            window.grabber["readInInterval_timer"].timeout.disconnect(read)
            window.grabber["read_btn"].triggered.connect(read)
        return None
    
    # Function for write button
    def write() -> None:
        global is_readingInInterval
        
        if is_readingInInterval or device.is_connecting:
            return None
        
        # When function is in progress
        window.commgroup.update_state("Writing...", "#2D4EB0")
        
        state_indicator("#D53734")
        window.grabber["write_btn"].setStyleSheet("background-color: #FA9938;")
        
        # If the device isn't connected - Error
        if not device.is_connected:
            window.commgroup.update_state("Error: Non-connected device", "#FA9938")
            return None
        
        # Function for writing the data to the device
        def write_thread():
            # get values from table write them to the device and update table
            if device.is_connected:
                temp = window.valuesgroup.get()
                device.write(temp)
                
        def write_update_state():
            state_indicator("#0D825D")
            window.grabber["connect_btn"].setStyleSheet("background-color: #D53734;")
        
            window.commgroup.update_state("Device: Ready", "#0D825D")

        calc_thread.set_function(write_thread)
        calc_thread.finished.connect(write_update_state)
        calc_thread.start()
    
    # Function for save button
    def save() -> None:
        # When function is in progress
        window.commgroup.update_state("Saving...", "#2D4EB0")
        
        if not device.is_connected:
            window.commgroup.update_state("Error: No data found in the table.", "#FA9938")
            return None
        
        # Get data and save them
        temp = window.valuesgroup.get()
        data.save(temp, window)
        
        window.commgroup.update_state("Device: Ready", "#0D825D")
    
    # Function for save as button  
    def saveas() -> None:
        # When function is in progress
        window.commgroup.update_state("Saving as...", "#2D4EB0")
        
        if not device.is_connected:
            window.commgroup.update_state("Error: No data found in the table", "#FA9938")
            return None
        
        # Get data and save them
        temp = window.valuesgroup.get()
        data.saveas(temp, window)
        window.setWindowTitle(f"{window.windowTitle().split('-')[0]} - {data.current_file_path}")
        
        window.commgroup.update_state("Device: Ready", "#0D825D")
    
    # Function for open button
    def open() -> None:
        # When function is in progress
        window.commgroup.update_state("Opening...", "#2D4EB0")
        
        if not device.is_connected:
            window.commgroup.update_state("Error: Table not prepared", "#FA9938")
            return None
        
        if device.table_is_imported:
            window.commgroup.update_state("Error: Data already imported; reconnect device.", "#FA9938")
            return None
        
        # Open the file and update the table
        device.table_is_imported = data.open(window)
        window.valuesgroup.update(data.data, False)
        window.setWindowTitle(f"{window.windowTitle().split('-')[0]} - {data.current_file_path}")
        
        window.commgroup.update_state("Device: Ready", "#0D825D")
    
    # Set the functions to the buttons
    window.grabber["port_refresh"].clicked.connect(port_refresh)
    window.grabber["connect"].triggered.connect(connect)
    window.grabber["disconnect"].triggered.connect(disconnect)
    window.grabber["read"].triggered.connect(read)
    window.grabber["readInInterval_action"].toggled.connect(readInInterval)
    window.grabber["write"].triggered.connect(write)
    window.grabber["save"].triggered.connect(save)
    window.grabber["saveas"].triggered.connect(saveas)
    window.grabber["open"].triggered.connect(open)
    
    # Show the window
    window.show()
    app.exec()

if __name__ == '__main__':
    main()