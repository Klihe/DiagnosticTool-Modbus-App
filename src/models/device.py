from pymodbus.client import ModbusSerialClient
from enum import Enum
from typing import Optional, Callable, Any


class State(Enum):
    CONNECTED = 0
    DISCONNECTED = 1


class Device:
    def __init__(self, config: dict) -> None:
        self.__config = config

        self.__create()

    def __create(self) -> None:
        self.__client = None
        self.__numberOfItems = {
            "coils": None,
            "discrete_inputs": None,
            "input_registers": None,
            "holding_registers": None,
        }
        self.__data: dict = {
            "group": [],
            "value": [],
        }

        self.__state = State.DISCONNECTED
        self.working = False
        self.error = False

    def set_working_state(
        func: Callable[["Device", Any], Any],
    ) -> Callable[["Device", Any], None]:
        def wrapper(self: "Device", *args, **kwargs) -> None:
            self.working = True
            try:
                func(self, *args, **kwargs)
            finally:
                self.working = False

        return wrapper

    def __clear_data(self) -> None:
        for key in self.__data:
            self.__data[key] = []

    @set_working_state
    def connect(
        self,
        method: str,
        port: str,
        baudrate: str,
        bytesize: str,
        parity: str,
        stopbits: str,
    ) -> None:
        if not baudrate.isdigit():
            self.error = "Baudrate must be a number"
            return None
        elif not bytesize.isdigit():
            self.error = "Byte Size must be a number"
            return None
        elif not stopbits.isdigit():
            self.error = "Stop Bits must be a number"
            return None

        self.__client = ModbusSerialClient(
            method=method,
            port=port,
            baudrate=int(baudrate),
            bytesize=int(bytesize),
            parity=parity,
            stopbits=int(stopbits),
        )

        if self.__client.connect():
            self.__state = State.CONNECTED
            self.__number_of_items()
            self.read()
        else:
            self.__state = State.DISCONNECTED
            self.error = "Connection failed"

        print(self.__numberOfItems)

    @set_working_state
    def disconnect(self) -> None:
        self.__client.close()
        self.__state = State.DISCONNECTED
        self.__clear_data()

    def __read_until_failure(self, read_method) -> int:
        address = 0

        while True:
            try:
                response = read_method(address=address, count=1, slave=1)
                try:
                    response.bits[0]
                except:
                    response.registers[0]
            except:
                break
            address += 1

        return address

    def __number_of_items(self) -> None:
        self.__numberOfItems["coils"] = self.__read_until_failure(
            self.__client.read_coils
        )
        self.__numberOfItems["discrete_inputs"] = self.__read_until_failure(
            self.__client.read_discrete_inputs
        )
        self.__numberOfItems["input_registers"] = self.__read_until_failure(
            self.__client.read_input_registers
        )
        self.__numberOfItems["holding_registers"] = self.__read_until_failure(
            self.__client.read_holding_registers
        )

    def __divide_to_sequences(self, number: int) -> tuple[int, int]:
        full_chunks = number // self.__config["device"]["max_count"]
        partial_chunk = number % self.__config["device"]["max_count"]

        return full_chunks, partial_chunk

    def __enter_data(self, group: str, response: list) -> None:
        for i in range(len(response)):
            self.__data["group"].append(group)
            self.__data["value"].append(response[i])

    def __read_item(
        self,
        read_func: callable,
        number_of_items: int,
        bits: Optional[bool] = False,
        registers: Optional[bool] = False,
    ) -> None:
        address = 0
        response = []

        full_chunks, partial_chunk = self.__divide_to_sequences(number_of_items)

        for _ in range(full_chunks):
            curr_response = read_func(
                address=address, count=self.__config["device"]["max_count"], slave=1
            )
            if bits:
                list_response = curr_response.bits
            elif registers:
                list_response = curr_response.registers0
            else:
                raise ValueError("Either 'bits' or 'registers' must be True.")

            response.extend(list_response)
            address += self.__config["device"]["max_count"]

        if partial_chunk > 0:
            curr_response = read_func(address=address, count=partial_chunk, slave=1)
            if bits:
                list_response = curr_response.bits
            elif registers:
                list_response = curr_response.registers
            else:
                raise ValueError("Either 'bits' or 'registers' must be True.")

        response.extend(list_response)

        return response

    @set_working_state
    def read(self) -> dict:
        self.__clear_data()

        coil_response = self.__read_item(
            self.__client.read_coils, self.__numberOfItems["coils"], bits=True
        )

        discrete_inputs_response = self.__read_item(
            self.__client.read_discrete_inputs,
            self.__numberOfItems["discrete_inputs"],
            bits=True,
        )

        input_registers_response = self.__read_item(
            self.__client.read_input_registers,
            self.__numberOfItems["input_registers"],
            registers=True,
        )

        holding_registers_response = self.__read_item(
            self.__client.read_holding_registers,
            self.__numberOfItems["holding_registers"],
            registers=True,
        )

        self.__enter_data("Coil", coil_response)
        self.__enter_data("Discrete input", discrete_inputs_response)
        self.__enter_data("Input register", input_registers_response)
        self.__enter_data("Holding register", holding_registers_response)
