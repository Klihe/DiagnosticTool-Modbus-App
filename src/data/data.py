from PyQt6.QtWidgets import QFileDialog
import pandas as pd
import csv

# Data class - for saving, opening, etc.
class Data:
    def __init__(self) -> None:
        self.data = {
            "Coil": {
                "group": [], 
                "physical_address": [],
                "logical_address": [],
                "value": [],
                "name": [],
                "description": [],
                "notes": []
            },
            "Discrete input": {
                "group": [],
                "physical_address": [],
                "logical_address": [],
                "value": [],
                "name": [],
                "description": [],
                "notes": []
            },
            "Input register": {
                "group": [],
                "physical_address": [],
                "logical_address": [],
                "value": [],
                "name": [],
                "description": [],
                "notes": []
            },
            "Holding register": {
                "group": [],
                "physical_address": [],
                "logical_address": [],
                "value": [],
                "name": [],
                "description": [],
                "notes": []
            }
        }
        
        self.current_file_path = None
    
    # Read the data from the file
    def read(self, file_path: str) -> None:
        # Save the file path
        self.__file_path = file_path
        
        # Read the data from the file
        pure_data = pd.read_csv(self.__file_path, sep=";")
        # Convert the data to dictionary
        curr_data = pure_data.to_dict()
        
        # Save the data to the dictionary
        for i in range(len(curr_data["group"])):
            if str(curr_data["group"][i]) == "Coil":
                self.data["Coil"]["group"].append(curr_data["group"][i])
                self.data["Coil"]["physical_address"].append(curr_data["physical_address"][i])
                self.data["Coil"]["logical_address"].append(curr_data["logical_address"][i])
                self.data["Coil"]["value"].append(curr_data["value"][i])
                self.data["Coil"]["name"].append(curr_data["name"][i])
                self.data["Coil"]["description"].append(curr_data["description"][i])
                self.data["Coil"]["notes"].append(curr_data["notes"][i])
            elif str(curr_data["group"][i]) == "Discrete input":
                self.data["Discrete input"]["group"].append(curr_data["group"][i])
                self.data["Discrete input"]["physical_address"].append(curr_data["physical_address"][i])
                self.data["Discrete input"]["logical_address"].append(curr_data["logical_address"][i])
                self.data["Discrete input"]["value"].append(curr_data["value"][i])
                self.data["Discrete input"]["name"].append(curr_data["name"][i])
                self.data["Discrete input"]["description"].append(curr_data["description"][i])
                self.data["Discrete input"]["notes"].append(curr_data["notes"][i])
            elif str(curr_data["group"][i]) == "Input register":
                self.data["Input register"]["group"].append(curr_data["group"][i])
                self.data["Input register"]["physical_address"].append(curr_data["physical_address"][i])
                self.data["Input register"]["logical_address"].append(curr_data["logical_address"][i])
                self.data["Input register"]["value"].append(curr_data["value"][i])
                self.data["Input register"]["name"].append(curr_data["name"][i])
                self.data["Input register"]["description"].append(curr_data["description"][i])
                self.data["Input register"]["notes"].append(curr_data["notes"][i])
            elif str(curr_data["group"][i]) == "Holding register":
                self.data["Holding register"]["group"].append(curr_data["group"][i])
                self.data["Holding register"]["physical_address"].append(curr_data["physical_address"][i])
                self.data["Holding register"]["logical_address"].append(curr_data["logical_address"][i])
                self.data["Holding register"]["value"].append(curr_data["value"][i])
                self.data["Holding register"]["name"].append(curr_data["name"][i])
                self.data["Holding register"]["description"].append(curr_data["description"][i])
                self.data["Holding register"]["notes"].append(curr_data["notes"][i])
    
    # Write the data to the file    
    def write(self, file_path: str, data: dict) -> None:
        # Write the data to the file
        with open(file_path, mode='w', newline='') as file:
            # Write the data to the file
            writer = csv.writer(file, delimiter=';')
            
            # Write the header
            header = data.keys()
            # Write the data
            writer.writerow(header)
            
            # Write the rows
            rows = zip(*data.values())
            # Write the data
            writer.writerows(rows)
    
    # Save the data to the file
    def save(self, content, window) -> None:
        # If the file path is not set
        if not self.current_file_path:
            # Save the data to the file
            self.saveas(content, window)
        else:
            # Save the data to the file
            self.write(self.current_file_path, content)
    
    # Save the data to the file
    def saveas(self, content, window) -> None:
        # Open the file dialog
        file_dialog = QFileDialog()
        # Get the file path
        file_path, _ = file_dialog.getSaveFileName(window, "Save File", "", "CSV files (*.csv);;All files (*.*)")
        # If the file path is set
        if file_path:
            self.current_file_path = file_path
            # Save the data to the file
            self.write(self.current_file_path, content)
    
    # Open the file
    def open(self, window) -> bool:
        # Open the file dialog
        file_dialog = QFileDialog()
        # Get the file path
        file_path, _ = file_dialog.getOpenFileName(window, "Open File", "", "CSV files (*.csv);;All files (*.*)")
        # If the file path is set
        if file_path:
            # Read the header of the file
            with open(file_path, mode='r') as file:
                reader = csv.reader(file, delimiter=';')
                header = next(reader)
                if header == ['group', 'physical_address', 'logical_address', 'value', 'name', 'description', 'notes']:
                    self.read(file_path)
                    self.current_file_path = file_path
            return True
        return False
    