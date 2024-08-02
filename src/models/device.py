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
        self.__client: ModbusSerialClient
        self.__numberOfItems: dict[str, int] = {
            "coils": 0,
            "discrete_inputs": 0,
            "input_registers": 0,
            "holding_registers": 0,
        }
        self.__data: dict[str, list] = {
            "group": [],
            "value": [],
        }

        self.state = State.DISCONNECTED
        self.working: bool = False
        self.error: str = ""

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

        if self.__client is None:
            self.error = "Client is None"
            return None

        if self.__client.connect():
            self.state = State.CONNECTED
            self.__number_of_items()
            self.read()
        else:
            self.state = State.DISCONNECTED
            self.error = "Connection failed"

    @set_working_state
    def disconnect(self) -> None:
        if self.__client is None:
            return

        self.__client.close()
        self.state = State.DISCONNECTED
        self.__clear_data()

    def __read_until_failure(self, read_method) -> int:
        address: int = 0

        while True:
            try:
                response = read_method(address=address, count=1, slave=1)
                bits = getattr(response, "bits", [])
                registers = getattr(response, "registers", [])

                if len(bits) == 0 and len(registers) == 0:
                    break

                if len(bits) > 0:
                    _ = bits[0]
                else:
                    _ = registers[0]
            except Exception:
                break

            address += 1

        return address

    def __number_of_items(self) -> None:
        if self.__client is None:
            return

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
        read_func: Callable,
        number_of_items: int,
        bits: Optional[bool] = False,
        registers: Optional[bool] = False,
    ) -> list:
        address: int = 0
        response: list = []

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
    def read(self) -> None:
        self.__clear_data()

        coil_response: list = self.__read_item(
            self.__client.read_coils, self.__numberOfItems["coils"], bits=True
        )

        discrete_inputs_response: list = self.__read_item(
            self.__client.read_discrete_inputs,
            self.__numberOfItems["discrete_inputs"],
            bits=True,
        )

        input_registers_response: list = self.__read_item(
            self.__client.read_input_registers,
            self.__numberOfItems["input_registers"],
            registers=True,
        )

        holding_registers_response: list = self.__read_item(
            self.__client.read_holding_registers,
            self.__numberOfItems["holding_registers"],
            registers=True,
        )

        self.__enter_data("Coil", coil_response)
        self.__enter_data("Discrete input", discrete_inputs_response)
        self.__enter_data("Input register", input_registers_response)
        self.__enter_data("Holding register", holding_registers_response)
