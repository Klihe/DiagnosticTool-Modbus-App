from PyQt6.QtWidgets import QFileDialog
import csv
import pandas as pd

def read_file(file_path: str) -> dict:
    pure_data = pd.read_csv(file_path, sep=";")
    curr_data = pure_data.to_dict()
    print(curr_data)
    
    return curr_data

def open_file(window) -> dict:
    file_dialog = QFileDialog()
    file_path, _ = file_dialog.getOpenFileName(window, "Open File", "", "CSV files (*.csv);;All files (*.*)")
    
    if file_path:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file, delimiter=';')
            header = next(reader)
            if header == ['group', 'physical_address', 'logical_address', 'value', 'name', 'description', 'notes']:
                return read_file(file_path)
