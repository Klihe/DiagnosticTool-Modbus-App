from PyQt6.QtWidgets import QFileDialog, QMainWindow
import csv
import pandas as pd

global curr_file_path

def read_file(file_path: str) -> dict:
    pure_data = pd.read_csv(file_path, sep=";")
    curr_data = pure_data.to_dict(orient='list')
    
    data: dict = {
        'group': [],
        'physical_address': [],
        'logical_address': [],
        'value': [],
        'name': [],
        'description': [],
        'notes': []
    }
    
    for i in range(len(curr_data["group"])):
        data['group'].append(curr_data["group"][i])
        data['physical_address'].append(curr_data["physical_address"][i])
        data['logical_address'].append(curr_data["logical_address"][i])
        data['value'].append(curr_data["value"][i])
        data['name'].append(curr_data["name"][i])
        data['description'].append(curr_data["description"][i])
        data['notes'].append(curr_data["notes"][i])

    return data

def write_file(file_path: str, data: dict) -> None:
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        header = data.keys()
        writer.writerow(header)
        rows = zip(*data.values())
        writer.writerows(rows)

def open_file(window: QMainWindow) -> dict:
    file_dialog = QFileDialog()
    file_path, _ = file_dialog.getOpenFileName(window, "Open File", "", "CSV files (*.csv);;All files (*.*)")
    
    if file_path:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file, delimiter=';')
            header = next(reader)
            if header == ['group', 'physical_address', 'logical_address', 'value', 'name', 'description', 'notes']:
                return read_file(file_path)
    return {}
            
def save_file(window: QMainWindow, data: dict) -> None:
    global curr_file_path
    if curr_file_path:
        write_file(curr_file_path, data)
    else:
        save_as_file(window, data)
        
def save_as_file(window: QMainWindow, data: dict) -> None:
    global curr_file_path
    file_dialog = QFileDialog()
    file_path, _ = file_dialog.getSaveFileName(window, "Save File", "", "CSV files (*.csv);;All files (*.*)")
    
    if file_path:
        write_file(file_path, data)
        curr_file_path = file_path

if __name__ == "__main__":
    data = read_file('bin/data.csv')
    write_file('bin/data2.csv', data)