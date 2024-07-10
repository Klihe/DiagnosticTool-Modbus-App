from pymodbus.client import ModbusSerialClient

class Device:
    def __init__(self) -> None:
        self._create()
        
    def _create(self) -> None:
        self.__client = None
        
        self.data = {
            "group": [],
            "physical_address": [],
            "logical_address": [],
            "value": [],
            "name": [],
            "description": [],
            "notes": [] 
        }
        self.is_connected = False
        
    def _clear_data(self) -> None:
        self.data["group"].clear()
        self.data["physical_address"].clear()
        self.data["logical_address"].clear()
        self.data["value"].clear()
        self.data["name"].clear()
        self.data["description"].clear()
        self.data["notes"].clear()
    
    def connect(self, method, port, baudrate, bytesize, parity, stopbits) -> None:
        self.__method = method
        self.__port = port
        self.__baudrate = baudrate
        self.__bytesize = bytesize
        self.__parity = parity
        self.__stopbits = stopbits
        
        self.__client = ModbusSerialClient(
            method=self.__method,
            port=self.__port,
            baudrate=self.__baudrate,
            bytesize=self.__bytesize,
            parity=self.__parity,
            stopbits=self.__stopbits
        )

        self.is_connected = True
        self.__client.connect()
    
    def disconnect(self) -> None:
        self.is_connected = False
        self.__client.close()
    
    def read(self) -> None:
        self._clear_data()

        address = 0

        while True:
            try:
                response = self.__client.read_coils(
                    address=address,
                    count=1,
                    slave=1
                )
                
                # Temporary variables
                group = "Coil"
                physical_address = address
                logical_address = address + 1
                value = response.bits[0]
                name = "None"
                description = "None"
                notes = "None"
                
            except Exception as e:
                print(f"Exception occurred: {e}")
                break
            
            # Append only if no exception
            self.data["group"].append(group)
            self.data["physical_address"].append(physical_address)
            self.data["logical_address"].append(logical_address)
            self.data["value"].append(value)
            self.data["name"].append(name)
            self.data["description"].append(description)
            self.data["notes"].append(notes)
            
            address += 1
            
        address = 0
        
        while True:
            try:
                response = self.__client.read_discrete_inputs(
                    address=address,
                    count=1,
                    slave=1
                )
                
                # Temporary variables
                group = "Discrete input"
                physical_address = address
                logical_address = address + 1
                value = response.bits[0]
                name = "None"
                description = "None"
                notes = "None"
                
            except Exception as e:
                print(f"Exception occurred: {e}")
                break
            
            # Append only if no exception
            self.data["group"].append(group)
            self.data["physical_address"].append(physical_address)
            self.data["logical_address"].append(logical_address)
            self.data["value"].append(value)
            self.data["name"].append(name)
            self.data["description"].append(description)
            self.data["notes"].append(notes)
            
            address += 1
        
        address = 0
        
        while True:
            try:
                response = self.__client.read_input_registers(
                    address=address,
                    count=1,
                    unit=1
                )
                
                # Temporary variables
                group = "Input register"
                physical_address = address
                logical_address = address + 1
                value = response.registers[0]
                name = "None"
                description = "None"
                notes = "None"
            
            except Exception as e:
                print(f"Exception occurred: {e}")
                break
            
            # Append only if no exception
            self.data["group"].append(group)
            self.data["physical_address"].append(physical_address)
            self.data["logical_address"].append(logical_address)
            self.data["value"].append(value)
            self.data["name"].append(name)
            self.data["description"].append(description)
            self.data["notes"].append(notes)
            
            address += 1
            
        address = 0
            
        while True:
            try:
                response = self.__client.read_holding_registers(
                    address=address,
                    count=1,
                    unit=1
                )
                
                # Temporary variables
                group = "Holding register"
                physical_address = address
                logical_address = address + 1
                value = response.registers[0]
                name = "None"
                description = "None"
                notes = "None"
                
            except Exception as e:
                print(f"Exception occurred: {e}")
                break
            
            # Append only if no exception
            self.data["group"].append(group)
            self.data["physical_address"].append(physical_address)
            self.data["logical_address"].append(logical_address)
            self.data["value"].append(value)
            self.data["name"].append(name)
            self.data["description"].append(description)
            self.data["notes"].append(notes)
            
            address += 1
            
    def write(self, data: dict) -> None:
        pass
    